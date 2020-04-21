#!/usr/bin/env python

# Python script which uses the WADMP public API to delete a number of devices.
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
    parser = argparse.ArgumentParser(description="Delete devices from WA/DMP")

    # Positional arguments:

    parser.add_argument("CSVfile",
                        help="Path to CSV file.",
                        type=str)

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

    with open(args.CSVfile, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip the first row
        for row in csvreader:
            logging.info(row)

            mac = row[2]
            logging.info(f"MAC {mac}")

            delete_device(session, auth_token, args.host, base_path, mac)


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


def delete_device(session, auth_token, base_url, base_path, mac_address):
    """Delete a device.
    """
    url = f"{base_url}/{base_path}/identity/devices/{mac_address}"
    header = {'Authorization': f'Bearer {auth_token}'}
    logging.debug(f"\nSending DELETE request to {url} with:\n"
        f"    header={header}\n")
    response = session.delete(url, headers=header)

    logging.debug(response.status_code)
    try:
        logging.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logging.debug(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['success']
    else:
        logging.error("Failed to delete device!")
        return None


if __name__ == "__main__":
    args = parse_args()
    main(args)
