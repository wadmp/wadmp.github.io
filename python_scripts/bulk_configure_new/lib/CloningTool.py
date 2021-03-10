import requests
import json
import time

#################################################
# For some responses accessing the json() method 
# throws error. This method lets us not care about
# that.
def response_str(resp):
    try:
        return f"{resp.status_code}: {resp.json()['message']}"
    except:
        return f"{resp.status_code}"

#################################################
# Returns true if the given firmware version is
# already on device2 (either as pending or as 
# installed).
def fw_already_present(fw_app_version_id, device2):
    if device2.pending_fw and \
       fw_app_version_id == device2.pending_fw['application_version']['id']:
        return True
    return fw_app_version_id == device2.firmware['application_version']['id']


class CloningTool:

    @staticmethod
    def clone_firmware(api, device1, device2):
        if fw_already_present(device1.firmware['application_version']['id'], device2):
            print(f"Skipping Firmware installation (already installed or queued).")
            return
        print(f"Installing Firmware {device1.firmware['application_version']['version']}.")
        resp = api.device.install_app(device2.mac, device1.firmware['application_version']['id'])
        if resp.status_code != requests.codes['ok']:
            print(resp.json()['message'])
            raise RuntimeError(f"Couldn't install new firmware ({response_str(resp)})")

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
                    raise RuntimeError(f"Installation of {app1_name} failed ({response_str(resp)})")

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
                    raise RuntimeError(f"Uninstallation  of {app2_name} failed ({response_str(resp)})")

    @staticmethod               
    def clone_firmware_settings(api, device1, device2):
        src_app_id = device1.firmware['application_version']['id']
        dst_app_id = device2.firmware['application_version']['id']
        app_name = "firmware" # Only relevant for printing errors.
        CloningTool._clone_app_settings(api, device1.mac, device2.mac, src_app_id, dst_app_id, app_name)

    @staticmethod
    def clone_apps_settings(api, device1, device2):
        for app in device1.apps_installed:
            app_version_id   = app['application_version']['id']
            app_name = app['application_version']['application']['name'] # Only relevant for printing errors.
            CloningTool._clone_app_settings(api, device1.mac, device2.mac, app_version_id, app_version_id, app_name)

    ############################################################
    # This method can be used for cloning firmware/user module
    # settings between 2 devices.
    # The reason for having 'src' and 'dst' version_id here is  
    # to enable cloning settings between different versions of 
    # firmware (each version of firmware has its own version_id).
    @staticmethod
    def _clone_app_settings(api, mac1, mac2, src_app_version_id, dst_app_version_id, app_name):
        resp = api.device.get_settings(mac1, src_app_version_id)
        if resp.status_code != requests.codes['ok']:
            raise RuntimeError(f"Getting settings of {app_name} failed ({response_str(resp)})")
        sections = []
        for section in resp.json()['data']:
            sections.append({'section_id': section['section_id'], 'set_config': section['desired_configuration']})
        print(f"Updating settings of {app_name}.")
        resp = api.device.update_settings(mac2, dst_app_version_id, sections)

        # TODO: Find a way to avoid the following workaround:
        # Update of configuration usually fails when done shortly after 
        # updating firmware. So if we receive this error, we will 
        # sleep for a while and then try again. 
        if resp.status_code == 404: 
            time.sleep(5)
            resp = api.device.update_settings(mac2, dst_app_version_id, sections)
        
        if resp.status_code != requests.codes['ok']:
            raise RuntimeError(f"Update of {app_name} settings failed ({response_str(resp)})")
