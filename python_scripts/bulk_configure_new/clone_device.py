import requests
import argparse
import re
import json
import sys
import csv

from lib.ApiConsumer import ApiConsumer
from lib.CloningTool import CloningTool
from lib.Models      import DeviceModel

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

def check_device_types(type1, type2, ignore_err):
    if type1['type_id'] != type2['type_id']:
        if not ignore_err:
            raise RuntimeError(f"Error: Device types differ ({type1['name']} != {type2['name']})")
        print(f"Warning: Device types differ ({type1['name']} != {type2['name']})", file = sys.stderr)
        
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
def get_column_from_csv(csv_file, col_name):
    with open(csv_file, encoding="UTF-8", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        index = None
        result = []
        for row in csvreader:
            if not index:
                try:
                    index = row.index(col_name)
                except Exception:
                    pass
                continue
            result.append(row[index])
        return result

#########################################################
# Reads MAC addresses from CSV, fixes their format and 
# returns them as a list.
def get_macs_from_csv(csv_file):
    macs = get_column_from_csv(csv_file, 'Mac Address')
    macs = list(filter(lambda mac: mac != '', macs)) # Remove empty values
    bad_macs = list(filter(lambda mac: not is_mac_address(mac), macs))
    if len(bad_macs) > 0:
            raise RuntimeError(f"Invalid MAC addresses in CSV file: {str(bad_macs)}")
    macs = list(map(lambda mac: fix_mac(mac), macs))
    return macs

#########################################################
#########################################################

if __name__ == "__main__":
    args = parse_args()
    validate_args(args)

    api = ApiConsumer(args.url)
    api.login(args.username, args.password)

    src_device  = get_device_data(api, args.src_mac)
    dst_devices = []
    
    if args.dest_mac:
        dst_devices.append(get_device_data(api, args.dest_mac)) 

    if args.dest_csv:
        macs = get_macs_from_csv(args.dest_csv)
        dst_devices += list(map(lambda mac: get_device_data(api, mac), macs))
    
    for dst_device in dst_devices:
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
