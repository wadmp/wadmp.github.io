# 2.5.1: November 15, 2022

This release contains improvements and bug fixes.

### Improvements:

* Stopped storing the temperature when the value is absolute zero (-273 Celsius degrees). This value is used by the device to report that no temperature could be measured. Now, this value is not stored and nothing is showing in temperature graphs correctly.

### Bug Fixes: 

* Fixed Playbooks failing to complete in a specific situation when there was a pending or failed update/downgrade of the application that the playbook was targeting.

* Fixed "Uptime" on the "My Devices" page now being calculated from the time of connection being established rather than the last registration message.

* Fixed the API Alert endpoints missed the check of name, recipient, and company id.

* Fixed supported characters in the Mobile WAN APN Username of the device configuration. The character "-" is now accepted.

### Content

* Added support for IPsec and OpenVPN Up/Down scripts (firmware versions 6.3.7 and higher).