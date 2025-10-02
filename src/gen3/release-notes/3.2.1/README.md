# 3.2.1 May 12, 2025

### Improvements:

- Enhanced the desired configuration page by adding markings to indicate unsupported apps, improving user awareness and configuration accuracy.

- Implemented a confirmation dialog when initializing a VPN hub, ensuring users intentionally proceed with critical actions.

### Bug Fixes:

- Fixed an issue where devices with disabled VPN settings could still connect under specific conditions.

- Fixed the form for editing large text fields, ensuring that inputted values are now saved properly.

- Fixed an issue where the roadwarrior configuration file could contain whitespace in its name, which previously prevented successful import into a WireGuard client.

- Fixed a bug causing the VPN Configuration form to become stuck in a loading state after encountering an error.

- Fixed deletion of devices via dashboard table previously not unselecting them for batch operations.

- Fixed temporary UI freezes when adding a large number of devices to a VPN network, improving performance and responsiveness.

- Fixed an issue where remaining VPN trial days were displaying negative values, now showing accurate counts.

- Fixed an issue that allowed the creation of invalid alerts, causing crashes on the Alerts page.

- Fixed CIDR validation within the VPN Configuration dialog to ensure correct input handling.

- Fixed minor UI inconsistencies that occurred when switching between companies.

- Fixed a display issue on the roadwarrior page where data usage temporarily appeared as 0 MB after disabling a roadwarrior.

- Fixed an issue where audit log pages would incorrectly show an error when filtering by partial MAC address.

- Fixed dashboard widgets that should show Top/Bottom device not displaying any value.

- Fixed VPN hub being able to start for a short duration even for companies with expired trial period.

- Fixed filtering functionality for the “VPN Connected” column on the Roadwarriors page.

- Fixed several error messages to provide more detailed and informative feedback to users.

- Fixed an issue in the configuration profile creation dialog where the list of applications would fail to display.

- Fixed the issue so that a user’s email change now updates immediately in the top-right navigation, without requiring a re-login.

- Fixed router images that previously did not fit properly into their designated areas.

- Fixed an issue where dialogs were being submitted twice if the user confirmed input by pressing Enter.

- Fixed a problem where the mouse cursor did not change appropriately when selecting a device on the Alerts page.

- Fixed the line chart on the VPN Overview page to now refresh periodically.

- Fixed _UserPassword_ field not being saved when unset value ('-') is selected on dashboard.

- Fixed “Request body too large” error in _UpdateFile_ endpoint.
