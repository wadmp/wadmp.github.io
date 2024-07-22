# 3.0.3: February 23, 2023

### Improvements:

- Added an API endpoint for creating configuration profiles from specification (in addition to the endpoint for creating configuration profiles from routers).

### Bug Fixes:

- Fixed a failure to display a device page after importing data from GEN2 that contained tags with “-”, “.” or one of a few other problematic non-alphabetic symbols in their name.

- Fixed an error in displaying a device page after creation of multiple fields that differed only in upper/lower case size.

- Fixed formatting of prices in billing notification emails (at most 2 decimal places will now be shown).

- Fixed the email link to billing details page that previously shown error 404 Not Found.

- Fixed “In Range” and “Not In Range” filtering operators not including their edge values.

- Fixed a redirect to the overview of alert endpoints after editing an alert endpoint and submiting changes.
