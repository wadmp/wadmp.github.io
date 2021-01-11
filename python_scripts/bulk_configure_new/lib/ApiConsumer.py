import requests

class ApiDevice:
    def __init__(self, session, base_url_api, auth_token = None):
        self.session = session
        self.base_url_api = base_url_api
        self.auth_token = auth_token

    def set_auth_token(self, auth_token):
        self.auth_token = auth_token

    def create(self, serial, mac, type_id, order_code="test"):
        url = f"{self.base_url_api}/identity/devices"
        header = {'Authorization': f'Bearer {self.auth_token}'}
        model = {
            "serial_number": serial,
            "mac_address": mac,
            "device_type_id": type_id,
            "order_code": order_code
        }
        response = self.session.post(url, headers=header, json=model)
        return response

    def claim(self, serial, mac, company_id, alias="", imei=""):
        url = f"{self.base_url_api}/identity/devices/claim"
        header = {'Authorization': f'Bearer {self.auth_token}'}
        model = {
            "serial_number": serial,
            "mac_address": mac,
            "company_id": company_id,
            "imei": imei,
            "alias": alias
        }
        response = self.session.post(url, headers=header, json=model)
        return response

    def release(self, serial, mac, imei):
        url = f"{self.base_url_api}/identity/devices/release"
        header = {'Authorization': f'Bearer {self.auth_token}'}
        model = {
            "serial_number": serial,
            "mac_address": mac,
            "imei": imei,
        }
        response = self.session.post(url, headers=header, json=model)
        return response

    def get_by_mac(self, mac):
        url = f"{self.base_url_api}/management/devices/{mac}"
        header = {'Authorization': f'Bearer {self.auth_token}'}
        response = self.session.get(url, headers=header)
        return response       

    def get_apps(self, mac):
        url = f"{self.base_url_api}/management/devices/{mac}/apps"
        header = {'Authorization': f'Bearer {self.auth_token}'}
        response = self.session.get(url, headers=header)
        return response 

    def get_settings(self, mac, app_version_id):
        url = f"{self.base_url_api}/management/devices/{mac}/apps/{app_version_id}/settings"
        header = {'Authorization': f'Bearer {self.auth_token}'}
        response = self.session.get(url, headers=header)
        return response 

    def update_settings(self, mac, app_version_id, data):
        url = f"{self.base_url_api}/management/devices/{mac}/apps/{app_version_id}/settings"
        header = {'Authorization': f'Bearer {self.auth_token}'}
        response = self.session.put(url, headers=header, json=data)
        return response

    def install_app(self, mac, app_version_id):
        url = f"{self.base_url_api}/management/devices/{mac}/apps/{app_version_id}"
        header = {'Authorization': f'Bearer {self.auth_token}'}
        response = self.session.post(url, headers=header)
        return response

    def remove_app(self, mac, app_version_id):
        url = f"{self.base_url_api}/management/devices/{mac}/apps/{app_version_id}"
        header = {'Authorization': f'Bearer {self.auth_token}'}
        response = self.session.delete(url, headers=header)
        return response

    def update_settings_section(self, mac, app_version_id, section_id, data):
        url = f"{self.base_url_api}/management/devices/{mac}/apps/{app_version_id}/settings/{section_id}"
        header = {'Authorization': f'Bearer {self.auth_token}'}
        response = self.session.put(url, headers=header, json=data)
        return response

#################################################
# Class for obtaining authorization token.
class ApiAuth:
    def __init__(self, session, base_url_auth):
        self.session = session
        self.base_url_auth = base_url_auth

    # Log into the the system and return authorization token.
    def authorize(self, username, password):
        url = f"{self.base_url_auth}/auth/connect/token"
        credentials = {'username': username,
                       'password': password,
                       'client_id': 'python',
                       'grant_type': 'password'}
        response = self.session.post(url, data=credentials)
        # How to get token from the response object: 
        #      response.json()["access_token"]
        return response

#################################################
# This class can be used for sending API requests
# and parsing response.
class ApiConsumer:
    def __init__(self, base_url="https://gateway.dev.wadmp.com"):
        self.session       = requests.Session()   # For sending API requests.
        self.base_url_auth = f"{base_url}/public" # Where authorization and weird stuff lies.
        self.base_url_api  = f"{base_url}/api"    # Where API lies.
        # SubAPIs:
        self._auth          = ApiAuth(self.session, self.base_url_auth)
        self.device         = ApiDevice(self.session, self.base_url_api)

    def login(self, username, password):
        response = self._auth.authorize(username, password)
        if response.status_code != requests.codes['ok']:
            raise RuntimeError("Authorization Failed (ERR: " + str(response.status_code)+") "+str(response.json()))             
        auth_token = response.json()["access_token"]
        self.device.set_auth_token(auth_token)