# 3.0.2: December 15, 2023

This is primarily a bug-fixing release, which also brings a few quality-of-life improvements.

### Improvements:

* Added a button to enable/disable alert rules on the *Alerts* page. 

* Added a feature to convert audit log timestamps to the user's local time.

* Added a “*Billing*” page for premium companies, which displays a list of historical billings. 

* Added persistence to the *page size* table setting (the UI now remembers the last selected value).

* The default time range for Audit logs has been changed from “the last 24 hours” to “the last 2 months”.

* Simplified the creation of charts on the Device page (the “*Aggregation Type*” parameter is no longer used).

* Added names of affected fields to DEVICE_UPDATED auditing message.

* [On-Premises] Added a button for creating users without an email confirmation.

### Bug Fixes:

* Fixed Alerts page and email messages showing internal representations of *Operand* and *Operator* (e.g. displaying “0” instead of “offline”).

* Fixed Dashboard page showing a loading animation for as long as a company has no views.

* Fixed Dashboard table showing duplicate devices after table`s page size is changed.

* Fixed Companies page not showing a newly created company until the page is refreshed.

* Fixed user being unable to switch from an existing company to a company that was just created by that user.

* Fixed user being shown in a table of users after having been removed from a company until a page is manually refreshed.

* Fixed chart`s name being reset to an empty string after a user edits it and saves it unchanged. It is also no longer possible to save a chart with an empty name.

* Fixed export of devices including only the data from the first or last page.

* Fixed batch edit affecting only the data from the first or last page.

* Fixed Device page showing green icon for all possible values of synchronization status.

* Fixed multiple auditing messages showing names of variables instead of their values.

* Fixed DEVICE_CREATED audit logs not being associated with a device.

* Fixed AlertDetail page sometimes not loading up correctly for alerts that target a single device.

* Fixed user`s email change not being reflected in the top right menu until the user relogs.

* Fixed various small UI issues that occurred only to users with Vivaldi browser.

* Fixed various small API issues (endpoints returning incorrect status code, etc.)

* [On-Premises] Fixed SearchDevices service not starting up if there exists a company without any reportable fields.

* [On-Premises] Improved handling of failures to send emails due to unsupported SMTP configuration. Also, using authentication for SMTP server is now optional.