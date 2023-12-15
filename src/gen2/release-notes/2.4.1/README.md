# 2.4.1: January 18, 2022

This is a primary bugfix release that addresses several issues that have been recently appearing.

### Improvements:

* A pagination option for 100 entries was added to all places in UI.

* Permission to delete devices is now the default for all newly added Company Admins. Note that this applies only for freshly created Company Admins; permissions of already existing users are not affected.


### Bugfixes:

* Fixed users with 20+ companies who experienced an issue with sign-in.

* Fixed GPS data not showing on the map at the dashboard.

* Fixed Alerts targeting a single device being perpetually triggered.

* Fixed Alerts do not support float numbers for StatusTemperature and StatusVoltage fields.

* Fixed avatar icons that showed more than two letters. Now only the first letters of the first two words are shown.

* Fixed auditing records with DEVICE_RELEASE action type not containing company ID.

* Fixed incorrect handling of malformed application version strings when reported by some routers.

* Fixed several API endpoints returning undocumented response 500 Internal Error when the user is not authorized. They now return 401 Unauthorized.

* Fixed several API endpoints returning undocumented response 500 Internal Error when called with invalid parameters.

### Content:

* Fixed inconsistencies between Router app names in a device and the database records.
  