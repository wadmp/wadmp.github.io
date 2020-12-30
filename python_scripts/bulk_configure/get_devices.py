#! /usr/bin/env python

"""
This script uses the public API to create a CSV file with a list of your devices.
Arguments to the script can be used to filter the devices.

Ben Kinsella, May 2020
Copyright Advantech B+B SmartWorx, 2020

Version 0.4

Last tested on Ubuntu 18.04 with Python 3.6, and on Windows 10 with Python 3.7
"""

# Standard library
import argparse
import os.path
import json
import sys
import logging
import logging.config
import time
import csv

# pip
import requests


BASE_PATH = "api"


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Get a list of devices, save in CSV file."
    )

    # Positional arguments:
    # None

    # Optional arguments:

    parser.add_argument(
        "-CSVfile",
        help="Name of saved file. \
                Default = 'get_devices.csv'",
        type=str,
        default="get_devices.csv",
    )

    parser.add_argument(
        "-mac_or_serial",
        help="MAC Address or Serial Number of an individual device",
        type=str,
    )

    parser.add_argument(
        "-alias",
        help="Alias (name) of an individual device",
        type=str,
    )

    parser.add_argument(
        "-companies",
        help="Names of Companies to which devices belong",
        nargs="*",
        type=str,
    )

    parser.add_argument(
        "-groups",
        help="Names of Groups to which devices belong",
        nargs="*",
        type=str,
    )

    parser.add_argument(
        "-tags",
        help="Names of Tags which have been applied to devices",
        nargs="*",
        type=str,
    )

    parser.add_argument(
        "-types",
        help="List of Device Types",
        nargs="*",
        type=str,
    )

    parser.add_argument(
        "-isOnline",
        help="isOnline?",
        choices=["yes", "no", "both"],
        type=str,
        default="both",
    )

    parser.add_argument(
        "-inSync",
        help="inSync?",
        choices=["yes", "no", "both"],
        type=str,
        default="both",
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

    companies = translate_company_names_to_ids(args.companies)
    # If company names were specified, but NO company IDs were found, stop.
    if args.companies and not companies:
        sys.exit(1)

    groups = translate_group_names_to_ids(args.groups)
    # If group names were specified, but NO group IDs were found, stop.
    if args.groups and not groups:
        sys.exit(1)

    tags = translate_tag_names_to_ids(args.tags)
    # If tag names were specified, but NO tag IDs were found, stop.
    if args.tags and not tags:
        sys.exit(1)

    types = translate_type_names_to_ids(args.types)
    # If type names were specified, but NO type IDs were found, stop.
    if args.types and not types:
        sys.exit(1)

    logger.info(f"Getting the list of matching devices ...")
    my_devices = get_devices(
        100,
        args.mac_or_serial,
        args.alias,
        companies,
        groups,
        tags,
        types,
        args.isOnline,
        args.inSync,
    )
    logger.info(f"Found {len(my_devices)} devices in total.\n")

    with open(args.CSVfile, "w", encoding="UTF-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(["Alias", "Serial No", "Order Code", "MAC", "IMEI", "Type"])
        for device in my_devices:
            csvwriter.writerow(
                [
                    device["alias"],
                    device["serial_number"],
                    device["order_code"],
                    device["mac_address"],
                    device["imei"],
                    device["device_type"]["name"],
                ]
            )

    logger.info(f"Saved to {args.CSVfile}.")


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


def translate_company_names_to_ids(company_names):
    """"""
    if company_names:
        logger.debug("Finding company IDs ...")
        all_companies = get_companies()

        company_ids = []
        for company_name in company_names:
            company_id = lookup_list(company_name, all_companies)
            if company_id:
                logger.debug(f"{company_name} = {company_id}")
                company_ids.append(company_id)
            else:
                logger.warning(f"{company_name} not found!")
        return company_ids

    else:
        return []


def translate_group_names_to_ids(group_names):
    """"""
    if group_names:
        logger.debug("Finding group IDs ...")
        all_groups = get_groups()

        group_ids = []
        for group_name in group_names:
            group_id = lookup_list(group_name, all_groups)
            if group_id:
                logger.debug(f"{group_name} = {group_id}")
                group_ids.append(group_id)
            else:
                logger.warning(f"{group_name} not found!")
        return group_ids

    else:
        return []


def translate_tag_names_to_ids(tag_names):
    """"""
    if tag_names:
        logger.debug("Finding tag IDs ...")
        all_tags = get_tags()

        tag_ids = []
        for tag_name in tag_names:
            tag_id = lookup_list(tag_name, all_tags)
            if tag_id:
                logger.debug(f"{tag_name} = {tag_id}")
                tag_ids.append(tag_id)
            else:
                logger.warning(f"{tag_name} not found!")
        return tag_ids

    else:
        return []


def translate_type_names_to_ids(type_names):
    """"""
    if type_names:
        logger.debug("Finding type IDs ...")
        all_types = get_types()

        type_ids = []
        for type_name in type_names:
            type_id = lookup_list(type_name, all_types)
            if type_id:
                logger.debug(f"{type_name} = {type_id}")
                type_ids.append(type_id)
            else:
                logger.warning(f"{type_name} not found!")
        return type_ids

    else:
        return []


def get_companies(name=None):
    """Retrieves the list of companies in the system"""
    url = f"{BASE_URL}/{BASE_PATH}/companies"
    logger.debug(f"Sending GET request to {url} with:\n" f"    name={name}\n")
    query = {"name": name}
    response = SESSION.get(url, params=query)

    logger.info(response.status_code)
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
            f"Failed to retrieve the list of Companies! {response.status_code}"
        )
        try:
            logger.error(f"{response.json()['message']}")
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
        except KeyError as err:
            logger.error(response.json())
        return None


def get_groups(name=None):
    """Retrieves the list of device groups in the system"""
    url = f"{BASE_URL}/{BASE_PATH}/management/device-groups"
    logger.debug(f"Sending GET request to {url} with:\n" f"    name={name}\n")
    query = {"name": name}
    response = SESSION.get(url, params=query)

    logger.info(response.status_code)
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
            f"Failed to retrieve the list of Device Groups! {response.status_code}"
        )
        try:
            logger.error(f"{response.json()['message']}")
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
        except KeyError as err:
            logger.error(response.json())
        return None


def get_tags(name=None):
    """Retrieves the list of device tags in the system"""
    url = f"{BASE_URL}/{BASE_PATH}/management/device-tags"
    logger.debug(f"Sending GET request to {url} with:\n" f"    name={name}\n")
    query = {"name": name}
    response = SESSION.get(url, params=query)

    logger.info(response.status_code)
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
            f"Failed to retrieve the list of Device Tags! {response.status_code}"
        )
        try:
            logger.error(f"{response.json()['message']}")
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
        except KeyError as err:
            logger.error(response.json())
        return None


def get_types(name=None):
    """Retrieves the list of device types in the system.

    Note that we actually use the "GET device-families" endpoint, as this returns a complete list in one request.
    """
    all_types = []
    all_families = get_families(name=None, includeTypes=True)
    for family in all_families:
        all_types.extend(family["types"])

    return all_types


def get_families(name=None, includeTypes=True):
    """Retrieves the list of device families in the system."""
    url = f"{BASE_URL}/{BASE_PATH}/identity/device-families"
    logger.debug(
        f"Sending GET request to {url} with:\n"
        f"    name={name}\n"
        f"    includeTypes={includeTypes}"
    )
    query = {"name": name, "includeTypes": includeTypes}
    response = SESSION.get(url, params=query)

    logger.info(response.status_code)
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
            f"Failed to retrieve the list of Device Families! {response.status_code}"
        )
        try:
            logger.error(f"{response.json()['message']}")
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
        except KeyError as err:
            logger.error(response.json())
        return None


def lookup_list(name, list_of_objects):
    """Use 'name' as an index into list, and return 'id'"""
    for obj in list_of_objects:
        if obj["name"] == name:
            return obj["id"]

    return None


def get_devices(
    page_size,
    mac_or_serial="",
    alias="",
    companies=[],
    groups=[],
    tags=[],
    types=[],
    isOnline="both",
    inSync="both",
):
    """Retrieves the list of your devices.
    Requests are paged, but this function automatically aggregates responses into one complete list.
    """
    page_number = 1
    total, devices = get_one_page_of_devices(
        page_number,
        page_size,
        mac_or_serial,
        alias,
        companies,
        groups,
        tags,
        types,
        isOnline,
        inSync,
    )

    while len(devices) < total:
        logger.debug(f"{len(devices)} out of {total} ...")
        page_number += 1
        total, page = get_one_page_of_devices(
            page_number,
            page_size,
            mac_or_serial,
            alias,
            companies,
            groups,
            tags,
            types,
            isOnline,
            inSync,
        )
        devices.extend(page)

    return devices


def get_one_page_of_devices(
    page_number,
    page_size,
    mac_or_serial="",
    alias="",
    companies=[],
    groups=[],
    tags=[],
    types=[],
    isOnline="both",
    inSync="both",
):
    """Retrieves one page of the list of your devices."""
    url = f"{BASE_URL}/{BASE_PATH}/management/devices"

    # The only REQUIRED query parameters are page and pageSize
    query = {"page": page_number, "pageSize": page_size}
    if mac_or_serial:
        query["search"] = mac_or_serial
    if alias:
        query["name"] = alias
    if companies:
        query["companies"] = companies
    if groups:
        query["groups"] = groups
    if tags:
        query["tags"] = tags
    if types:
        query["types"] = types
    if isOnline != "both":
        if isOnline == "yes":
            query["isOnline"] = True
        if isOnline == "no":
            query["isOnline"] = False
    if inSync != "both":
        if inSync == "yes":
            query["inSync"] = True
        if inSync == "no":
            query["inSync"] = False

    logger.debug(f"Sending GET request to {url} with:\n{json.dumps(query, indent=4)}")
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
