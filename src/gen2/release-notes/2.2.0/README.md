# 2.2.0: 8th June 2020

This release introduces a significant new feature: Playbooks.

* Apply a sequence of "actions" to a group of devices immediately or at a scheduled time in the future.
* Devices may be already online or not online yet. i.e., Zero-Touch Provisioning, mass deployment.
* Supported actions include:
  * Set Firmware
  * Install User Module
  * Apply a Settings Group
  * Reboot
  * Change Local Password

### UI

* Major new feature: Playbooks.
* New feature: Device Groups.
* New feature: Settings Groups.
* New feature: change the local password for the root user on a device.
* Bugfix: validated users are now shown green on the Users screen.
* Added “Change Password” feature for users.
* Bugfix: search for users.

### Code / API

* REST API: new endpoints for managing Playbooks.
* REST API: new endpoint to update a Settings Group.
* REST API: new endpoints for change-password, retrieve-password.
* Bugfix: some devices were showing as offline when they were online.
* Bugfix: Prevent cyclical company structures.

### Content

* Added the HMPClient User Module (for backward compatibility with Gen1).
* Added the latest version of the WA/DMP Client User Module: 2.0.5.
* Bugfix: changes to the WLAN section were causing some devices to be out of sync.

### docs.wadmp.com

* Added Privacy Policy page. [[1]](https://docs.wadmp.com/privacy-policy.html)
* New article “Understanding OAuth”. [[2]](https://docs.wadmp.com/explanations-discussions/understanding-oauth.html)
* Fixed bug in example Node-RED flow. [[3]](https://github.com/wadmp/wadmp.github.io/tree/master/node-red_flows)
* Added “release_from_csv.py” script to CSV utilities. [[4]](https://github.com/wadmp/wadmp.github.io/tree/master/python_scripts/csv_utilities)
* Added new Bulk Configuration scripts. [[5]](https://github.com/wadmp/wadmp.github.io/tree/master/python_scripts/bulk_configure)
