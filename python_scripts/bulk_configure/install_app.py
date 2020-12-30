#! /usr/bin/env python

"""
This script uses the public API to install or upgrade an application, on multiple devices.
An "application" may be Firmware or a User Module.

Ben Kinsella, June 2020
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
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description="Install an app. on multiple devices")

    # Positional arguments:

    parser.add_argument("devices", help="CSV file of devices", type=str, default="ALL")

    parser.add_argument("appName", help="App. name", type=str, default="wadmp_client")

    parser.add_argument(
        "appVersion", help="App. version number", type=str, default="2.0.5"
    )

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

    # If --replace_pending_installs is NOT given on the command line, it defaults to False.
    parser.add_argument(
        "--replace_pending_installs",
        help="If a device already has an upgrade-downgrade pending for this app, replace it",
        action="store_true",
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

    # Check that the app name and version provided are correct

    app_id = None
    app_version_id = None
    matching_apps = get_applications(args.appName)

    if len(matching_apps) == 0:
        logger.error(f"No app found with name '{args.appName}'")
        sys.exit(1)

    elif len(matching_apps) == 1:
        if matching_apps[0]["is_unknown"] is False:
            app_id = matching_apps[0]["id"]
            logger.info(f"App name {args.appName} has app ID {app_id}")
            if matching_apps[0]["is_firmware"] is True:
                logger.info("This application is FIRMWARE")

            available_versions = matching_apps[0]["versions"]
            for available_version in available_versions:
                if available_version["version"] == args.appVersion:
                    app_version_id = available_version["id"]
                    break
            if app_version_id:
                logger.info(
                    f"{args.appName} version {args.appVersion} has app version ID {app_version_id}"
                )
            else:
                logger.error(
                    f"No match found for {args.appVersion}. Please double-check!"
                )
                sys.exit(1)

    else:
        logger.warning(
            f"{len(matching_apps)} apps found with a name matching '{args.appName}'! Proceeding with caution ..."
        )

        for matching_app in matching_apps:
            logger.info(f"Considering {matching_app['name']} ...")
            if matching_app["name"] == args.appName:
                logger.info(f"{args.appName} is an EXACT match")
                app_id = matching_app["id"]
                logger.info(f"App name {args.appName} has app ID {app_id}")
                if matching_app["is_firmware"] is True:
                    logger.info("This application is FIRMWARE")

                available_versions = matching_app["versions"]
                for available_version in available_versions:
                    if available_version["version"] == args.appVersion:
                        app_version_id = available_version["id"]
                        break
                if app_version_id:
                    logger.info(
                        f"{args.appName} version {args.appVersion} has app version ID {app_version_id}"
                    )

                break
        if app_id:
            if app_version_id:
                logger.info(
                    f"Proceeding with app ID {app_id} and app version ID {app_version_id}"
                )
            else:
                logger.error(
                    f"No match found for {args.appVersion}. Please double-check!"
                )
                sys.exit(1)
        else:
            logger.error(
                f"No exact match found for {args.appName}. Please double-check the spelling, upper/lower-case, etc."
            )
            sys.exit(1)

    # Get the list of devices

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
    installed_device_count = 0

    for device in my_devices:
        device_count += 1
        logger.info(f"Device {device['mac_address']}")

        result, message = install_app(device["mac_address"], app_version_id)
        if result == 200:
            installed_device_count += 1
        elif result == 400:
            if message.startswith("There is already an upgrade/downgrade pending"):
                # Each device can only have 2 versions of an app: one installed and one pending
                if args.replace_pending_installs:
                    logger.debug("Attempting to remove the pending installation ...")
                    pending_app_version = None

                    apps = get_applications_in_device(device["mac_address"])
                    for app in apps:
                        if app["application_version"]["application"]["id"] == app_id:
                            if app["state"] == "Initial":
                                pending_app_version_id = app["application_version"][
                                    "id"
                                ]
                                pending_app_version = app["application_version"][
                                    "version"
                                ]
                                break

                    if pending_app_version:
                        logger.info(
                            f"   Removing pending installation {pending_app_version}"
                        )
                        remove_result, remove_message = remove_app(
                            device["mac_address"], pending_app_version_id
                        )
                        if remove_result == 200:
                            # Try to install again
                            result, message = install_app(
                                device["mac_address"], app_version_id
                            )
                            if result == 200:
                                installed_device_count += 1
                    else:
                        logger.error(
                            f"   Failed to find a pending installation of {args.appName} on {device['mac_address']}!"
                        )

    logger.info(
        f"{device_count} devices in total, and we installed {args.appName} version {args.appVersion} on {installed_device_count}."
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


def get_applications(name=None, device_type_ids=[]):
    """Retrieves the list of applications available to install on devices"""
    url = f"{BASE_URL}/{BASE_PATH}/applications"
    logger.debug(
        f"\nSending GET request to {url} with:\n"
        f"    name={name}\n"
        f"    deviceTypeIds={device_type_ids}\n"
    )
    query = {"name": name, "deviceTypeIds": device_type_ids}
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


def get_application_versions(app_id=None, device_type_ids=[]):
    """Retrieves the list of applications available to install on devices"""
    url = f"{BASE_URL}/{BASE_PATH}/applications/{app_id}/versions"
    logger.debug(
        f"\nSending GET request to {url} with:\n"
        f"    deviceTypeIds={device_type_ids}\n"
    )
    query = {"deviceTypeIds": device_type_ids}
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
        logger.error(
            f"Failed to retrieve the list of Application Versions! {response.status_code}"
        )
        try:
            logger.error(f"{response.json()['message']}")
        except json.decoder.JSONDecodeError as err:
            logger.error(f"Problem decoding JSON!\n{err}")
        except KeyError as err:
            logger.error(response.json())
        return None


def install_app(mac, app_version_id):
    """Install an app to a device.

    This request will fail if the device type and app version are incompatible. Example:
        {
            "success": false,
            "message": "Application 'gps v1.5.2' does not support device type 'LR77-v2'."
        }
    """
    url = f"{BASE_URL}/{BASE_PATH}/management/devices/{mac}/apps/{app_version_id}"
    logger.debug(f"Sending POST request to {url}\n")
    response = SESSION.post(url)

    logger.debug(response.status_code)
    try:
        logger.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logger.debug(response.text)

    try:
        message = response.json()["message"]
    except json.decoder.JSONDecodeError as err:
        message = f"Problem decoding JSON!\n{err}"
    except KeyError as err:
        message = response.json()

    if response.status_code != requests.codes["ok"]:
        logger.error(f"Failed to install app! {response.status_code}")
        logger.error(message)

    return int(response.status_code), message


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


def remove_app(mac, app_version_id):
    """Uninstall an app from a device."""
    url = f"{BASE_URL}/{BASE_PATH}/management/devices/{mac}/apps/{app_version_id}"
    logger.debug(f"Sending DELETE request to {url}\n")
    response = SESSION.delete(url)

    logger.debug(response.status_code)
    try:
        logger.debug(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        logger.debug(response.text)

    try:
        message = response.json()["message"]
    except json.decoder.JSONDecodeError as err:
        message = f"Problem decoding JSON!\n{err}"
    except KeyError as err:
        message = response.json()

    if response.status_code != requests.codes["ok"]:
        logger.error(f"Failed to remove app! {response.status_code}")
        logger.error(message)

    return int(response.status_code), message


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
