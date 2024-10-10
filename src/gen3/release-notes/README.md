# 3.1.2: September 12, 2024

### Improvements:

- Improved the text of several error messages to be more helpful.
- Sorted the options that are offered when editing rows of a dashboard table. Application and Firmware versions are now sorted from the latest to the oldest.
- Added an option to update names of existing configuration profiles.
- Added an option to use 3rd party identity provider when registering through the company invitation link.

### Bug Fixes:

- Fixed dashboard table filtering not working for date values.
- Fixed dashboard table previously not automatically refreshing after adding a device or performing a&nbsp;batch operation.
- Fixed 2-FA not being enforced for users that sign-in via 3rd party identity providers (Google/Microsoft).
- Fixed password reset not working for users that have not yet clicked the verification sent during their registration process.
- Fixed _IsServiceAccount_ flag being always hidden at the permission page. Now it will show up if the user is in at least one company where 2-FA is enabled.
- Fixed disabling of permission checkboxes in the UI to correctly reflect what permissions the active user can grant.
- Fixed import/export of device data from CSV failing if certain types of Fields are present.
- Fixed users being previously able to create multiple Fields that target the same application, setting, user or script.
- Fixed editing of information about Fields not working if multiple Fields of the same kind exist.
- Fixed Fields created via import of data from DMP version 2.x.x not being available until a page refresh or relog.
- Fixed table editing on a device page to offer the same options as dashboard table.
- Fixed Desired Configuration device tab sometimes not working correctly when submiting changes more than once before leaving the page.
- Fixed error message not being displayed when attempting to exceed the maximum number of free devices.
- Fixed _Between_ filtering operator not working for numeric columns on dashboard.
- Fixed _“Empty”_ (set to an empty string) and _“-”_ (not set) values being untintentionally grouped into the same slice in pie charts.
