import requests
import json

class CloningTool:

    @staticmethod
    def clone_firmware(api, device1, device2):
        if device1.firmware['application_version']['id'] != \
           device2.firmware['application_version']['id']:
            print(f"Installing Firmware {device1.firmware['application_version']['version']}.")
            resp = api.device.install_app(device2.mac, device1.firmware['application_version']['id'])
            if resp.status_code != requests.codes['ok']:
                raise RuntimeError(f"Couldn't install new firmware [response code: {resp.status_code}]")

    @staticmethod
    def clone_apps(api, device1, device2):
        # Install apps that are on device1 but not on device2
        for app1 in device1.apps_installed:
            found_on_device2 = False
            for app2 in device2.apps_installed:
                if app2['application_version']['id'] == app1['application_version']['id']:
                    found_on_device2 = True
                    break
            if not found_on_device2:
                app1_name = app1['application_version']['application']['name']
                print(f"Installing {app1_name}.")
                resp = api.device.install_app(device2.mac, app1['application_version']['id'])
                if resp.status_code != requests.codes['ok']:
                    raise RuntimeError(f"Installation of {app1_name} failed [response code: {resp.status_code}]")

        # Uninstall apps that are on device2 but not on device1
        for app2 in device2.apps_installed:
            found_on_device1 = False
            for app1 in device1.apps_installed:
                if app2['application_version']['id'] == app1['application_version']['id']:
                    found_on_device1 = True
                    break
            if not found_on_device1:
                app2_name = app2['application_version']['application']['name']
                print(f"Removing {app2_name}.")
                resp = api.device.remove_app(device2.mac, app2['application_version']['id'])
                if resp.status_code != requests.codes['ok']:
                    raise RuntimeError(f"Uninstallation  of {app2_name} failed [response code: {resp.status_code}]")

    @staticmethod               
    def clone_firmware_settings(api, device1, device2):
        app_id = device1.firmware['application_version']['id']
        app_name = "firmware" # Only relevant for printing errors.
        CloningTool._clone_app_settings(api, device1.mac, device2.mac, app_id, app_name)

    @staticmethod
    def clone_apps_settings(api, device1, device2):
        for app in device1.apps_installed:
            app_id   = app['application_version']['id']
            app_name = app['application_version']['application']['name'] # Only relevant for printing errors.
            CloningTool._clone_app_settings(api, device1.mac, device2.mac, app_id, app_name)

    @staticmethod
    def _clone_app_settings(api, mac1, mac2, app_version_id, app_name):
        resp = api.device.get_settings(mac1, app_version_id)
        if resp.status_code != requests.codes['ok']:
            raise RuntimeError(f"Getting settings of {app_name} failed [response code: {resp.status_code}]")
        sections = []
        for section in resp.json()['data']:
            sections.append({'section_id': section['section_id'], 'set_config': section['desired_configuration']})
        print(f"Updating settings of {app_name}.")
        resp = api.device.update_settings(mac2, app_version_id, sections)
        if resp.status_code != requests.codes['ok']:
            raise RuntimeError(f"Update of {app_name} settings failed [response code: {resp.status_code}]")
