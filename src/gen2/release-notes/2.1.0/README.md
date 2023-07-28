# 2.1.0: 9th April 2020

This release was mainly for bug fixes. However, there were also minor changes to the public API.

### User Interface

* Bugfix: GPS location was not displayed on the map correctly.
* Bugfix: GPS locations on the map are now clustered automatically.
* Bugfix: Settings icon restored.
* Bugfix: Monitoring data would not display if the company name contained special characters.
* Bugfix: Ignore sections with no model for unknown apps.
* Bugfix: In the Users view, Search now includes company names.
* Bugfix: Reset New User modal when closed.
* Disable permissions the user can't edit.

### Code

* Bugfix: SNMP messages were getting lost.
* Bugfix: Devices were sometimes reported as “offline” when “online”.
* Bugfix: Added SNMP support for ICR-1601 routers with A8 firmware.
* Bugfix: Use UTC time for all Monitoring data.
* Bugfix: Race condition in sync application versions.
* Changed default User permissions to include “Edit Companies”.
* REST API change: “GET users” has a new optional “search” parameter.
* REST API change: “default_user_permissions” are no longer included in a license model.
* Bugfix: Support applications with only two characters in their name. For example, the “Midnight Commander” user module is named “mc” on the router’s file system. This User Module was causing devices never to sync.
* Minor typos fixed in the License endpoint.

### Content

* New version of the WA/DMP Client User Module: 2.0.3

### docs.wadmp.com

* Updated Jupyter Notebook “create_licence.ipynb” to match the change in REST API.