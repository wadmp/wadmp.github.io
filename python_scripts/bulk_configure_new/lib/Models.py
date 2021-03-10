class DeviceModel:
    def __init__(self, data):
        apps = data['applications']
        self.type           = data['device_type']
        self.mac            = data['mac_address']
        self.firmware       = list(filter(lambda x: x['application_version']['application']['is_firmware'] == True and\
                                                    x['state'] == "Installed", apps))
        self.firmware       = self.firmware[0]
        self.pending_fw     = list(filter(lambda x: x['application_version']['application']['is_firmware'] == True and\
                                                    x['state'] != "Installed", apps))
        self.pending_fw     = self.pending_fw[0] if self.pending_fw else []
        self.apps_installed = list(filter(lambda x: x['application_version']['application']['is_firmware'] == False and \
                                                    x['application_version']['application']['name'] != 'wadmp_client', apps))