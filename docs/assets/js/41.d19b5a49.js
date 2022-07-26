(window.webpackJsonp=window.webpackJsonp||[]).push([[41],{572:function(e,t,a){"use strict";a.r(t);var i=a(35),r=Object(i.a)({},(function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("ContentSlotsDistributor",{attrs:{"slot-key":e.$parent.slotKey}},[a("h1",{attrs:{id:"_2-4-0-december-11-2021"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#_2-4-0-december-11-2021"}},[e._v("#")]),e._v(" 2.4.0: December 11, 2021")]),e._v(" "),a("h3",{attrs:{id:"user-interface"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#user-interface"}},[e._v("#")]),e._v(" User Interface")]),e._v(" "),a("h4",{attrs:{id:"features"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#features"}},[e._v("#")]),e._v(" Features:")]),e._v(" "),a("ul",[a("li",[a("p",[e._v("There is a new "),a("strong",[e._v("Alert")]),e._v(" feature available. Alerts allow users to observe specific parameters of a single device or a company and set notification triggers based on its values. The Alert feature is only available for Premium accounts.")])]),e._v(" "),a("li",[a("p",[e._v("The "),a("strong",[e._v("Auditing")]),e._v(" feature - gives Users the option to browse auditing events related to a single Device, Users, and the WADMP application. Complete Auditing records are available under the new menu item - Audit Logs. The Device logs are located on the Device page on the tab Audit Logs. The User-related records can be found on the “Audit Logs” tab in the Users section.")])]),e._v(" "),a("li",[a("p",[e._v("Added reboot button and upgrade firmware button for a single device (on the right on the device detail page):")])])]),e._v(" "),a("p",[a("img",{attrs:{src:"2.4.0_reboot_upgrade_delete.png",alt:"reboot upgrade delete",title:"reboot upgrade delete"}})]),e._v(" "),a("ul",[a("li",[e._v("As we now support device deletion, the icon to delete is shown at all times at the device (showed previously at unclaimed devices only).")])]),e._v(" "),a("h4",{attrs:{id:"improvements"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#improvements"}},[e._v("#")]),e._v(" Improvements:")]),e._v(" "),a("ul",[a("li",[a("p",[e._v('In login web, we removed the redundant "Remember Me" checkbox (this is enabled by default), allowed all special characters in the password and corrected some formatting.')])]),e._v(" "),a("li",[a("p",[e._v("User edit form was changed to on-page form (previously modal dialog) for better readability and usability. Also, the error placement was changed to a popup message.")])]),e._v(" "),a("li",[a("p",[e._v('Two state filters on the "My Devices" page (online/offline, claimed/unclaimed, in-sync) now have green color for positive selection, so it is clear what state they are in.')])]),e._v(" "),a("li",[a("p",[e._v("Added EULA and Privacy policy popup dialog to record user agreements.")])]),e._v(" "),a("li",[a("p",[e._v("Aggregated Router Apps were hidden from the installation menu (these apps will be installed automatically when the parent app is installed).")])]),e._v(" "),a("li",[a("p",[e._v("Added missing message about being empty to empty tag filter at devices.")])])]),e._v(" "),a("h4",{attrs:{id:"bugfixes"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#bugfixes"}},[e._v("#")]),e._v(" Bugfixes:")]),e._v(" "),a("ul",[a("li",[a("p",[e._v("Added missing Back button to Create new playbook form.")])]),e._v(" "),a("li",[a("p",[e._v("Fixed rendering of icons with initials for companies/users whose names contained spaces.")])]),e._v(" "),a("li",[a("p",[e._v("Added missing error message for incorrect Company Contact Email on the sign-up form.")])]),e._v(" "),a("li",[a("p",[e._v('Fixed "Value is not an integer" error at the device configuration that occurred in the situation when the router reported the value of ports in the NAT section.')])]),e._v(" "),a("li",[a("p",[e._v("Error message shown when saving an invalid device configuration is now more specific.")])])]),e._v(" "),a("hr"),e._v(" "),a("h3",{attrs:{id:"code-api"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#code-api"}},[e._v("#")]),e._v(" Code / API")]),e._v(" "),a("h4",{attrs:{id:"features-2"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#features-2"}},[e._v("#")]),e._v(" Features:")]),e._v(" "),a("ul",[a("li",[a("p",[e._v("Alerts feature has been implemented, including API endpoints.")])]),e._v(" "),a("li",[a("p",[e._v("Auditing API endpoints were merged into one that allows filtering by company, user, and device (in the previous version, only filtering by user or company was possible).")])]),e._v(" "),a("li",[a("p",[e._v("Moved auditing data to a more appropriate database to improve performance.")])]),e._v(" "),a("li",[a("p",[e._v("Device delete. It is now possible to delete a device (previously, devices could only be deleted if they had never been claimed before). Some information about deleted devices remains in the database for auditing purposes. It is possible to create a deleted device again.")])])]),e._v(" "),a("h4",{attrs:{id:"maintenace"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#maintenace"}},[e._v("#")]),e._v(" Maintenace:")]),e._v(" "),a("ul",[a("li",[e._v("Updated our database with monitoring data to the newest version.")])]),e._v(" "),a("h4",{attrs:{id:"bugfixes-2"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#bugfixes-2"}},[e._v("#")]),e._v(" Bugfixes:")]),e._v(" "),a("ul",[a("li",[a("p",[e._v("Fixed routers were getting out of sync due to the server not sending a particular message to the router in some situations.")])]),e._v(" "),a("li",[a("p",[e._v("Fixed server sometimes not reconnecting to MQTT brokers after its maintenance.")])]),e._v(" "),a("li",[a("p",[e._v("Fixed password check at sign-up/password change so all special characters can be used.")])]),e._v(" "),a("li",[a("p",[e._v("Fixed Playbook sometimes not shown as “running” for the first device of the device group where it was running.")])]),e._v(" "),a("li",[a("p",[e._v("Default value for devices with no temperature sensor was changed to -273 degrees Celsius from 0 degrees Celsius.")])]),e._v(" "),a("li",[a("p",[e._v("Fixed monitoring data not being available after re-claim of device.")])]),e._v(" "),a("li",[a("p",[e._v('Fixed error "Instance ID already in use" when installing Router App after the previous fail to install the same app.')])]),e._v(" "),a("li",[a("p",[e._v("Modified default parameters for several GET endpoints.")])]),e._v(" "),a("li",[a("p",[e._v("Fixed “InSync” status sometimes not updated after application (un)installation.")])]),e._v(" "),a("li",[a("p",[e._v('Fixed "/management/devices/{macAddress}/commands/trigger-bootstrap" API endpoint not returning 401 Not Authorized message when it should.')])]),e._v(" "),a("li",[a("p",[e._v("Fixed internal server error popup that was incorrectly shown when deleting a company (the company was correctly deleted, but the error was established).")])]),e._v(" "),a("li",[a("p",[e._v('Removed unused Family ID parameter from "/identity/device-families/{familyId}/device-types/{typeId}" API endpoint. This parameter was redundant and the API endpoint was changed to "/identity/device-families/device-types/{typeId}".')])])]),e._v(" "),a("hr"),e._v(" "),a("h3",{attrs:{id:"content"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#content"}},[e._v("#")]),e._v(" Content")]),e._v(" "),a("h4",{attrs:{id:"bugfixes-3"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#bugfixes-3"}},[e._v("#")]),e._v(" Bugfixes:")]),e._v(" "),a("ul",[a("li",[a("p",[e._v("Fixed Backup Routes firmware section on v2i routers.")])]),e._v(" "),a("li",[a("p",[e._v("Fixed USB Port model section at all firmware.")])])]),e._v(" "),a("hr"),e._v(" "),a("h3",{attrs:{id:"docs-wadmp-com"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#docs-wadmp-com"}},[e._v("#")]),e._v(" docs.wadmp.com")]),e._v(" "),a("ul",[a("li",[e._v("Added explanantion page: "),a("a",{attrs:{href:"https://docs.wadmp.com/explanations-discussions/alerts.html",target:"_blank",rel:"noopener noreferrer"}},[e._v("Alerts Explained"),a("OutboundLink")],1),e._v(".")]),e._v(" "),a("li",[e._v("Added explanantion page: "),a("a",{attrs:{href:"https://docs.wadmp.com/explanations-discussions/auditing.html",target:"_blank",rel:"noopener noreferrer"}},[e._v("Auditing Explained"),a("OutboundLink")],1),e._v(".")]),e._v(" "),a("li",[e._v("Added explanantion page: "),a("a",{attrs:{href:"https://docs.wadmp.com/explanations-discussions/grafana.html",target:"_blank",rel:"noopener noreferrer"}},[e._v("Grafana - Company Dashboard, Device Dashboard (Monitoring Data)"),a("OutboundLink")],1),e._v(".")])])])}),[],!1,null,null,null);t.default=r.exports}}]);