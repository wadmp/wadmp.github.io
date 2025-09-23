# 3.3.0 September XX, 2025

### Improvements:

- **Device Pages**
  - Added a **Connection History** tab.
  - Added an **Interfaces** tab.
  - Reworked the **VPN** tab for a more user-friendly experience.
  - Added a visual indicator for unsupported apps on the **Desired Configuration** tab.

- **Proxy Links**
  - Proxy links can now have a custom **name**.
  - Added support for **custom destination ports**.
  - Added the ability to choose between **HTTP** and **HTTPS**.
  - Added an option to configure an **expiration period**.
  - Added the ability to **disable** a proxy link without deleting it.

- **VPN Networks**
  - Added bulk device removal from VPN networks.
  - Reworked VPN data usage charts to show **monthly total usage** instead of immediate usage.
  - Added tooltips explaining VPN **network types** and **roles**.

- **Alerts**
  - Improved the UI for creating, editing, and displaying alerts.
  - Added the option to evaluate alerts only for devices with a specified **tag**.
  - Added support for **custom alert messages** with placeholders for dynamic values.
  - Added a button to delete multiple alert history records at once.

- **Fields**
  - Added read-only field **Firmware Version**.
  - Added read-only field **DMP Client Version**.
  - Added read-only field **VPN LAN Proxy Links**.
  - Added read-only field **WAN Interface Name**.

- **User Management**
  - Added a UI option to **view and manage pending invitations**.
  - Implemented measures to prevent accidental uninstallation of the WebAccess/DMP Client app.
  - Uninstallation is now only allowed after disabling protection at the company level.

- **UI and General Improvements**
  - Implemented clustering of device markers in **Map widgets**.
  - Improved validation and error messages across many API endpoints.
  - Removed **Device Connected / Device Disconnected** events from auditing.
  - Numerous small UI improvements.

- **On-Premises**
  - Added a user-friendly way to add new router apps via the **Administrative Portal**.
  - Added an option to configure **password strictness requirements** for DMP users.
  - Added an option to **batch register devices from CSV**.
  - Added support for **StartTLS** mode in SMTP.



### Bug Fixes:

- **Dashboard & Widgets**
  - Fixed widgets breaking in certain situations after cloning a View.
  - Fixed widget order not being ordered correctly in new companies.
  - Fixed UI freezing during data reload if a Map widget contains a very high number of devices.

- **Desired Configuration**
  - Fixed pages getting stuck in a loading state in certain situations.
  - Fixed newly created config profiles not appearing until a page refresh.

- **VPN & Roadwarrior**
  - Fixed Roadwarrior configurations incorrectly containing IP addresses instead of DNS addresses, which required re-download after VPN hub restarts.
  - Fixed Roadwarrior descriptions not displaying on detail pages.
  - Fixed retry intervals sometimes being calculated incorrectly when resending messages to routers.

- **User & Company Management**
  - Fixed user deletion sometimes failing.
  - Fixed **UserDeleted** auditing record not being visible in user’s companies.
  - Fixed users being unable to leave a company without **RemoveUsers** permission.
  - Fixed company deletion failing if a child company had existed in the past.

- **API & Backend**
  - Fixed many cases where API endpoints returned generic **Internal Error** messages instead of more specific errors for invalid parameter combinations.

- **On-Premises**
  - Fixed error **413** when uploading large files via a VPN proxy link.
