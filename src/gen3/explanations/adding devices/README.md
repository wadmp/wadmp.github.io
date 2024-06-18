# Adding Devices

##	1. Register A Device (On-Premises Only)

In the on-premises version of our system, administrators must register devices before they can be added. This process is necessary because on-premises installations lack access to our manufacturing database, which is utilized for device registration in the public instance. Here's how administrators can register a device:

1. **Accessing Device Registration:**
   - Navigate to the dashboard interface.
   - Click on the "+" icon located above the dashboard table.

2. **Registration Process:**
   - Upon clicking the "+" icon, administrators will be directed to the device registration interface.
   - Administrators will notice an additional tab labeled "Create Device."

      ![create device](../images/devices/create-device.png)

   - Fill in the required details about the device in this tab.

      ![register on premises](../images/devices/register-on-premises.png)


3. **API Endpoint:**
   - Additionally, administrators have the option to register devices programmatically using the API endpoint designated for device registration.

By following these steps, administrators can efficiently register devices in the on-premises version of our system, ensuring seamless integration and management within their environment.

##	2. Add A Device
 ⚠️ You must have the appropriate permissions to add a device to your company.

### User Criteria for adding a Device

* User authentication: You need to log in and have the right permissions.

* You can select your username from the Users list to check your permissions.

 * An example of how permissions are displayed is shown below:

![permissions](../images/devices/permissions_user-1.png)

### Rules

* Both removed and new devices can be added.
* A device can only be added by one company at a time.
* A company can remove a device it has previously added.
* A device must be added by a company before it can be managed or monitored.
* A free company can add up to five unique devices. Once you add five devices, you cannot add more, even if you remove a device. The limit is based on the number of times the "Add" device function has been used successfully, not the current number of devices.


### Steps To Add a Device

#### How to obtain router information?

* You can obtain router information through the WebAccess/DMP Client application by following these steps:
 1. Login to the router's user interface.
 2. Navigate to Router Apps (in Customization section of the menu).
 3. Enter the WebAccess/DMP Client application.
 4. Click on Create Device on WA/DMP.
 5. You will find the information about this router there.

![Router informations](../images/devices/routerinformations2.jpg)

* You can also use the printed device labe:

 ![label](../images/devices/device_label.png)

#### Steps to add a device for your company (Assuming you have the required permissions):

1. Navigate to the "Dashboard" on the Side Menu.
2. Click the "Add Devices" action button above the table.

   ![add Device](../images/devices/add_device.png)

3. Fill out the "Add Device" form with the following information:

   - **Alias:**
    Enter a human-friendly name to help identify the device later.*This field is optional.*

   - **MAC Address:**
    Enter the exact MAC Address for ETH0 of your device as it appears on the device label. The format should be `00:0A:14:aa:bb:cc`. *This is a required field.*

   - **Serial Number:**
    Enter the exact Serial Number as printed on the device label, including any alphanumeric characters. *This is a required field.*

   - **IMEI:**
    Enter the exact IMEI number as printed on the device label. Note that some devices may not have an IMEI number; *this field is only required if applicable.*

   ![add decice](../images/devices/adddevice1.png)

4. If you need to add more than one device at a time, enable the option "Add multiple devices from CSV".

5. Click the *Submit* button to complete the add.


* Here’s how the Add Device form would look when filled out:

![filled Form](../images/devices/claimDeviceForm_1.png)

* **After successfully adding a device, it will appear in the Device List for your company, as shown here:**

![added Device](../images/devices/added-device.png)



##	3. Install a WebAccess/DMP client app
xxxxxxxxxxxxxxxxxxxxxxxx

##	4. Firewall considerations (ports & addresses to whitelist)
xxxxxxxxxxxxxxxxx

