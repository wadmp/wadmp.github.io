#! /usr/bin/env python

"""
This script uses the public API to read the applications (both Firmware and User Modules),
from multiple devices.

Ben Kinsella, July 2020
Copyright Advantech B+B SmartWorx, 2020

Version 0.4

Last tested on Ubuntu 18.04 with Python 3.6, and on Windows 10 with Python 3.7
"""

# Standard library
import argparse
import os
import csv
import json
import sys
import logging
import logging.config
import time
import unittest

# pip
import requests
import pandas as pd


BASE_PATH = "api"


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description="Read applications from all devices")

    # Positional arguments:

    parser.add_argument("devices", help="CSV file of devices", type=str, default="ALL")

    # Optional arguments:

    parser.add_argument(
        "-CSVfile",
        help="Name of saved file. \
                Default = 'get_apps.csv'",
        type=str,
        default="get_apps.csv",
    )

    parser.add_argument(
        "-host",
        help="URL of the API gateway. \
                Default = 'https://gateway.wadmp.com'",
        type=str,
        default="https://gateway.wadmp.com",
    )

    parser.add_argument(
        "-username",
        help="Username. \
                Check the code for the default!",
        type=str,
        default="email address",
    )

    parser.add_argument(
        "-password",
        help="Password. \
                Check the code for the default!",
        type=str,
        default="password",
    )

    parser.add_argument(
        "-console_loglevel",
        help="Log verbosity level. The higher the level, the fewer messages that will be logged. \
                             Default = info",
        type=str,
        choices=["debug", "info", "warning", "error", "critical"],
        default="info",
    )

    parser.add_argument(
        "-file_loglevel",
        help="Log verbosity level. The higher the level, the fewer messages that will be logged. \
                             Default = info",
        type=str,
        choices=["debug", "info", "warning", "error", "critical"],
        default="info",
    )

    args = parser.parse_args()

    return args


def main(args):
    """Main function"""

    # A log message will only be emitted if the message level is greater than or equal to the configured level of the logger.
    LOG_LEVELS = {
        "critical": logging.CRITICAL,
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG,
    }

    console_loglevel = LOG_LEVELS[args.console_loglevel]
    file_loglevel = LOG_LEVELS[args.file_loglevel]

    script_name = os.path.splitext(os.path.basename(__file__))[0]
    configure_logging(script_name, console_loglevel, file_loglevel)

    global logger
    logger = logging.getLogger(script_name)

    global BASE_URL
    BASE_URL = args.host

    global SESSION
    SESSION = requests.Session()

    user_token = login(args.username, args.password)

    SESSION.headers.update({"Authorization": f"Bearer {user_token}"})

    if args.devices == "ALL":
        logger.info("Getting a list of ALL your devices ...")
        my_devices = get_devices(100)
        logger.info(f"You have {len(my_devices)} devices in total.\n")
    else:
        logger.info("Opening CSV file of devices ...")
        with open(args.devices, encoding="UTF-8", newline="") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            next(csvreader)  # Skip the first row
            my_devices = []
            for row in csvreader:
                logger.debug(row)
                alias, serial_number, order_code, mac, imei, device_type = row
                device = {
                    "alias": alias,
                    "serial_number": serial_number,
                    "order_code": order_code,
                    "mac_address": mac,
                    "imei": imei,
                    "device_type": {"description": device_type},
                }
                my_devices.append(device)
        logger.info(f"File contains {len(my_devices)} devices in total.\n")

    # The end goal is a Pandas dataframe, but appending to a dataframe in a loop is very inefficient.
    # Instead, we create a list of dictionaries, one dictionary per device.
    # When we convert the list to a dataframe later, the dictionary keys will automatically be used as the column names.
    data = []

    for device in my_devices:
        logger.info(f"Device {device['mac_address']}")

        apps = get_applications_in_device(device["mac_address"])
        if apps:
            logger.info(f"{len(apps)} applications found")

            for i, app in enumerate(apps):
                if app["has_failed"]:
                    logger.warning(
                        f"{device['mac_address']}: app {app['application_version']['application']['name']}, {app['application_version']['version']} failed to install - ignoring"
                    )
                    del apps[i]  # We ignore any apps that failed to install

            firmwares = []
            user_modules = []
            for i, app in enumerate(apps):
                if app["has_failed"]:
                    logger.warning(
                        f"{device['mac_address']}: app {app['application_version']['application']['name']}, {app['application_version']['version']} failed to install - ignoring"
                    )
                elif app["application_version"]["application"]["is_firmware"]:
                    firmwares.append(app)
                else:
                    user_modules.append(app)

            if firmwares:
                logger.info(
                    f"{len(firmwares)} firmwares, {len(user_modules)} User Modules"
                )
            else:
                logger.warning(
                    f"No firmware application found, {len(user_modules)} User Modules"
                )
        else:
            logger.error("No applications found!")
            continue

        device_info = {
            "Alias": device["alias"],
            "Serial No": device["serial_number"],
            "Order Code": device["order_code"],
            "MAC": device["mac_address"],
            "IMEI": device["imei"],
            "Type": device["device_type"]["description"],
        }

        for app in firmwares:
            # Note that we prefix each app name with "FW" so that we can group them later
            device_info[
                f"FW {app['application_version']['application']['name']}, {app['application_version']['version']}"
            ] = summarise_app(app)

        for app in user_modules:
            device_info[
                f"{app['application_version']['application']['name']}, {app['application_version']['version']}"
            ] = summarise_app(app)

        data.append(device_info)

    table = pd.DataFrame(data)

    # Re-order the columns to list all the Firmware apps first, before the User Modules
    columns = table.columns.tolist()
    new_columns = sort_columns(columns)
    table = table[new_columns]

    table.to_csv(args.CSVfile, index=False)
    logger.info(f"Saved to {args.CSVfile}.")


def summarise_app(app):
    """Return a string the summarises the important information about the app"""
    state = app["state"]
    if state != "Installed":
        state = state.upper()

    pin_status = "Pinned" if app["is_pinned"] else "NOT PINNED"

    known_status = "UNKNOWN" if app["application_version"]["is_unknown"] else "Known"

    return f"{state}, {pin_status}, {known_status}"


def sort_columns(old_list):
    """Re-order a list of strings.
    Specifically, we want to keep all the Firmware apps together, before the User Modules.

    The first 6 positions are fixed. For example:
         0   Alias                       Alias
         1   Serial No                   Serial No
         2   Order Code                  Order Code
         3   MAC                         MAC
         4   IMEI                        IMEI
         5   Type                        Type
         6   FW ICR-321x, 6.2.5          FW ICR-321x, 6.2.5
         7   wadmp_client, 2.0.5         FW ICR-321x, 6.2.3
         8   ipsec_tools, 1.0.1          wadmp_client, 2.0.5
         9   zebra, 1.7.0                ipsec_tools, 1.0.1
         10  bgp, 1.7.0                  zebra, 1.7.0
         11  nhrp, 1.1.0                 bgp, 1.7.0
         12  netflow, 1.0.0              nhrp, 1.1.0
         13  scepClient, 2.0.0           netflow, 1.0.0
         14  FW ICR-321x, 6.2.3          scepClient, 2.0.0
         15  pinger, 2.3.3               pinger, 2.3.3

    """
    order = []
    first_fw_found = None

    for i, name in enumerate(old_list):
        if name.startswith("FW "):
            if not first_fw_found:
                first_fw_found = True
                fw_index = i
                order.append(i)
            else:
                order.insert(fw_index + 1, i)
                fw_index += 1
        else:
            order.append(i)

    new_list = [old_list[i] for i in order]

    return new_list


class test_sort_columns(unittest.TestCase):
    """Invoke these tests from the command line as follows:
    $ python -m unittest get_apps.test_sort_columns
    """

    def test_0(self):
        input_list = [
            "Alias",
            "Serial No",
            "Order Code",
            "MAC",
            "IMEI",
            "Type",
            "FW ICR-321x, 6.2.5",
            "wadmp_client, 2.0.5",
            "ipsec_tools, 1.0.1",
            "zebra, 1.7.0",
            "bgp, 1.7.0",
            "nhrp, 1.1.0",
            "netflow, 1.0.0",
            "scepClient, 2.0.0",
            "FW ICR-321x, 6.2.3",
            "pinger, 2.3.3",
        ]
        output_list = sort_columns(input_list)
        expected_list = [
            "Alias",
            "Serial No",
            "Order Code",
            "MAC",
            "IMEI",
            "Type",
            "FW ICR-321x, 6.2.5",
            "FW ICR-321x, 6.2.3",
            "wadmp_client, 2.0.5",
            "ipsec_tools, 1.0.1",
            "zebra, 1.7.0",
            "bgp, 1.7.0",
            "nhrp, 1.1.0",
            "netflow, 1.0.0",
            "scepClient, 2.0.0",
            "pinger, 2.3.3",
        ]
        self.assertEqual(output_list, expected_list)

    def test_1(self):
        input_list = [
            "Alias",
            "Serial No",
            "Order Code",
            "MAC",
            "IMEI",
            "Type",
            "FW 0",
            "wadmp_client, 2.0.5",
            "FW 1",
            "zebra, 1.7.0",
            "FW 2",
            "nhrp, 1.1.0",
            "FW 3",
            "scepClient, 2.0.0",
            "FW 4",
            "pinger, 2.3.3",
        ]
        output_list = sort_columns(input_list)
        expected_list = [
            "Alias",
            "Serial No",
            "Order Code",
            "MAC",
            "IMEI",
            "Type",
            "FW 0",
            "FW 1",
            "FW 2",
            "FW 3",
            "FW 4",
            "wadmp_client, 2.0.5",
            "zebra, 1.7.0",
            "nhrp, 1.1.0",
            "scepClient, 2.0.0",
            "pinger, 2.3.3",
        ]
        self.assertEqual(output_list, expected_list)


def login(username, password):
    """Login to the system, and return a token"""
    url = f"{BASE_URL}/public/auth/connect/token"
    credentials = {
        "username": username,
        "password": password,
        "client_id": "python",
        "grant_type": "password",
    }
    logger.debug(
        f"Sending POST request to {url} with:\n" f"    credentials={credentials}"
    )
    response = SESSION.post(url, data=credentials)

    logger.debug(response.status_code)
    try:
        logger.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logger.debug(response.text)

    if response.status_code == requests.codes["ok"]:
        try:
            return response.json()["access_token"]
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
            return None
        except KeyError as err:
            logger.error(f"Didn't find what we expected in the JSON response!\n{err}")
            return None
    else:
        logger.error(f"Failed to login! {response.status_code}")
        try:
            logger.error(f"{response.json()['message']}")
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
        except KeyError as err:
            logger.error(response.json())
        sys.exit(1)


def get_devices(page_size):
    """Retrieves the list of your devices.
    Requests are paged, but this function automatically aggregates responses into one complete list.
    """
    page_number = 1
    total, devices = get_one_page_of_devices(page_number, page_size)

    while len(devices) < total:
        logger.debug(f"{len(devices)} out of {total} ...")
        page_number += 1
        total, page = get_one_page_of_devices(page_number, page_size)
        devices.extend(page)

    return devices


def get_one_page_of_devices(page_number, page_size):
    """Retrieves one page of the list of your devices."""
    url = f"{BASE_URL}/{BASE_PATH}/management/devices"

    # The only REQUIRED query parameters are page and pageSize
    logger.debug(
        f"Sending GET request to {url} with:\n"
        f"    page={page_number}\n"
        f"    pageSize={page_size}"
    )
    query = {"page": page_number, "pageSize": page_size}
    response = SESSION.get(url, params=query)

    logger.debug(response.status_code)
    try:
        logger.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logger.debug(response.text)

    try:
        total = response.json()["total_items"]
    except json.decoder.JSONDecodeError as err:
        logger.error(f"Problem decoding JSON!\n{err}")
        return None, None
    except KeyError as err:
        logger.error(f"Didn't find what we expected in the JSON response!\n{err}")
        return None, None

    if response.status_code == requests.codes["ok"]:
        try:
            return total, response.json()["data"]
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
            return total, None
        except KeyError as err:
            logger.error(f"Didn't find what we expected in the JSON response!\n{err}")
            return total, None
    else:
        logger.error(f"Failed to retrieve page {page_number}! {response.status_code}")
        try:
            logger.error(f"{response.json()['message']}")
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
        except KeyError as err:
            logger.error(response.json())
        return None, None


def get_applications_in_device(mac):
    """Gets apps installed in a device."""
    url = f"{BASE_URL}/{BASE_PATH}/management/devices/{mac}/apps"
    logger.debug(f"Sending GET request to {url}")
    response = SESSION.get(url)

    logger.debug(response.status_code)
    try:
        logger.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logger.debug(response.text)

    if response.status_code == requests.codes["ok"]:
        try:
            return response.json()["data"]
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
            return None
        except KeyError as err:
            logger.error(f"Didn't find what we expected in the JSON response!\n{err}")
            return None
    else:
        logger.error(
            f"Failed to retrieve the list of Applications! {response.status_code}"
        )
        try:
            logger.error(f"{response.json()['message']}")
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
        except KeyError as err:
            logger.error(response.json())
        return None


def search(array, key, value):
    """Generic function to find a particular dictionary in a list of dictionaries,
    based on one key:value pair in each dict.
    """
    for item in array:
        if item[key] == value:
            return item
    return None


class UTCFormatter(logging.Formatter):
    """Allows us to configure the logging timestamps to use UTC.

    We could have used an external JSON or YAML file to hold the configuration for logging.config.dictConfig(),
    but there is no way to configure timestamps via a file!
    """

    converter = time.gmtime


def configure_logging(name, console_loglevel, file_loglevel):
    """We use a dictionary to configure the Python logging module."""

    LOG_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "loggers": {name: {"level": "DEBUG", "handlers": ["console", "file"]}},
        "handlers": {
            "console": {
                "level": console_loglevel,
                "class": "logging.StreamHandler",
                "formatter": "console_format",
            },
            "file": {
                "level": file_loglevel,
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "file_format",
                "filename": f"{name}.log",
                "mode": "w",
            },
        },
        "formatters": {
            "console_format": {"format": "%(name)s - %(levelname)s - %(message)s"},
            "file_format": {
                "()": UTCFormatter,
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
    }

    logging.config.dictConfig(LOG_CONFIG)


if __name__ == "__main__":
    args = parse_args()
    main(args)
