#! /usr/bin/env python

"""
This script uses the public API to read the latest settings (both Reported and Desired),
for one or multiple sections,
from multiple devices.

Ben Kinsella, January 2020
Copyright Advantech B+B SmartWorx, 2020

Version 0.6

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

# pip
import requests


BASE_PATH = "api"


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Read settings for one section from all devices"
    )

    # Positional arguments:

    parser.add_argument("devices", help="CSV file of devices", type=str, default="ALL")

    parser.add_argument("section", help="Section name", type=str, default="snmp")

    # Optional arguments:

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
                device = {"mac_address": mac}
                my_devices.append(device)
        logger.info(f"File contains {len(my_devices)} devices in total.\n")

    device_count = 0
    device_with_specified_section_count = 0
    in_sync_count = 0
    desired_count = 0
    reported_count = 0

    for device in my_devices:
        device_count += 1
        logger.info(f"Device {device['mac_address']}")

        fw_app_id, fw_app_version_id = find_fw_ids(device["mac_address"])

        if fw_app_id and fw_app_version_id:
            logger.info(
                f"Firmware application ID {fw_app_id}, application version ID {fw_app_version_id}"
            )

            try:
                os.mkdir("get_settings")
                logger.debug("Created the 'get_settings' directory.")
            except FileExistsError:
                logger.debug("The 'get_settings' directory already exists")

            # Windows doesn't allow colons (':') in filenames
            device_folder = os.path.join(
                "get_settings", device["mac_address"].replace(":", "-")
            )
            try:
                os.mkdir(device_folder)
            except FileExistsError:
                logger.error(f"The sub-directory {device_folder} already exists!")
                logger.error(
                    "Please delete or move the contents of the 'get_settings' folder before trying again"
                )
                sys.exit(1)

            all_sections = get_sections(fw_app_id, fw_app_version_id)
            if not all_sections:
                logger.error("No application sections found!")
                continue

            if args.section == "ALL":
                for section in all_sections:
                    logger.info(f"Section {section['name']}")

                    settings = get_section_settings(
                        device["mac_address"], fw_app_version_id, section["id"]
                    )
                    logger.info(json.dumps(settings, indent=4, sort_keys=True) + "\n")

                    if settings:
                        desired_file = os.path.join(
                            device_folder, f"{section['name']}_desired.ini"
                        )
                        reported_file = os.path.join(
                            device_folder, f"{section['name']}_reported.ini"
                        )
                        if settings[
                            "desired_configuration"
                        ]:  # Can't write 'null' or 'None':
                            with open(desired_file, "x") as f:
                                f.write(settings["desired_configuration"])
                        if settings[
                            "reported_configuration"
                        ]:  # Can't write 'null' or 'None':
                            with open(reported_file, "x") as f:
                                f.write(settings["reported_configuration"])

            else:  # Only one section was specified on the command line
                section = search(all_sections, "name", args.section)
                if section:
                    device_with_specified_section_count += 1
                    settings = get_section_settings(
                        device["mac_address"], fw_app_version_id, section["id"]
                    )

                    if settings:
                        logger.info(
                            json.dumps(settings, indent=4, sort_keys=True) + "\n"
                        )

                        desired_file = os.path.join(
                            device_folder, f"{section['name']}_desired.ini"
                        )
                        reported_file = os.path.join(
                            device_folder, f"{section['name']}_reported.ini"
                        )
                        with open(desired_file, "x") as f:
                            if settings[
                                "desired_configuration"
                            ]:  # Can't write 'null' or 'None'
                                f.write(settings["desired_configuration"])
                        with open(reported_file, "x") as f:
                            if settings[
                                "reported_configuration"
                            ]:  # Can't write 'null' or 'None'
                                f.write(settings["reported_configuration"])

                        if settings["in_sync"]:
                            in_sync_count += 1
                        if settings["desired_configuration"]:
                            desired_count += 1
                        if settings["reported_configuration"]:
                            reported_count += 1
                else:
                    logger.warning(
                        f"This device does not have a section called {args.section}"
                    )

        else:
            logger.error("No firmware application found!")

    if args.section != "ALL":
        logger.info(
            f"{device_count} devices in total, of which {device_with_specified_section_count} have the {args.section} section"
        )
        logger.info(
            f"Of those {device_with_specified_section_count}:\n"
            f"    {reported_count} have a reported state,\n"
            f"    {desired_count} have a desired state,\n"
            f"    {in_sync_count} are in sync.\n"
        )


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


def get_sections(app_id, version_id):
    """Gets an application version details by its id.
    Returns the array of sections associated with that version.
    """
    url = f"{BASE_URL}/{BASE_PATH}/applications/{app_id}/versions/{version_id}"
    logger.debug(f"Sending GET request to {url}")
    response = SESSION.get(url)

    logger.debug(response.status_code)
    try:
        logger.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logger.debug(response.text)

    if response.status_code == requests.codes["ok"]:
        try:
            return response.json()["data"]["sections"]
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
            return None
        except KeyError as err:
            logger.error(f"Didn't find what we expected in the JSON response!\n{err}")
            return None
    else:
        logger.error(f"Failed to get the version details! {response.status_code}")
        try:
            logger.error(f"{response.json()['message']}")
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
        except KeyError as err:
            logger.error(response.json())
        return None


def find_fw_ids(mac):
    """For the given device, find the app ID and the app version ID for the firmware app."""
    fw_app_id = None
    fw_app_version_id = None

    apps = get_applications_in_device(mac)
    if apps:
        for app in apps:
            if app["application_version"]["application"]["is_firmware"]:
                fw_app_id = app["application_version"]["application"]["id"]
                fw_app_version_id = app["application_version"]["id"]
                break

    return fw_app_id, fw_app_version_id


def search(array, key, value):
    """Generic function to find a particular dictionary in a list of dictionaries,
    based on one key:value pair in each dict.
    """
    for item in array:
        if item[key] == value:
            return item
    return None


def get_section_settings(mac, version_id, section_id):
    """Gets the desired and reported settings of a specific section of an app in a device."""
    url = f"{BASE_URL}/{BASE_PATH}/management/devices/{mac}/apps/{version_id}/settings/{section_id}"
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
        logger.error(f"Failed to get the section settings! {response.status_code}")
        try:
            logger.error(f"{response.json()['message']}")
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
        except KeyError as err:
            logger.error(response.json())
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
