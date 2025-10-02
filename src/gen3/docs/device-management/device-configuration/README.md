---
next: ../../device-monitoring/
---

## Device Configuration

Device configuration may be done individually via specific managed settings (Fields from the Configuration category) that can be changed per device, and via Configuration Profiles (these are sets of settings values that serve as a template).

A combination of both is possible.

::: tip Example:
When you have hundreds of devices and need the same Firmware version on all of them, the same Router App version on all of them, but a different interface IP address for each device, you can:

- Prepare a Configuration Profile (that would include settings shared by all devices).
- Add a Unique Setting Value Field for the interface IP address.

**Assign a Configuration Profile**

- Set up a view on the dashboard that contains a devices table with columns for the Configuration Profile Field and the Unique Setting Value Field.

- Select all devices in the table, and using the Batch Edit dialog, apply the same Configuration Profile to all devices.

**Setup Unique Setting Value Field**

- For the individual IP address setting:

  - Export the dashboard table data to a CSV file.
  - Open the CSV file in Excel and copy increasing IP addresses to the Unique Setting Value column.
  - Import the updated CSV file back.

  For each individual device, both values from the Configuration Profile and the Unique Setting Value Field are tracked as managed (desired) by WebAccess/DMP. Unique Setting Value Field has priority over Configuration profile. You can check this (or setup for individual device) on the Desired Configuration tab on the Device page.

  :::

### Configuration Profiles

Configuration profiles are used for easy installation of any of our Router Apps, as well as router firmware and its overall settings as individual devices or bunch devices in bulk.

You may create Configuration Profile from scratch, clone from existing, or setup one model device and then create Configuration Profile as a snaphsot from this device.

#### Creating of Configuration Profile as a Snapshot from Device:

1. First, you must choose an example router that will be used to create a default configuration for your Configuration Profile.

2. Connect to your router via IP address to the user GUI.

![login](../../images/management/login.png)

3. Ensure you're running the latest WebAccess/DMP Client in the Router Apps section so the router is connected with WA/DMP. You can check the Client Release Notes section for the latest version of WA/DMP.

![WADMP Client Version](../../images/management/client-vers.png)

4. Now you can make all desired settings localy via Web interface in the selected device. This includes all your desired Router Apps, Firmware version, Configuration settings of the router, Scripts and Users.

5. At this point, head for the Dashboard in WebAccess/DMP and find your device in the table, where you can make a Configuration Profile out of this router (the icon button to create Configuration Profile is also accessible in the header of individual Device Page).

   Note: If you create Configuration Profile from the device that already has Configuration Profile setup, the created Configuration Profile will be the result of original Configuration Profile and ather individual configuration fields if applicable.

![Create Configuration Profile](../../images/management/Create-ConfigP2.png)

6. Now you can apply your newly created Configuration Profile to any router in your current Company, as showcased in the picture below.

![Configuration Profile Edit](../../images/management/ApplyingConfP2.png)

::: tip Example Tip:
If you apply Configuration Profile, the router will apply all configurations from the router from which Config Profile was created.

For example:

- You have router_1 with an IP address on eth0=10.10.10.1 and router_2 with an IP address on eth0=10.10.10.2.
- If you create a Config Profile from router_1, it will contain setting ETH_IPADDR=10.10.10.1. and if you apply that Config Profile to router_2, setting ETH_IPADDR on router_2 will be overwritten to 10.10.10.1.
- Only if you create a Unique setting with Setting Name ETH_IPADDR (the exact name of the setting from the router) and display the name, for example, Unique_ETH_IPADDR, and edit that field to Unique_ETH_IPADDR=10.10.10.2, the setting will not be overwritten, because the individual Unique Settings fields have priority over Configuration Profile values.

:::

7. You can overview, compare, and delete your Configuration Profiles in the _Configuration Profiles_ section.

![config_prof_menu](../../images/management/ConfigProfile1.png)

8. You can overview Configuration Profile values by clicking on it.

![Config Profile Compare](../../images/management/ConfigProfileCompare3.png)

9. you can Clone or delete, or you can create new Config Profile from scratch, if you know your desired settings names and values.

![create Config Profile](../../images/management/CreateNewCompareConfigurationProfile.png)

10. Compare by choosing 2 Configuration Profiles of your desire.

![Config Profile Compare 2](../../images/management/CompareConfigurationProfile-2.png)

### Overriding Specific Settings

You may override specific setting as desribed above in introduction and example tip (via field edited on devices table). You may also set or overide specific setting directly on device page:

On Device page on Desired Configuration tab, there is your individual device configuration overview and control:

![Config Profile Compare](../../images/management/desired-config.png)

- You can assign Configuration Profile here. When unassigned, you need to Read Router Configuration first (press the button) to see individual settings and their values on the device. Only online devices can be read.

- You can set the individual settings as Desired (managed). This action creates a new Field automatically, if needed.

- You can do this for:

  - Firmware and Apps,
  - Settings,
  - Scripts,
  - Users,

    as seen on the respective tabs.

- Changes are propagated to the device after clicking on the "Apply Desired Configuration" button.

### Performing Batch Edit of Field Values

#### In Devices Table on Dashboard

To edit multiple devices at once:

1. Select your desired devices (you can also choose all devices, which really selects all ignoring pagination).
2. Click on the _Batch Edit Filtered Devices_ icon.

![Batch Filter](../../images/dashboards/BatchFilter.png)

3. Specify your changes in the _Batch Edit Devices_ table.
4. Confirm the changes by clicking the _Submit_ button. The changes will apply only to the selected devices.

![Batch Filter2](../../images/dashboards/BatchFilter2.png)

#### Via CSV Export/Import

You can also set editable Fields (including configuration) vie CSV Import. It is advisable to setup your dashboard devices table to contain all columns (Fileds) you want to edit in CSV file (via Excel), and the Export them first (as described in Monitoring section - [Exporting data to CSV](/gen3/docs/device-monitoring/exporting-data-to-csv/)), edit them vie Excel and Import back on the same Dashboard view:

![Import data](../../images/dashboards/Data_Import.png)
