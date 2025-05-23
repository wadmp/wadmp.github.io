# Networks & Devices

- You need to add Devices / Roadwarriors to same Network (group) to make them visible to each other via VPN.

## Networks

- On Networks page, you can manage Networks (groups) of your company VPN. Navigate to VPN - Networks section in menu.

<p align="center">
  <img src="../../images/vpn/vpn_networks_select.png" alt="VPN Networks">
</p>

- Here you'll be able to add new networks by clicking the **ADD** button.

![VPN Networks](../../images/vpn/vpn_networks.png)

- You can choose between two network types:

![VPN Networks](../../images/vpn/vpn_networks_addnetwork.png)

1. **All to All** &rarr; _All to All_ refers to a network configuration where all devices see each other, allowing direct communication between every device in the network without restrictions. Each device can send and receive data to and from any other device. Roadwarriors have a special role → they can see all devices, but the devices do not see them, so the Roadwarrior must initiate the communication. Roadwarriors also do not see each other.

2. **Master to Slave** &rarr; _Master-to-Slave_ refers to a network configuration where the Master device (server) controls and manages the connections, while the Slave devices follow its instructions. This setup is often used for centralized management and control. The Master and Slave devices always see each other, but a Slave device does not see other Slaves. Roadwarriors have a special role → they can see all devices (both Master and Slave), but the devices do not see them, so the Roadwarrior must initiate the communication. Roadwarriors do not see each other.

- Once you've created your networks, you can either enter them by clicking on their name, or edit/delete them using the options on the right side of each line.
  ![VPN Networks](../../images/vpn/vpn_networks_select_2.png)

- When you enter your desired network, you can edit the network's name by clicking the **EDIT NETWORK** button, or add devices by clicking the **ADD DEVICES** button.

![VPN Networks](../../images/vpn/vpn_networks_edit.png)

- When adding devices to your network, you can either select all available devices or choose specific ones based on your preference.

![VPN Networks](../../images/vpn/vpn_networks_add-device.png)

- Using _Add Device_, a Roadwarrior can also be added to the network, and all of them are reffered as Clients.

- You can now either enter your device by clicking its name, or use the options on the right side of its line to access the _Proxy Link_, edit its role, or delete it.

![VPN Networks](../../images/vpn/vpn_networks_proxy.png)

- When editing your device's role, you can switch between _Master_ and _Slave_ modes (applicable in Master-Slave network type only).

![VPN Networks](../../images/vpn/vpn_networks_master-slave.png)

## Devices

### Status of a Device

⚠️ **Note:** To connect a device to VPN, ensure the device has Client Router App version 3.2.0 or higher installed, where VPN is supported.

On WebAccess/DMP, the status of VPN connection of the device is visible on device page header. Also "VPN Connected" Field can be added on the dashboard. When the device is added in Network, connection status of devices is also visible on Network detail page.

![VPN Networks](../../images/vpn/vpn_device_status.png)

On device in client, you can check the VPN Connection status on this page in WebAccess/DMP Client Router App:

![VPN Networks](../../images/vpn/vpn_client_status.png)

### VPN Tab on Device Detail Page

- Once you're in the device's VPN tab, you can configure the following settings:

1. Disable or Enable VPN client of the device
2. Edit membership in VPN networks.

![VPN Networks](../../images/vpn/vpn_device_edit-networks.png)

#### PROXY

![VPN Networks](../../images/vpn/vpn_device_online.png)

1. In the Proxy section, you can disable the proxy and reset its URL using the **DISABLE PROXY** and **RESET URL** buttons.

2. You can add additional Proxy links, where you can specify the Local IP, CIDR, and Local Interface of the device. This is useful when you have a device with a Web User Interface behind the router and want to access it directly via VPN. You need to know the address of the local network where the device behind the router is accessible. Note that adding a proxy link will expose the link to the Internet (it will automatically add a LAN interface on the LANs tab).

![VPN Networks](../../images/vpn/vpn_device-proxy_add.png)

3. Delete the Proxy link from the device.

⚠️ Note: Change in proxy link may take up to 3 minutes to update the config on server.

⚠️ Note: When in UI on a device via VPN Proxy link, size of file that can be uploaded is limited to 256 MB.

⚠️ Known Issue: Proxy links do not work when the device has Firmware versions 6.5.1 or 6.5.0. Please update Firmware on the device.

#### LANS

![VPN Networks](../../images/vpn/vpn_device_lans.png)

1. In the LANS section, you can edit the VPN subnet by clicking the **EDIT VPN SUBNET** button.

![VPN Networks](../../images/vpn/vpn_device_lans_edit-subnet.png)

2. Add additional LAN interfaces by clicking the **ADD** button. Adding a LAN interface enables direct access via VPN to any device behind the router. 1:1 NAT is used; to find the VPN IP address of your locally known device, use the provided address translator (magnifying glass icon for the added interface).

![VPN Networks](../../images/vpn/vpn_device_lans_add-lan-interface.png)

3. Delete the LAN interfaces from the device.

4. Access Local Address Translator. You can then access your device directly in the VPN network, e.g., via SSH.

<p align="center">
  <img src="../../images/vpn/vpn_device-lans-access.png" alt="VPN Networks">
</p>

#### DATA USAGE

1. In the Data Usage section, you can view the data usage over the past year.

![VPN Networks](../../images/vpn/vpn_device_data-usage.png)

#### CONNECTION HISTORY

1. In the Connection History section, you can track the times when your device was connected or disconnected.

![VPN Networks](../../images/vpn/vpn_device_connection-history.png)
