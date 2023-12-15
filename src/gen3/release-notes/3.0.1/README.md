# 3.0.1: September 21, 2023

This release focuses mainly on fixing bugs that were found in version 3.0.0.

### Improvements:

* Added an option to change the order of View tabs (Drag & Drop).

* On-premises deployments may now be configured to create all companies as type Trial instead of type Free.

* Added a button for deleting information about alerts` triggering history.

### Bug Fixes:

* Fixed Dashboard lacking some fields in the list of options for creating Charts and Company Stats.

* Fixed Device page offering for Chart creation fields that do not support this functionality.

* Fixed Device page showing incorrect value for Connection Status field.

* Fixed Alert Creation/Update page not allowing users to change Period and Cooldown.

* Fixed Alert Creation/Update page offering multiple invalid options when a Single Device target was selected.

* Fixed alerts targeting Invalid Login Attempts Count source not getting triggered when they should.

* Removed the date of EULA`s confirmation from the EULA_CONFIRMED auditing message.

* Fixed Fields page not being refreshed after field deletions.

* Fixed Alert Endpoints page loading very slowly when accessed for the first time after each login.

* Fixed user invitation to the company failing when the requester selects no permissions.

* Fixed message for successful claiming device saying "undefined" in place of a company name.

* Fixed the User Permissions page showing a miss-aligned permissions table when viewed on small screens.