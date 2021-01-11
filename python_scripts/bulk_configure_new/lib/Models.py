class DeviceModel:
    def __init__(self, data):
        apps = data['applications']
        self.type           = data['device_type']
        self.mac            = data['mac_address']
        self.firmware       = list(filter(lambda x: x['application_version']['application']['is_firmware'] == True, apps))[0]
        self.apps_installed = list(filter(lambda x: x['application_version']['application']['is_firmware'] == False and \
                                                    x['application_version']['application']['name'] != 'wadmp_client', apps))
            