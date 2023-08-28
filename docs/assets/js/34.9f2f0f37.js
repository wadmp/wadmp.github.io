(window.webpackJsonp=window.webpackJsonp||[]).push([[34],{437:function(e,t,a){e.exports=a.p+"assets/img/traffic_usage.d28932ed.png"},438:function(e,t,a){e.exports=a.p+"assets/img/device-dashboard.ab462f36.png"},439:function(e,t,a){e.exports=a.p+"assets/img/client_config.6806b209.png"},580:function(e,t,a){"use strict";a.r(t);var i=a(10),n=Object(i.a)({},(function(){var e=this,t=e._self._c;return t("ContentSlotsDistributor",{attrs:{"slot-key":e.$parent.slotKey}},[t("h1",{attrs:{id:"cellular-data-usage"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#cellular-data-usage"}},[e._v("#")]),e._v(" Cellular Data Usage")]),e._v(" "),t("h2",{attrs:{id:"introduction"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#introduction"}},[e._v("#")]),e._v(" Introduction")]),e._v(" "),t("p",[e._v("WebAccess/DMP requires every device to have the "),t("a",{attrs:{href:"https://ep.advantech-bb.cz/products/software/user-modules#webaccessdmp-client",target:"_blank",rel:"noopener noreferrer"}},[e._v("WebAccess/DMP Client"),t("OutboundLink")],1),e._v(" Router App installed.")]),e._v(" "),t("p",[e._v("The basic principle of operation is that the WebAccess/DMP client maintains a TCP connection with the WebAccess/DMP management server.\nThis means that the device is "),t("em",[e._v("always connected")]),e._v(", and therefore the user can reach the device immediately, as required.")]),e._v(" "),t("p",[e._v('However, there is a cost associated with maintaining this always-on TCP connection.\nPackets of data must be sent periodically to maintain the connection.\nIn addition, for most of our customers, the device connects to WebAccess/DMP via cellular.\nThis means that the cellular network provider (or "carrier") charges for all data exchanged: even if it is only TCP "keepalive" data and not "application" data.')]),e._v(" "),t("h2",{attrs:{id:"summary"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#summary"}},[e._v("#")]),e._v(" Summary")]),e._v(" "),t("p",[e._v("The amount of data consumed is based on the type of the used Field, you can check the Traffic Usage of individual fields in the Fields section.")]),e._v(" "),t("p",[t("img",{attrs:{src:a(437),alt:"Traffic Usage",title:"Traffic Usage"}})]),e._v(" "),t("h2",{attrs:{id:"monitoring-cellular-data-usage-on-device"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#monitoring-cellular-data-usage-on-device"}},[e._v("#")]),e._v(" Monitoring Cellular Data Usage on Device")]),e._v(" "),t("ul",[t("li",[e._v("If monitoring is enabled in the WebAccess/DMP client on a device, you can observe the "),t("em",[e._v("actual")]),e._v(" cellular data usage on the Monitoring tab of the device: On this example you can see 2 graphs with average Download / Upload in MB in the past 21 hours.\nThe default time interval in these views is 24 hours, but only If your device has been UP for at least that time.")])]),e._v(" "),t("p",[t("img",{attrs:{src:a(438),alt:"Device Dashboard",title:"Device Dashboard"}})]),e._v(" "),t("ul",[t("li",[e._v('To disable WebAccess/DMP monitoring on a device, you can re-configure the WebAccess/DMP Router App via its local web server or via WebAccess/DMP itself. First, from the WebAccess/DMP UI, activate the "toggle" beside the "Enable Monitoring" checkbox, then unclick the checkbox and Submit:')])]),e._v(" "),t("p",[t("img",{attrs:{src:a(439),alt:"alt text",title:"WebAccess/DMP Client configuration options"}})]),e._v(" "),t("ul",[t("li",[e._v("Similarly, you may also decide to leave monitoring enabled but adjust the monitoring interval.\nPlease be aware of this impact on your cellular data bill.")])]),e._v(" "),t("h2",{attrs:{id:"further-details"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#further-details"}},[e._v("#")]),e._v(" Further details")]),e._v(" "),t("ul",[t("li",[t("p",[e._v("The most significant factor that leads to the data usage figures above is the transport keepalive interval we use in the WebAccess/DMP Client Router App.\nThis is hard-coded to be 60 seconds (1 minute). This may seem aggressive, but we have encountered cellular operators with VERY short timeouts on their networks. Of the order of 2 minutes!")])]),e._v(" "),t("li",[t("p",[e._v('The Configuration manual for your device has a section on the "Check Connection" feature, which is part of the Mobile WAN configuration.\nIt states unequivocally:')])])]),e._v(" "),t("blockquote",[t("p",[e._v("Enabling the Check Connection function for mobile networks is necessary for the uninterrupted and continuous operation of the router.")])]),e._v(" "),t("ul",[t("li",[t("p",[e._v("This advice still applies to any device using WebAccess/DMP, "),t("em",[e._v('but the "Enable Traffic Monitoring" item should also be enabled.')]),e._v('\nThe device will monitor all traffic on the cellular interface and only send ping requests if the selected Ping Interval is less than the WebAccess/DMP keepalive interval (60 seconds).\nIf you do not "Enable Traffic Monitoring", the device will send periodic ping requests to check the cellular connection. This will add to your cellular data usage.')])]),e._v(" "),t("li",[t("p",[e._v("The data usage figures given above are correct for steady-state operation. i.e., The device has already connected to the WebAccess/DMP Management Server.\nIf your device's cellular connection is unstable (for example, due to poor signal strength), you may experience occasional re-connects.\nEach re-connection involves several data transfers:")]),e._v(" "),t("ul",[t("li",[e._v("TLS handshake = approximately 5kB, due to the exchange of X.509 certificates;")]),e._v(" "),t("li",[e._v("configuration re-synchronization = approximately 150kB, depending on the number of Router Apps installed and the content of the configuration data.")])])]),e._v(" "),t("li",[t("p",[e._v("When a user actively manages a device via WebAccess/DMP, the overall data usage figures will depend on the exact actions performed.\nFor example:")]),e._v(" "),t("ul",[t("li",[e._v("Firmware upgrade = approximately 14MB, depending on the exact device type and firmware version;")]),e._v(" "),t("li",[e._v("Router App installation or upgrade = anything from 30kB for a small app such as Pinger to 6MB for a large app such as Python;")]),e._v(" "),t("li",[e._v("Re-configuration = varies, depending on the section or sections being re-configured and the content of the configuration data.")])])]),e._v(" "),t("li",[t("p",[e._v('In this article, we are using the traditional base-10 (aka "decimal" or "SI") prefixes for digital data. i.e. 1000B = 1kB, 1000kB = 1MB, etc. The difference to base-2 (aka "binary" or "IEC") is 2.4%. However '),t("strong",[e._v("on WebAccess/DMP we always use base-2 (1024) counted data units!")]),e._v(" It is to maintain unification with our routers, where we use the customary practice of base-2 counts and B, KB, MB, GB units. To sum up: On WebAccess/DMP may occur, both types of units B, KB, MB, ... and B, KiB, MiB, ... but they always use the base-2 (1024) count.")])])])])}),[],!1,null,null,null);t.default=n.exports}}]);