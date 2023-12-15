(window.webpackJsonp=window.webpackJsonp||[]).push([[19],{278:function(e,t,i){e.exports=i.p+"assets/img/desired-reported.fad86348.png"},279:function(e,t,i){e.exports=i.p+"assets/img/device-configuration.edc80b46.png"},280:function(e,t,i){e.exports=i.p+"assets/img/desired-reported-endpoints.b6311902.png"},281:function(e,t,i){e.exports=i.p+"assets/img/device-configuration-api.5d94501b.png"},282:function(e,t,i){e.exports=i.p+"assets/img/sync-engine-endpoints.761d5c0e.png"},283:function(e,t,i){e.exports=i.p+"assets/img/sync-engine-parameters.b4980e97.png"},552:function(e,t,i){"use strict";i.r(t);var n=i(10),o=Object(n.a)({},(function(){var e=this,t=e._self._c;return t("ContentSlotsDistributor",{attrs:{"slot-key":e.$parent.slotKey}},[t("h1",{attrs:{id:"device-desired-and-reported-states"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#device-desired-and-reported-states"}},[e._v("#")]),e._v(" Device Desired and Reported states")]),e._v(" "),t("p",[e._v("To configure a device, you need access to it, either to its web server or through SSH. When connected to a device, all changes made are immediately applied, and, if needed, services are restarted.")]),e._v(" "),t("p",[e._v("Remote device configuration, on the other hand, is a different business. It adds a second actor that can receive configuration changes and send them to the device. This raises new issues: Will this actor save a copy of all the properties or request them to the device every time? What if the device is temporarily not available? These and other questions are addressed by the solution DMP implemented. Desired and Reported states are not a new idea, especially now that cloud management of IoT devices is increasingly popular. We took pictures from other solutions but aimed to make ours lightweight and straightforward.")]),e._v(" "),t("p",[e._v("If you are curious about the ideas behind them, please visit the documentation for the following projects:")]),e._v(" "),t("ul",[t("li",[t("a",{attrs:{href:"https://aws.amazon.com/iot-platform/how-it-works/",target:"_blank",rel:"noopener noreferrer"}},[e._v("AWS IoT"),t("OutboundLink")],1),e._v(" and its implementation of "),t("a",{attrs:{href:"http://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-shadows.html",target:"_blank",rel:"noopener noreferrer"}},[e._v("Device Shadows"),t("OutboundLink")],1)]),e._v(" "),t("li",[t("a",{attrs:{href:"https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-what-is-iot-hub",target:"_blank",rel:"noopener noreferrer"}},[e._v("Azure IoT"),t("OutboundLink")],1),e._v(" and the similar "),t("a",{attrs:{href:"https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-device-twins",target:"_blank",rel:"noopener noreferrer"}},[e._v("Device Twins"),t("OutboundLink")],1),e._v(" "),t("a",{attrs:{href:"https://www.eclipse.org/ditto/intro-overview.html",target:"_blank",rel:"noopener noreferrer"}},[e._v("Eclipse Ditto"),t("OutboundLink")],1),e._v(" also provides a similar solution.")])]),e._v(" "),t("h2",{attrs:{id:"how-it-works"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#how-it-works"}},[e._v("#")]),e._v(" How It Works")]),e._v(" "),t("p",[t("img",{attrs:{src:i(278),alt:"Desired Reported",title:"Desired and Reported states"}})]),e._v(" "),t("p",[e._v("DMP defines two sets of configuration:")]),e._v(" "),t("ul",[t("li",[e._v("The Desired state or changes a user wants to make on a device and")]),e._v(" "),t("li",[e._v("The Reported state, the configuration the device reports to DMP")])]),e._v(" "),t("p",[e._v("In this model, the user can only modify the Desired state, while the Reported is only by the device. DMP is in charge of sending the difference between the two to the device, so eventually, both Desired and Reported are the same. Devices are the source of truth, so the Desired state has to be updated at any change so DMP can make correct decisions.")]),e._v(" "),t("p",[e._v("Two things are implied in this explanation:\nThe device needs a process capable of monitoring changes to report them and also be able to apply modifications received from DMP.\nDMP also needs to be able to send changes to the device, possibly waiting for the device to connect.\nIf the device doesn't apply the changes, DMP should be able to re-apply them.")]),e._v(" "),t("h3",{attrs:{id:"dmp-client"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#dmp-client"}},[e._v("#")]),e._v(" DMP Client")]),e._v(" "),t("p",[e._v("Routers allow extensibility through "),t("RouterLink",{attrs:{to:"/references/routers-overview.html"}},[e._v("Router Apps")]),e._v('. We created the "WebAccess/DMP client" Router App to be the service that updates DMP when the router changes and applies all changes sent by DMP, among other tasks. It maintains a connection with DMP using the '),t("RouterLink",{attrs:{to:"/explanations-discussions/what-is-webaccess-dmp.html"}},[e._v("MQTT protocol")]),e._v(" so changes on both sides can be reported to the other end.")],1),e._v(" "),t("p",[e._v("Because the router is the source of truth when this client connects, it reports all its configurations. This allows DMP to have a detailed report of all the changes when the device was disconnected.")]),e._v(" "),t("p",[e._v("Configuration on routers is naturally separated into sections, so we take advantage of it by sending to DMP all the properties of that section only. This allows for less information exchanged and is a practical difference from the other similar solutions.")]),e._v(" "),t("p",[e._v("The client knows where the changes need to be applied and what extra steps need to be taken. When finished, it reports back the changed configuration.")]),e._v(" "),t("h3",{attrs:{id:"applying-configuration-changes"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#applying-configuration-changes"}},[e._v("#")]),e._v(" Applying Configuration Changes")]),e._v(" "),t("p",[e._v("Every time the Desired state is changed, DMP will determine the difference with the reported state and send it to the device. If the device is online, it will receive the change immediately, but if it is offline, all subsequent changes will be merged into the Desired state. When the device connects again, it will receive only one change request per section modified.\nThis behavior has a downside. For example, if a user wants to apply a set of changes, wait or request a reboot, and then use other modifications to the same section while the device is offline, all changes will be merged into one request only. In this exceptional scenario, the user should wait for the device to reboot before applying the second set of changes.")]),e._v(" "),t("h3",{attrs:{id:"everything-is-an-application"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#everything-is-an-application"}},[e._v("#")]),e._v(" Everything is an Application")]),e._v(" "),t("p",[e._v("DMP treats both Firmware and Router Apps as applications. An application is a versioned set of properties grouped in sections. It can be replaced by a different version that may have a different set of properties. The Firmware is still a unique application because it is related to the device type and cannot be uninstalled.\nThis simplification allows to use of Desired and Reported states in all applications.")]),e._v(" "),t("h2",{attrs:{id:"how-to-use-desired-and-reported-states"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#how-to-use-desired-and-reported-states"}},[e._v("#")]),e._v(" How to Use Desired and Reported States")]),e._v(" "),t("p",[e._v("DMP groups all properties into sections. The DMP UI reflects this on the left column of the configuration screen:\n"),t("img",{attrs:{src:i(279),alt:"Device configuration",title:"UI Device configuration"}}),e._v('\nThe desired value always takes priority in the UI. The reported is shown only if it is different from the reported (like the "Name" property above, that was changed but not saved) or if there is no desired value. This simplified view allows focusing on what the user wants to change, showing details about the reported data only when relevant.')]),e._v(" "),t("p",[e._v("On the other hand, the API exposes all values to the user, processing and presenting them more appropriately. Moreover, the API allows a user more control over the presentation as the way to do it is not imposed by DMP.")]),e._v(" "),t("p",[e._v("The following endpoints are the ones that allow us to interact with Desired and Reported states:\n"),t("img",{attrs:{src:i(280),alt:"Desired Reported endpoints",title:"Desired and Reported endpoints"}})]),e._v(" "),t("p",[e._v("For example, the image of the UI above called the following endpoint to get the Desired and Reported states for the SNMP section :\n"),t("img",{attrs:{src:i(281),alt:"Device Desired and Reported through the API",title:"API Device configuration"}})]),e._v(" "),t("h3",{attrs:{id:"re-applying-configuration-with-syncengine"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#re-applying-configuration-with-syncengine"}},[e._v("#")]),e._v(" Re-Applying Configuration With SyncEngine")]),e._v(" "),t("p",[e._v("When a user applies a configuration change, DMP will send it to the device immediately or as soon as the device connects. However, if the device does not use the difference, DMP needs to re-apply the changes configured previously by the user. This is the job of SyncEngine.")]),e._v(" "),t("p",[e._v("SyncEngine is an active agent in DMP in charge of detecting not applied differences in all devices and re-applying them following the policy set for the company to which the device belongs.")]),e._v(" "),t("p",[e._v("This is how the SyncEngine can be configured:\n"),t("img",{attrs:{src:i(282),alt:"SyncEngine",title:"SyncEngine"}}),e._v(" "),t("img",{attrs:{src:i(283),alt:"SyncEngine parameters",title:"SyncEngine parameters"}})]),e._v(" "),t("p",[e._v('Sync Type "Never" disables the SyncEngine for the company. "Forever" will keep re-applying every "retry_interval" seconds until the device reports changes were applied. The custom mode will retry "retry_attempts" times.')]),e._v(" "),t("p",[e._v("When installing or removing applications, SyncEngine also supervises the change following the company's policy. In addition, SyncEngine will ensure an application is changed, retrying if needed.")])])}),[],!1,null,null,null);t.default=o.exports}}]);