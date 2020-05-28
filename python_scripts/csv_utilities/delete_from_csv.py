#!/usr/bin/env python

"""
Python script which uses the WADMP public API to delete a number of devices.
Note that you can only delete a device if:
* The device is not claimed by a company.
  Use the "release_from_csv.py" script.
* The device has never connected to (aka "registered" with) the Management Server.
  A delete request will be rejected with the message "You cannot delete a device that has registered to a server."
  The only option in this case is to ask a System Adinistrator to delete the device manually in the database.

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
    parser = argparse.ArgumentParser(description="Delete devices from WA/DMP")

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

            delete_device(mac)


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


def delete_device(mac_address):
    """Delete a device.
    """
    url = f"{BASE_URL}/{BASE_PATH}/identity/devices/{mac_address}"
    logger.debug(f"\nSending DELETE request to {url}\n")
    response = SESSION.delete(url)

    logger.debug(response.status_code)
    try:
        logger.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logger.debug(response.text)

    if response.status_code == requests.codes["ok"]:
        try:
            return response.json()["success"]
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
            return None
        except KeyError as err:
            logger.error(f"Didn't find what we expected in the JSON response!\n{err}")
            return None
    else:
        logger.error(f"Failed to delete device! {response.status_code}")
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
