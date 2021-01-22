#!/usr/bin/python3
"""
This script uses the public API to copy applications, firmware and 
their settings between devices.

Examples of usage:
    python3 ./clone_device.py --src-mac 00:AA:AA:AA:AA:AA --dest-mac 00:BB:BB:BB:BB:BB --username test@advantech.com --password 123456
    python3 ./clone_device.py --src-mac 00:AA:AA:AA:AA:AA --dest-csv ./xxx.csv --username test@advantech.com --password 123456

Example of the .csv file can be found at:
   ./resources/clone_device_test.csv

Ondrej Fabianek, December 2020
Version 0.3
"""
import requests
import argparse
import re
import json
import sys
import csv

from lib.ApiConsumer import ApiConsumer
from lib.CloningTool import CloningTool
from lib.Models      import DeviceModel

COL_MAC = 'Mac Address'

def parse_args():
    parser = argparse.ArgumentParser(description="Clones a device on WADMP.")

    # Positional arguments:
    parser.add_argument("--src-mac",
                        help="MAC of the source device.",
                        type=str)

    parser.add_argument("--dest-mac",
                        help="MAC of the destination device.",
                        type=str)

    parser.add_argument("--dest-csv",
                        help="CSV file containing MAC addresses of destination devices.",
                        type=str)

    parser.add_argument("--username",
                        help="Username.",
                        type=str,
                        required=True)

    parser.add_argument("--password",
                        help="Password.",
                        type=str,
                        required=True)

    parser.add_argument("--ignore-type",
                        help="Allow the destination device to be of a different type than the source device.",
                        action="store_true",
                        default=False)

    parser.add_argument("--skip-fw-config",
                        help="Do not clone firmware configuration.",
                        action="store_true",
                        default=False)

    parser.add_argument("--skip-fw-version",
                        help="Do not clone firmware version.",
                        action="store_true",
                        default=False)

    parser.add_argument("--skip-apps-config",
                        help="Do not clone apps configuration.",
                        action="store_true",
                        default=False) 

    parser.add_argument("--skip-apps",
                        help="Do not clone router apps.",
                        action="store_true",
                        default=False) 

    parser.add_argument("--skip-apps-unpinned",
                        help="Do not clone unpinned apps.",
                        action="store_true",
                        default=False)    

    parser.add_argument("--url",
                        help="Default: 'https://gateway.wadmp.com'",
                        type=str,
                        default="https://gateway.wadmp.com")

    parser.add_argument("--no-prompt",
                        help="Do not prompt the user for confirmation.",
                        action="store_true",
                        default=False)

    args = parser.parse_args()
    return fix_args(args)

def is_mac_address(x):
    return re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", x.lower())

def validate_args(args):
    if not is_mac_address(args.src_mac):
        raise RuntimeError(f"Invalid MAC address: '{args.src_mac}'")
    if args.dest_mac and not is_mac_address(args.dest_mac):
        raise RuntimeError(f"Invalid MAC address: '{args.dest_mac}'")
    if not args.username:
        raise RuntimeError(f"Missing '--username <user>' mandatory parameter.")
    if not args.password:
        raise RuntimeError(f"Missing '--password <pass>' mandatory parameter.")
    if not args.dest_mac and not args.dest_csv:
        raise RuntimeError(f"Missing destination parameter (use '--dest-csv <file>' or '--dest-mac <mac>'")

def fix_args(args):
    if not args.url.startswith("http"):
        args.url = f"https://{args.url}"
    return args

#########################################################
# Unless 'ignore_err' argument is set to true, throws 
# error when types do not match.
def check_device_types(type1, type2, ignore_err):
    if type1['type_id'] != type2['type_id']:
        if not ignore_err:
            raise RuntimeError(f"Error: Device types differ ({type1['name']} != {type2['name']})")
        print(f"Warning: Device types differ ({type1['name']} != {type2['name']})", file = sys.stderr)

#########################################################
# Downloads info about a device that has the given MAC
# and parses it into our model.        
def get_device_data(api, device_mac):
    resp = api.device.get_by_mac(device_mac)
    if resp.status_code != requests.codes['ok']:
        raise RuntimeError(f"Couldn't get device [{device_mac}]: {str(resp.json())}")
    return DeviceModel(resp.json()['data'])

#########################################################
# Takes MAC in format "AABBCCDDEEFF" and converts it to 
# "AA:BB:CC:DD:EE:FF"
def fix_mac(mac):
    if not ':' in mac:
        mac = ':'.join(mac[i:i+2] for i in range(0,12,2))
    return mac

#########################################################
# Looks for column named <col_name> and returns list 
# of values from this column.
def csv_get_column(csv_file, col_name):
    with open(csv_file, encoding="UTF-8", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        index = None
        result = []
        for row in csvreader:
            if index == None:
                try:
                    index = row.index(col_name)
                except Exception:
                    pass
                continue
            result.append(row[index])
        return result

#########################################################
# We locate the row with column names (it might not be the
# first row in the file) by searching for 'Mac Address'
# string.
def csv_get_col_names(csv_file):
    with open(csv_file, encoding="UTF-8", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        for row in csvreader:
            try:
                row.index(COL_MAC)
                return row
            except Exception:
                pass

#########################################################
# Converts contents of csv_file into a dictionary, where
# keys are column names and values are lists of values 
# from those columns.
def csv_to_dict(csv_file):
    col_names = csv_get_col_names(csv_file)
    result = dict()
    for col_name in col_names:
        result[col_name] = csv_get_column(csv_file, col_name)
    return result

#########################################################
# This method goes through contents od csv_dict and 
# extracts those columns whose names have format: 
# $APP_VERSION:SECTION_ID:SETTING_NAME. It also includes
# the column with mac addresses.
def extract_site_specific_changes(csv_dict):
    # Item[0] is name of the key and Item[1] would be the value.
    return dict(filter(lambda item: re.match(r'^\$[0-9]+:[0-9]+:[A-Z_]+$', item[0]) or item[0] == COL_MAC, csv_dict.items()))

#########################################################
# Extract only those values from the sites_specific_dict
# that are related to the given mac.
def get_site_specific_by_mac(mac, site_specific_dict):
    result = dict()
    index = site_specific_dict[COL_MAC].index(mac)
    for key, values in site_specific_dict.items():
        result[key] = values[index]
    return result

#########################################################
# Updates device configuration (firmware/user modules) by 
# the contents of the changes_dict.
def set_site_specific_changes(api, mac, changes_dict):
    sections=[]
    print("Applying site specific changes:")
    for key, value in changes_dict.items():
        if not value or key == COL_MAC:
            continue
        app_version_id, section_id, setting_name = key.split(':')
        app_version_id = app_version_id[1:] # Remove starting '$' character
        set_config = setting_name+"="+value+"\n"
        sections.append({'section_id': section_id, 'set_config': set_config})
        print(set_config[:-1])
    resp = api.device.update_settings(mac, app_version_id, sections)
    if resp.status_code != requests.codes['ok']:
        raise RuntimeError(f"Site specific setting {set_config[:-1]} was not applied ({resp.status_code}) {resp.text}")
    

#########################################################
# 
def prompt_csv_ok(site_specific_dict):
    print(f'Found {len(site_specific_dict.keys())-1} columns with site specific settings in CSV.')
    while True:
        answer = input("Continue? [y/n]: ")
        if answer == "n":
            exit()
        if answer == "y":
            return

#########################################################
#########################################################

if __name__ == "__main__":
    args = parse_args()
    validate_args(args)

    api = ApiConsumer(args.url)
    api.login(args.username, args.password)

    src_device  = get_device_data(api, args.src_mac)
    dst_devices = []
    site_specific_dict = dict()

    if args.dest_mac:
        dst_devices.append(get_device_data(api, args.dest_mac)) 

    if args.dest_csv:
        csv_dict = csv_to_dict(args.dest_csv)
        site_specific_dict = extract_site_specific_changes(csv_dict)
        if not args.no_prompt:
            prompt_csv_ok(site_specific_dict)
        dst_devices += list(map(lambda mac: get_device_data(api, mac), csv_dict[COL_MAC]))
    
    for dst_device in dst_devices:
        if len(dst_devices) > 1:
            print("\n*************************")
            print(f"Device {dst_device.mac}:")
            print("*************************\n")

        check_device_types(src_device.type, dst_device.type, args.ignore_type)
        
        if args.skip_apps_unpinned:
            src_device.apps_installed = list(filter(lambda app: app['is_pinned'] == True, src_device.apps_installed))
            dst_device.apps_installed = list(filter(lambda app: app['is_pinned'] == True, dst_device.apps_installed))

        if not args.skip_fw_version:
            CloningTool.clone_firmware(api, src_device, dst_device)
        
        if not args.skip_fw_config:
            CloningTool.clone_firmware_settings(api, src_device, dst_device)
        
        if not args.skip_apps:
            CloningTool.clone_apps(api, src_device, dst_device)
            if not args.skip_apps_config:
                CloningTool.clone_apps_settings(api, src_device, dst_device)

        if len(site_specific_dict.keys()) > 1: # If CSV is used, this dict will at minimum contain 'Mac Address' column.
            ss_dict = get_site_specific_by_mac(dst_device.mac, site_specific_dict)
            set_site_specific_changes(api, dst_device.mac, ss_dict)
