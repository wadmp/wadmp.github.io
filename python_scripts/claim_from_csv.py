#!/usr/bin/env python

# Python script which uses the WADMP public API to create a number of devices.
#
# Ben Kinsella, January 2020
# Copyright Advantech B+B SmartWorx, 2020
#
# Version 0.1
# This version was written and tested using Python 3.6.8 on Ubuntu 18.04

import argparse
import csv
import requests
import json
import sys
import logging


def parse_args():
    """Parse command-line arguments
    """
    parser = argparse.ArgumentParser(description="Claim devices to a company on WA/DMP")

    # Positional arguments:

    parser.add_argument("CSVfile",
                        help="Path to CSV file.",
                        type=str)
    
    parser.add_argument("Company",
                        help="Company name. \
                            Check the code for the default!",
                        type=str,
                        default='Company X')

    # Optional arguments:
    
    parser.add_argument("-host",
                        help="URL of the WADMP server's API gateway. \
                                Check the code for the default!",
                        type=str,
                        default='https://gateway.staging.wadmp.com')

    parser.add_argument("-username",
                        help="Username. \
                                Check the code for the default!",
                        type=str,
                        default='email')

    parser.add_argument("-password",
                        help="Password. \
                                Check the code for the default!",
                        type=str,
                        default='password')

    parser.add_argument("-loglevel",
                        help="Log verbosity level. The higher the level, the fewer messages that will be logged. \
                                Default = info (second lowest)",
                        type=str,
                        choices=['debug', 'info', 'warning', 'error', 'critical'],
                        default='info')

    return parser.parse_args()


def main(args):
    """ Main function
    """

    """
    A log message will only be emitted if the message level is greater than
    or equal to the configured level of the logger.
    """
    LOG_LEVELS = {'critical': logging.CRITICAL,
                'error':    logging.ERROR,
                'warning':  logging.WARNING,
                'info':     logging.INFO,
                'debug':    logging.DEBUG
                }

    # The user can specify specify -loglevel DEBUG or -loglevel debug
    loglevel = LOG_LEVELS[args.loglevel.lower()]

    logging.basicConfig(level=loglevel,
                        format='%(name)-12s %(levelname)-8s %(message)s')

    base_path = "api"

    # We will be making multiple requests to the same host, so we want to re-use the underlying TCP connection.
    # See http://docs.python-requests.org/en/master/user/advanced/
    session = requests.Session()

    auth_token = login(session, args.host, args.username, args.password)

    # Get the company ID
    company_id = None
    companies = get_companies(session, auth_token, args.host, base_path)
    for company in companies:
        if company['name'] == args.Company:
            company_id = company['id']
            break

    if company_id:
        logging.info(f"Company {args.Company} has ID {company_id}")
    else:
        logging.error(f"Company {args.Company} not found!")
        sys.exit()

    with open(args.CSVfile, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            logging.info(row)

            serial_number = row[0]
            logging.info(f"Serial Number {serial_number}")

            mac = row[1]
            logging.info(f"MAC {mac}")

            imei = row[2]
            logging.info(f"IMEI {imei}")

            device = {
                "serial_number": serial_number,
                "mac_address": mac,
                "imei": imei,
                "company_id": company_id
            }
            claim_device(session, auth_token, args.host, base_path, device)


def login(session, base_url, username, password):
    """Login to the system, and return a token
    """
    url = f"{base_url}/public/auth/connect/token"
    credentials = {'username': username,
                   'password': password,
                   'client_id': 'python',
                   'grant_type': 'password'}
    logging.debug(f"\nSending POST request to {url} with:\n"
        f"    credentials={credentials}")
    response = session.post(url, data=credentials)

    logging.debug(response.status_code)
    try:
        logging.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logging.debug(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()["access_token"]
    else:
        logging.error("Failed to login!")
        sys.exit(1)	


def get_device_families(session, auth_token, base_url, base_path, name=None):
    """Retrieves the list of families in the system
    """
    url = f"{base_url}/{base_path}/identity/device-families"
    header = {'Authorization': f'Bearer {auth_token}'}
    logging.debug(f"\nSending GET request to {url} with:\n"
        f"    header={header}\n"
        f"    name={name}\n")
    query = {'name': name}
    response = session.get(url, params=query, headers=header)

    logging.info(response.status_code)
    try:
        logging.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logging.debug(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']
    else:
        logging.error("Failed to retrieve the list of Families!")
        return None


def get_device_types(session, auth_token, base_url, base_path, family_id=None):
    """Retrieves the list of device types belonging to a particular family
    """
    url = f"{base_url}/{base_path}/identity/device-families/{family_id}/device-types"
    header = {'Authorization': f'Bearer {auth_token}'}
    logging.debug(f"\nSending GET request to {url} with:\n"
        f"    header={header}\n")
    response = session.get(url, headers=header)

    logging.debug(response.status_code)
    try:
        logging.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logging.debug(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']
    else:
        logging.error("Failed to retrieve the list of Types!")
        return None


def create_device(session, auth_token, base_url, base_path, model=None):
    """Create a device in the system.
    """
    url = f"{base_url}/{base_path}/identity/devices"
    header = {'Authorization': f'Bearer {auth_token}'}
    logging.debug(f"\nSending POST request to {url} with:\n"
        f"    header={header}\n"
        f"    model={model}\n")
    response = session.post(url, headers=header, json=model)

    logging.debug(response.status_code)
    try:
        logging.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logging.debug(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']['id']
    else:
        logging.error("Failed to create device!")
        return None


def form_MAC_address(serial_number):
    if len(serial_number) < 12:
        id = serial_number.zfill(12)
    else:
        id = serial_number[:12]
    mac = "{0}{1}:{2}{3}:{4}{5}:{6}{7}:{8}{9}:{10}{11}".format(
        id[0], id[1], id[2], id[3], id[4], id[5],
        id[6], id[7], id[8], id[9], id[10], id[11]
    )
    return mac


def get_companies(session, auth_token, base_url, base_path, name=None):
    """Retrieves the list of companies in the system
    """
    url = f"{base_url}/{base_path}/companies"
    header = {'Authorization': f'Bearer {auth_token}'}
    logging.debug(f"\nSending GET request to {url} with:\n"
        f"    header={header}\n"
        f"    name={name}\n")
    query = {'name': name}
    response = session.get(url, params=query, headers=header)

    logging.info(response.status_code)
    try:
        logging.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logging.debug(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']
    else:
        logging.error("Failed to retrieve the list of Companies!")
        return None


def claim_device(session, auth_token, base_url, base_path, model=None):
    """Claim a device to a company.
    """
    url = f"{base_url}/{base_path}/identity/devices/claim"
    header = {'Authorization': f'Bearer {auth_token}'}
    logging.debug(f"\nSending POST request to {url} with:\n"
        f"    header={header}\n"
        f"    model={model}\n")
    response = session.post(url, headers=header, json=model)

    logging.debug(response.status_code)
    try:
        logging.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logging.debug(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']['id']
    else:
        logging.error("Failed to claim device!")
        return None


if __name__ == "__main__":
    args = parse_args()
    main(args)
