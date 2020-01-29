#! /usr/bin/env python

"""
This script is intended to upload the User Module-related content as defined by a JSON "manifest" file,
using the public API.

Specifically, it creates Applications, Versions, and Sections,
and it uploads the binary User Module files.


WARNING!
Before running this script, you may want to manually delete any old Applications and Versions.


PREPARATION:
* Create a new Python 3 virtual environment and install the dependencies:
  $ pip install -r requirements3.6.txt

* Confirm that the username (specified on the command line) has the necessary permissions on WA/DMP.

* Prepare your manifest file. See "my_manifest.json", etc. for examples.


USAGE:
(env3.6) bkinsella@ben-ubuntu1804:/opt/projects/device-models/scripts$ ./deploy_user_modules.py -h
usage: deploy_user_modules.py [-h] [-url URL] [-manifest MANIFEST]
                              [-username USERNAME] [-password PASSWORD]

Upload Applications, Versions, Sections, and binary User Module files

optional arguments:
  -h, --help          show this help message and exit
  -url URL            URL of the API gateway. Default = 'https://gateway.dev.wadmp.com'
  -manifest MANIFEST  JSON manifest file
  -username USERNAME  Username
  -password PASSWORD  Password


EXAMPLE:
(env3.6) bkinsella@ben-ubuntu1804:/opt/projects/device-models/scripts$ ./deploy_user_modules.py -url https://gateway.dev.wadmp.com -manifest dev_user_modules.json -username bkinsella@advantech-bb.com -password password

Last tested on Ubuntu 18.04 with Python 3.6
"""

import argparse
import requests
import json
import os
import sys
from collections import OrderedDict


BASE_PATH = 'api'


def parse_args():
    """Parse command-line arguments
    """
    parser = argparse.ArgumentParser(description="Upload Applications, Versions, Sections, and binary User Module files")

    # Positional arguments:
    # None

    # Optional arguments:

    parser.add_argument("-url",
                        help="URL of the API gateway. \
                                Default = 'https://gateway.staging.wadmp.com'",
                        type=str,
                        default='https://gateway.staging.wadmp.com')

    parser.add_argument("-manifest",
                        help="JSON manifest file",
                        type=str)

    parser.add_argument("-username",
                        help="Username",
                        type=str,
                        default='email')

    parser.add_argument("-password",
                        help="Password",
                        type=str,
                        default='password')

    args = parser.parse_args()

    return args


def main(args):
    """Main function
    """
    global BASE_URL
    global USER_TOKEN

    BASE_URL = args.url
    USER_TOKEN = login(args.username, args.password)

    with open(args.manifest) as f:
        manifest = json.load(f)

    apps = get_applications()
    firmwares = [app for app in apps if app['is_firmware']==True]
    user_modules = [app for app in apps if app['is_firmware']==False]
    print(f"{len(apps)} applications found: {len(firmwares)} firmware, {len(user_modules)} user modules")

    for _, um_object in manifest.items():
        um_name = um_object['model']['name']

        existing_app = search(user_modules, 'name', um_name)
        if existing_app:
            app_id = existing_app['id']
            print(f"\nApplication {um_name} already exists with app_id {app_id}.")
            if existing_app['is_unknown']:
                print("BUT this app is 'unknown', so we make it known before proceeding ...")
                # The model for update_application is the same as for create_application,
                # except that we need to add an 'id' field:
                um_model = um_object['model']
                um_model['id'] = app_id
                update_application(app_id, um_model)
        else:
            um_model = um_object['model']
            app_id = create_application(um_model)

        if app_id:
            versions = get_application_versions(app_id)

            for version_name, version_value in um_object['versions'].items():

                existing_version = search(versions, 'version', version_name)

                if existing_version:
                    version_id = existing_version['id']
                    print(f"\nVersion {version_name} already exists with version_id {version_id}.")
                    if existing_version['is_unknown']:
                        print("BUT this version is 'unknown', so we make it known before proceeding ...")
                        # The model for update_application_version is the same as for create_application_version,
                        # except that we need to add a 'version_id' field:
                        version_model = {'application_id': app_id, 'version_id': version_id, 'version': version_name}
                        update_application_version(app_id, version_id, version_model)
                else:
                    version_model = {'application_id': app_id, 'version': version_name}
                    version_id = create_application_version(app_id, version_model)

                if version_id:

                    if 'model_location' in version_value:
                        dirs = os.listdir(version_value['model_location'])
                        loc = version_value['model_location']
                        dirs = os.listdir(loc)
                        dirs.sort()

                        for dirname in dirs:
                            section = prepare_section(os.path.join(loc, dirname), version_id)
                            create_application_sections(app_id, version_id, [section])

                    if 'binaries' in version_value:
                        for binary in version_value['binaries']:

                            if 'binary_location' in binary:
                                file_id = upload_file(binary['binary_location'], version_name)
                            
                                if file_id:
                                    if 'device_families' in binary:

                                        types = []

                                        for family in binary['device_families']:
                                            if '*' in family:
                                                families = get_device_families(family.replace('*', ''))
                                                for family in families:
                                                    types += get_device_types(family['id'])
                                            else:
                                                family = get_device_families(family)
                                                types += get_device_types(family['id'])

                                        type_ids = [t['type_id'] for t in types]
                                        associate_file_and_device_types_with_version(app_id, version_id, file_id, type_ids)


def login(username, password):
    """Login to the system, and return a token
    """
    url = f"{BASE_URL}/public/auth/connect/token"
    credentials = {'username': args.username, 'password': args.password, 'client_id': 'python', 'grant_type': 'password'}
    print(f"\nSending POST request to {url} with:\n"
          f"    credentials={credentials}")
    response = requests.post(url, data=credentials)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()["access_token"]
    else:
        print("Failed to login!")
        sys.exit(1)	


def get_device_families(name=None):
    """Retrieves the list of families in the system
    """
    url = f"{BASE_URL}/{BASE_PATH}/identity/device-families"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending GET request to {url} with:\n"
          f"    header={header}\n"
          f"    name={name}\n")
    query = {'name': name}
    response = requests.get(url, params=query, headers=header)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']
    else:
        print("Failed to retrieve the list of Families!")
        return None


def get_device_types(family_id=None):
    """Retrieves the list of device types belonging to a particular family
    """
    url = f"{BASE_URL}/{BASE_PATH}/identity/device-families/{family_id}/device-types"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending GET request to {url} with:\n"
          f"    header={header}\n")
    response = requests.get(url, headers=header)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']
    else:
        print("Failed to retrieve the list of Types!")
        return None


def get_applications(name=None, device_type_ids=[]):
    """Retrieves the list of applications available to install on devices
    """
    url = f"{BASE_URL}/{BASE_PATH}/applications"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending GET request to {url} with:\n"
          f"    header={header}\n"
          f"    name={name}\n"
          f"    deviceTypeIds={device_type_ids}\n")
    query = {'name': name, 'deviceTypeIds': device_type_ids}
    response = requests.get(url, params=query, headers=header)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']
    else:
        print("Failed to retrieve the list of Applications!")
        return None
    

def create_application(model=None):
    """Creates a new application definition in the system.
    """
    url = f"{BASE_URL}/{BASE_PATH}/applications"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending POST request to {url} with:\n"
          f"    header={header}\n"
          f"    model={model}\n")
    response = requests.post(url, headers=header, json=model)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']['id']
    else:
        print("Failed to create application!")
        return None


def update_application(app_id, model=None):
    """Edits an existing application in the system.
    """
    url = f"{BASE_URL}/{BASE_PATH}/applications/{app_id}"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending PUT request to {url} with:\n"
          f"    header={header}\n"
          f"    model={model}\n")
    response = requests.put(url, headers=header, json=model)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['success']
    else:
        print("Failed to update application!")
        return None


def get_application_versions(app_id=None, device_type_ids=[]):
    """Retrieves the list of applications available to install on devices
    """
    url = f"{BASE_URL}/{BASE_PATH}/applications/{app_id}/versions"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending GET request to {url} with:\n"
          f"    header={header}\n"
          f"    deviceTypeIds={device_type_ids}\n")
    query = {'deviceTypeIds': device_type_ids}
    response = requests.get(url, params=query, headers=header)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']
    else:
        print("Failed to retrieve the list of Application Versions!")
        return None


def create_application_version(app_id, model=None):
    """Creates a new application version definition in the system.
    """
    url = f"{BASE_URL}/{BASE_PATH}/applications/{app_id}/versions"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending POST request to {url} with:\n"
          f"    header={header}\n"
          f"    model={model}\n")
    response = requests.post(url, headers=header, json=model)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']['id']
    else:
        print("Failed to create application version!")
        return None


def update_application_version(app_id, version_id, model=None):
    """Edits an existing application version in the system.
    """
    url = f"{BASE_URL}/{BASE_PATH}/applications/{app_id}/versions/{version_id}"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending PUT request to {url} with:\n"
          f"    header={header}\n"
          f"    model={model}\n")
    response = requests.put(url, headers=header, json=model)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['success']
    else:
        print("Failed to update application version!")
        return None


def associate_file_and_device_types_with_version(app_id, version_id, file_id, device_type_ids=[]):
    """Associates an application version with a set of compatible device types,
       AND a file ID.
    """
    url = f"{BASE_URL}/{BASE_PATH}/applications/{app_id}/versions/{version_id}/file/{file_id}/device-types"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending PUT request to {url} with:\n"
          f"    header={header}\n"
          f"    deviceTypeIds={device_type_ids}\n")
    response = requests.put(url, headers=header, json=device_type_ids)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()
    else:
        print("Failed to update application version file and device types!")
        return None


def prepare_section(dir_path, version_id):
    """dir_path is a directory like "../Usti/routers/v3/SmartStart/SPECTRE-v3L-LTE/6.1.9/001 - LAN"
       This directory must contain 3 files:
       - 'metadata.json'
       - 'model.json'
       - 'ui_model.json'
       This function returns a dictionary suitable for use with create_application_sections()
    """
    print(f"\nModel path: {dir_path}")
    metaFile = os.path.join(dir_path, 'metadata.json')
    modelFile = os.path.join(dir_path, 'model.json')
    uiFile = os.path.join(dir_path, 'ui_model.json')

    with open(metaFile, 'r') as f:
        meta = json.load(f, object_pairs_hook=OrderedDict)

    with open(modelFile, 'r') as f:
        model = json.load(f, object_pairs_hook=OrderedDict)

    with open(uiFile, 'r') as f:
        ui = json.load(f, object_pairs_hook=OrderedDict)

    section = {
        'name': meta['section_name'],
        'display_name': model['title'],
        'version_id': version_id,
        'config_type': 'INIFile',
        'metadata': meta,
        'model': model,
        'ui_model': ui
    }

    return section


def create_application_sections(app_id, version_id, sections):
    """Creates new section definitions for an existing application
    """
    url = f"{BASE_URL}/{BASE_PATH}/applications/{app_id}/versions/{version_id}/sections"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending POST request to {url} with:\n"
          f"    header={header}\n"
          f"    model={sections}\n")
    response = requests.post(url, headers=header, json=sections)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()
    else:
        print("Failed to create application sections!")
        return None


def upload_file(filename, version):
    """Uploads the application's binary file to the system.

    The "version" string will be inserted into the filename.
    E.g. "SPECTRE-v3L-LTE.bin" > "SPECTRE-v3L-LTE_6.1.8.bin"
    """
    basename = os.path.basename(filename)
    name = f"{os.path.splitext(basename)[0]}_{version}{os.path.splitext(basename)[1]}"
    data = open(filename, 'rb').read()
    url = f"{BASE_URL}/{BASE_PATH}/files"
    header = {'Authorization': f'Bearer {USER_TOKEN}'}
    print(f"\nSending POST request to {url} with:\n"
          f"    header={header}\n"
          f"    name={name}\n"
          f"    body=<contents of {filename}>")
    query = {'name': name}
    response = requests.post(url, params=query, headers=header, data=data)

    print(response.status_code)
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except ValueError:
        print(response.text)

    if response.status_code == requests.codes['ok']:
        return response.json()['data']['id']
    else:
        print("Failed to upload file!")
        return None


def search(array, key, value):
    """Generic function to find a particular dictionary in a list of dictionaries,
       based on one key:value pair in each dict.
    """
    for item in array:
        if item[key] == value:
            return item
    return None


if __name__ == "__main__":
    args = parse_args()
    main(args)
