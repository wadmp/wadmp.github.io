#!/usr/bin/env python

"""
Python script which uses the WADMP public API to create a number of devices.

Ben Kinsella, January 2020
Copyright Advantech B+B SmartWorx, 2020

Version 0.4
Last tested on Ubuntu 18.04 with Python 3.6, and on Windows 10 with Python 3.7
"""

# Standard library
import argparse
import os.path
import csv
import json
import sys
import logging
import logging.config
import time

# pip
import requests


BASE_PATH = "api"


def parse_args():
    """Parse command-line arguments
    """
    parser = argparse.ArgumentParser(description="Create devices on WA/DMP")

    # Positional arguments:

    parser.add_argument("CSVfile", help="Path to CSV file.", type=str)

    # Optional arguments:

    parser.add_argument(
        "-host",
        help="URL of the WADMP server's API gateway. \
                                Check the code for the default!",
        type=str,
        default="https://gateway.wadmp.com",
    )

    parser.add_argument(
        "-username",
        help="Username. \
                                Check the code for the default!",
        type=str,
        default="email",
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

    return parser.parse_args()


def main(args):
    """ Main function
    """

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

    # Create a list of all device types on the system
    all_types = []
    families = get_device_families()
    for family in families:
        family_id = family["id"]
        types = get_device_types(family_id)
        all_types.extend(types)

    with open(args.CSVfile, encoding="UTF-8", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)  # Skip the first row
        for row in csvreader:
            logger.debug(row)

            alias, serial_number, order_code, mac, imei, requested_type = row
            logger.info(f"Alias {alias}")
            logger.info(f"Serial Number {serial_number}")
            logger.info(f"Order Code {order_code}")
            logger.info(f"MAC {mac}")
            logger.info(f"IMEI {imei}")
            logger.info(f"Type {requested_type}\n")

            type_id = None
            for existing_type in all_types:
                if existing_type["name"] == requested_type:
                    type_id = existing_type["type_id"]
                    break

            if type_id:
                logger.debug(f"Device type {requested_type} has ID {type_id}")
            else:
                logger.error(f"Device type {requested_type} not found!")
                continue

            device = {
                "alias": alias,
                "serial_number": serial_number,
                "order_code": order_code,
                "mac_address": mac,
                "device_type_id": type_id,
                "imei": imei,
            }
            create_device(device)


def login(username, password):
    """Login to the system, and return a token
    """
    url = f"{BASE_URL}/public/auth/connect/token"
    credentials = {
        "username": username,
        "password": password,
        "client_id": "python",
        "grant_type": "password",
    }
    logger.debug(
        f"\nSending POST request to {url} with:\n" f"    credentials={credentials}"
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
        sys.exit(1)


def get_device_families(name=None):
    """Retrieves the list of families in the system
    """
    url = f"{BASE_URL}/{BASE_PATH}/identity/device-families"
    logger.debug(f"\nSending GET request to {url} with:\n" f"    name={name}\n")
    query = {"name": name}
    response = SESSION.get(url, params=query)

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
        logger.error(f"Failed to retrieve the list of Families! {response.status_code}")
        return None


def get_device_types(family_id=None):
    """Retrieves the list of device types belonging to a particular family
    """
    url = f"{BASE_URL}/{BASE_PATH}/identity/device-families/{family_id}/device-types"
    logger.debug(f"\nSending GET request to {url}\n")
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
        logger.error(f"Failed to retrieve the list of Types! {response.status_code}")
        return None


def create_device(model=None):
    """Create a device in the system.
    """
    url = f"{BASE_URL}/{BASE_PATH}/identity/devices"
    logger.debug(f"\nSending POST request to {url} with:\n" f"    model={model}\n")
    response = SESSION.post(url, json=model)

    logger.debug(response.status_code)
    try:
        logger.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logger.debug(response.text)

    if response.status_code == requests.codes["ok"]:
        try:
            return response.json()["data"]["id"]
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
            return None
        except KeyError as err:
            logger.error(f"Didn't find what we expected in the JSON response!\n{err}")
            return None
    else:
        logger.error(f"Failed to create device! {response.status_code}")
        return None


class UTCFormatter(logging.Formatter):
    """Allows us to configure the logging timestamps to use UTC.

       We could have used an external JSON or YAML file to hold the configuration for logging.config.dictConfig(),
       but there is no way to configure timestamps via a file!
    """

    converter = time.gmtime


def configure_logging(name, console_loglevel, file_loglevel):
    """We use a dictionary to configure the Python logging module.
    """

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
