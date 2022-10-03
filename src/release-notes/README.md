# 2.5.0: October 4, 2022

This release contains new features (2FA) and mainly improvements to the server architecture, so on-premise installation could be offered in one of the next releases.


### New Features

* Added an option to enable **2-Factor Authentication** (2FA) for a company. This can be enabled in the company edit dialog. Once 2FA is enabled for the company, the user in that company can set up the authentication app at login via QR code, or at the top right user menu. When 2FA is enabled, there is also an option to mark the user account as *Service Account* (at the user's permissions configuration), so the scripts can bypass 2FA. More information on 2FA can be found [here](https://docs.wadmp.com/explanations/2fa/).
![2FA](./2.5.0/2fa.png "2FA")

* Added support for storing and displaying the SIM ID (IMSI) if reported by the device (depends on the version of WebAccess/DMP Client). SIM ID is displayed on the device detail page.
![2FA](./2.5.0/sim-id.png "SIM ID")

* Added *Claimed Devices* number to the list of companies. It is now easier to see the number of company devices. If the company has sub-companies, there is also the overall number of devices including sub-companies.  
![2FA](./2.5.0/number-of-companies.png "Number of companies")

* Added the memory for filters and sorting config in the UI. All the filters/sorting on the *Devices* page is now remembered when navigating somewhere else. Same for most of the other pages containing filters/sorting. The switch of the list/card view was removed everywhere.
![2FA](./2.5.0/filters.png "Filters")

* Modified the change-password API endpoint (/management/devices/{macAddress}/commands/change-password) so the desired password can be set (random generated password was supported only). Now there are new optional parameters (user, password) for the endpoint.

* Added support of automatic update of WebAccess/DMP client. This is dependent on WebAccess/DMP client version (2.2.0 and higher). When an unsupported version of the client is detected by the server, it can be updated automatically.


### Improvements

* Changed architecture of backend server services, so they are running in **platform independent environment**. We were dependent on one cloud services provider, and now the server is cloud platform independent. This will enable the offer of an on-premise product version in one of the next releases. This change also made the app overall faster and ready for a bigger load. 

* Sorted Router Apps by status in Install dialog, so the installed apps are shown first and not installed apps after them.
![2FA](./2.5.0/install-ra.png "Install Router Apps")

* Changed Auditing Action Types at *Audit Logs* to more human-readable (added GET /auditing/action-types API endpoint), also unified naming to use past tense everywhere. Added Select All and Clear options for better usability when filtering Action Types.
![2FA](./2.5.0/action-types.png "Action Types")

* Made swagger API endpoints (documentation at [api.wadmp.com](https://api.wadmp.com)) displayed in alphabetical order.
  
* Updated billing email text so it matches the fact that billing overview and invoice are sent in separate emails.


### Bug Fixes 

* Fixed the Alert Rules were being triggered even when disabled in case they were created as enabled.

* Fixed Alert Endpoint change of email address was not applied. Now email can be changed in the Alert Endpoint.

* Fixed Sync engine was forcing the download of a pinned Router App over the app that was being currently installed. This could lead to a downgrade of the router app without a user prompt.

* Fixed repeatedly adding a Device to the same Device Group did not return any information notice that this device had already been in the group.
  
* Added missing redirects after the Save button back to the list page on several places in UI - when creating or editing items like Device Group, Settings Group, Alert Rule, and Alert Endpoint.

* Fixed completed playbooks with missing devices were displayed redundantly in playbooks. Now the Playbook won't show if all of its devices are missing.

* Fixed counting of Total device days for Billing. When a Device had multiple claims/releases in one day, the device days number was not correct when counting device days for a month during Billing.

* Fixed User Permissions edit behaved unpredictably in some cases. E. g. there was a false positive notification when the user removed himself from the company. He was not removed however the notification showed success. Now the user can remove himself from a company under some conditions. The permissions follow the rules mentioned in this [Permissions Explanation](https://docs.wadmp.com/explanations/permissions/).

* Made Page and Pagesize parameters optional for all API endpoints.

* Removed unused parameter in POST /management/settings-groups API endpoint.












