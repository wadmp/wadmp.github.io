(window.webpackJsonp=window.webpackJsonp||[]).push([[8],{511:function(e,t,a){e.exports=a.p+"assets/img/dmp-client1.ac321dd3.png"},512:function(e,t,a){e.exports=a.p+"assets/img/field-cat.e88f8779.png"},513:function(e,t,a){e.exports=a.p+"assets/img/data-device.35f6ec7d.png"},514:function(e,t,a){e.exports=a.p+"assets/img/data-dash.e77b6bbc.png"},515:function(e,t,a){e.exports=a.p+"assets/img/ping.19f97ac5.png"},516:function(e,t,a){e.exports=a.p+"assets/img/ping-device.b7f482a7.png"},517:function(e,t,a){e.exports=a.p+"assets/img/ping-dash.9284a663.png"},518:function(e,t,a){e.exports=a.p+"assets/img/cust-reportable.96f19937.png"},519:function(e,t,a){e.exports=a.p+"assets/img/avg-speed-add-chart.addeb5d9.png"},520:function(e,t,a){e.exports=a.p+"assets/img/avg-speed-cust-no.37a4f89c.png"},521:function(e,t,a){e.exports=a.p+"assets/img/mwan1.98020449.png"},522:function(e,t,a){e.exports=a.p+"assets/img/mwan2.e267ebae.png"},523:function(e,t,a){e.exports=a.p+"assets/img/mwan3.6927a491.png"},524:function(e,t,a){e.exports=a.p+"assets/img/mwan4.9a26e56f.png"},525:function(e,t,a){e.exports=a.p+"assets/img/mwan5.98add92e.png"},526:function(e,t,a){e.exports=a.p+"assets/img/mwan6.ea5ce1d5.png"},707:function(e,t,a){"use strict";a.r(t);var n=a(11),i=Object(n.a)({},(function(){var e=this,t=e._self._c;return t("ContentSlotsDistributor",{attrs:{"slot-key":e.$parent.slotKey}},[t("h2",{attrs:{id:"collecting-data-from-routers"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#collecting-data-from-routers"}},[e._v("#")]),e._v(" Collecting Data from Routers")]),e._v(" "),t("p",[e._v("In the the WebAccess/DMP Client router app, the “Enable Monitoring” checkbox must be checked (default state is checked) in order to collect data from the device. Note the “Monitoring Interval” (default is 15 minutes).")]),e._v(" "),t("p",[t("img",{attrs:{src:a(511),alt:"Client monitoring interval"}})]),e._v(" "),t("p",[e._v("You may disable WebAccess/DMP monitoring on a device, when disable the checkbox, and press apply. Similarly, you may leave monitoring enabled but adjust the monitoring interval.")]),e._v(" "),t("p",[e._v("Note that monitoring interval may affect your cellular data bill (more often - more data sent in long time interval).\nAmount of data sent in every regular message is affected by Fields configured for your company. This may also affect your cellular data bill - see example below.")]),e._v(" "),t("p",[e._v("Fields have different categories you can filter, but monitoring (representation in Stats, Charts, Tables) can be generally done above all types of Fields, including Configuration.")]),e._v(" "),t("p",[e._v("Adding a Field means it is tracked in the database, and some fields may take more cellular data when reported.")]),e._v(" "),t("p",[t("img",{attrs:{src:a(512),alt:"CSV export"}})]),e._v(" "),t("h3",{attrs:{id:"how-device-data-reporting-works"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#how-device-data-reporting-works"}},[e._v("#")]),e._v(" How Device Data Reporting Works")]),e._v(" "),t("p",[e._v("The basic principle of operation is that the WebAccess/DMP client maintains a TCP connection with the WebAccess/DMP management server. This means the device is always connected, so the user can reach the device immediately, as required.")]),e._v(" "),t("p",[e._v('However, there is a cost associated with maintaining this always-on TCP connection. Packets of data must be sent periodically to maintain the connection. In addition, for most of our customers, the device connects to WebAccess/DMP via cellular. This means that the cellular network provider (or "carrier") charges for all data exchanged, even if it is only TCP "keepalive" data and not "application" data.')]),e._v(" "),t("p",[e._v("The amount of data consumed is based on the type of the used Field. You can set Reporting behaviour for some Fields (Always, Never, On Change with Treshold). For examples on how much data are used by some actions, check the "),t("RouterLink",{attrs:{to:"/gen3/docs/faq/"}},[e._v("FAQ")]),e._v(" section.")],1),e._v(" "),t("h3",{attrs:{id:"example-monitoring-cellular-data-usage"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#example-monitoring-cellular-data-usage"}},[e._v("#")]),e._v(" Example: Monitoring Cellular Data Usage")]),e._v(" "),t("p",[e._v("For example you can observe the actual cellular data usage on the Monitoring tab of the device like this, after you make visible Data Up+Down Field in the Table (click on eye icon), and add charts for Data Up+Down Field. See "),t("RouterLink",{attrs:{to:"/gen3/docs/dashboards-widgets/"}},[e._v("Dashboards & Widgets")]),e._v(" for more information on how to work with widgets and table.")],1),e._v(" "),t("p",[t("img",{attrs:{src:a(513),alt:"CSV export"}})]),e._v(" "),t("p",[e._v("Similarly you can observe data for devices from the company on the main dashboard like this - here Company Stat for Max aggregation Data Up+Down Field and adding of Line Chart, where you can add more fields of same type with different aggreation to the same chart (e.g. show Max and Average in same chart).")]),e._v(" "),t("p",[t("img",{attrs:{src:a(514),alt:"CSV export"}})]),e._v(" "),t("h3",{attrs:{id:"ping-status-ping-latency"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#ping-status-ping-latency"}},[e._v("#")]),e._v(" Ping Status & Ping Latency")]),e._v(" "),t("p",[e._v("These Fields can be used for monitoring of connection to specified IP address. Provide IP Address when creating the Field:")]),e._v(" "),t("p",[t("img",{attrs:{src:a(515),alt:"CSV export"}})]),e._v(" "),t("ul",[t("li",[t("strong",[e._v("Ping Status")]),e._v(" - True/False value indicating whether ping to some predefined address succeeded.")]),e._v(" "),t("li",[t("strong",[e._v("Ping Latency")]),e._v(" - Latency (in miliseconds) when pinging a predefined address.")])]),e._v(" "),t("p",[e._v("Reported monitoring data may be used in Widgets (Stats or Charts) or in the devices Table on dashboards.\nExample of ping Fields made visible in Table and added as Line Charts on Device Monitoring tab:")]),e._v(" "),t("p",[t("img",{attrs:{src:a(516),alt:"CSV export"}})]),e._v(" "),t("p",[e._v("Example of ping Fields made visible in Table on company dashboard, Ping Latency added as Company Stat and Ping Status added as Pie Chart:")]),e._v(" "),t("p",[t("img",{attrs:{src:a(517),alt:"CSV export"}})]),e._v(" "),t("h3",{attrs:{id:"custom-reportable-string-custom-reportable-number"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#custom-reportable-string-custom-reportable-number"}},[e._v("#")]),e._v(" Custom Reportable String & Custom Reportable Number")]),e._v(" "),t("p",[e._v("These Fields can be programmaticaly connected to any customer desired string or number to be reported from device, e.g. via Script.")]),e._v(" "),t("ul",[t("li",[t("p",[t("strong",[e._v("Custom Reportable String")]),e._v(" is up to 40 characters long string stored in a local file on router that is reported. Files are located in /var/data/wadmp_client/custom_metrics/custom_str1 to custom_str5. Up to 5 custom strings can be added.")])]),e._v(" "),t("li",[t("p",[t("strong",[e._v("Custom Reportable Number")]),e._v(" is a number stored in a local file on router that is reported. Files are located in /var/data/wadmp_client/custom_metrics/custom_number1 to custom_number5. Up to 5 custom numbers can be added.")])])]),e._v(" "),t("p",[t("img",{attrs:{src:a(518),alt:"CSV export"}})]),e._v(" "),t("p",[t("strong",[e._v("Note:")]),e._v(" Only "),t("em",[e._v("Custom Reportable Number")]),e._v(" Field can be used for charts (string data type can not be shown in charts).")]),e._v(" "),t("p",[e._v("Custom Fields can be used also with a sensor connected to the router (via RS232/485, binary I/O or other industrial interface). E.g. If a flow meter in a tube would be connected, a script would exist in a device, that would write the value from the sensor to a file, the value could then be reported to WebAccess/DMP and could be presented as data in Stats, Charts, or Tables, exported or used for Alerts.")]),e._v(" "),t("h4",{attrs:{id:"download-speed-reporting-example-of-the-script-using-custom-reportable-number"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#download-speed-reporting-example-of-the-script-using-custom-reportable-number"}},[e._v("#")]),e._v(" Download Speed Reporting - Example of the Script Using Custom Reportable Number")]),e._v(" "),t("ul",[t("li",[e._v("Add this code as Startup Script (e. g. in Device Configuration):")])]),e._v(" "),t("div",{staticClass:"language- extra-class"},[t("pre",{pre:!0,attrs:{class:"language-text"}},[t("code",[e._v('#!/bin/sh\n# -----------------------------------------------------------------------------\n# Initialization Script\n# -----------------------------------------------------------------------------\n# This script will run *after* all other init scripts and is intended to set up\n# a custom metric collection script that downloads a file and logs download speed.\n# -----------------------------------------------------------------------------\n\n# -----------------------------------------------------------------------------\n# Create the metric collection script\n# -----------------------------------------------------------------------------\ncat << \'EOF\' > /var/scripts/script.sh\n#!/bin/bash\n\n# URL of the file to be downloaded\nurl="http://ipv4.download.thinkbroadband.com/10MB.zip"\n\n# Define the directory and file path for storing metrics\ndir_path="/var/data/wadmp_client/custom_metrics"\nfile_path="$dir_path/custom_number1"\n\n# -----------------------------------------------------------------------------\n# Ensure the required directory and file exist\n# -----------------------------------------------------------------------------\n# Check if the directory exists; if not, create it\nif [ ! -d "$dir_path" ]; then\n    mkdir -p "$dir_path"\nfi\n\n# Check if the file exists; if not, create it\nif [ ! -f "$file_path" ]; then\n    touch "$file_path"\nfi\n\n# -----------------------------------------------------------------------------\n# Download the file and measure download speed\n# -----------------------------------------------------------------------------\necho "Downloading 10MB file..."\n\n# Perform the download and capture the average download speed in bytes/sec\nspeed_bytes=$(curl -o /dev/null --silent --write-out "%{speed_download}" "$url")\n\n# Verify if a valid speed value was captured\nif [[ -z "$speed_bytes" ]]; then\n  echo "Error: Speed not found in response"\n  exit 1\nfi\n\n# Convert the speed from bytes/sec to megabytes/sec\nmbps=$(awk "BEGIN {printf \\"%.2f\\", $speed_bytes / 1024 / 1024}")\n\n# Output the download speed in MBps\necho "Average download speed: $mbps MBps"\n\n# Write the download speed to the specified file\necho "$mbps" > "$file_path"\nEOF\n\n# -----------------------------------------------------------------------------\n# Make the script executable\n# -----------------------------------------------------------------------------\nchmod +x /var/scripts/script.sh\n\n# -----------------------------------------------------------------------------\n# Schedule the script to run daily using cron\n# -----------------------------------------------------------------------------\n# Append the script to the root crontab to execute at midnight daily\necho "0 0 * * * root /var/scripts/script.sh" >> /etc/crontab\n\n# -----------------------------------------------------------------------------\n# Ensure the cron service is started\n# -----------------------------------------------------------------------------\nservice cron start\n\n')])])]),t("ul",[t("li",[t("p",[e._v("To show the number on Dashboard (column in table, Stat or Chart), ensure that the Field "),t("em",[e._v("Custom Reportable Number")]),e._v(" is added. If using more Custom Reportable fields, ensure that the path shown in the description is same as the file_path in the script (custom_number1).")])]),e._v(" "),t("li",[t("p",[e._v("To add chart, in this case select Line Chart, and select "),t("em",[e._v("Custom Reportable Number")]),e._v(" Field:")])])]),e._v(" "),t("p",[t("img",{attrs:{src:a(519),alt:"CSV export"}})]),e._v(" "),t("ul",[t("li",[e._v("The chart then may look like this:")])]),e._v(" "),t("p",[t("img",{attrs:{src:a(520),alt:"CSV export"}})]),e._v(" "),t("h4",{attrs:{id:"mwan-interface-reporting-example-of-the-script-using-custom-reportable-string"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#mwan-interface-reporting-example-of-the-script-using-custom-reportable-string"}},[e._v("#")]),e._v(" MWAN Interface Reporting - Example of the Script Using Custom Reportable String")]),e._v(" "),t("p",[e._v("Follow this tutorial on how to get the MWAN interface into the WADMP3 table:")]),e._v(" "),t("ul",[t("li",[e._v("First create custom reportable string field like this:")])]),e._v(" "),t("p",[t("img",{attrs:{src:a(521),alt:"MWAN"}})]),e._v(" "),t("p",[t("img",{attrs:{src:a(522),alt:"MWAN"}})]),e._v(" "),t("ul",[t("li",[e._v("And then show it in table:")])]),e._v(" "),t("p",[t("img",{attrs:{src:a(523),alt:"MWAN"}})]),e._v(" "),t("ul",[t("li",[e._v("After this step you would need to apply this Startup Script (below) to the Routers where you would like to read the WAN interface from:")])]),e._v(" "),t("p",[t("img",{attrs:{src:a(524),alt:"MWAN"}})]),e._v(" "),t("div",{staticClass:"language- extra-class"},[t("pre",{pre:!0,attrs:{class:"language-text"}},[t("code",[e._v('#!/bin/sh\n# -----------------------------------------------------------------------------\n# Initialization Script\n# -----------------------------------------------------------------------------\n# This script will run *after* all other init scripts and is intended to set up\n# a custom metric collection script that logs the primary network interface.\n# -----------------------------------------------------------------------------\n\n# -----------------------------------------------------------------------------\n# Create the metric collection script\n# -----------------------------------------------------------------------------\ncat << \'EOF\' > /var/scripts/script.sh\n#!/bin/bash\n\n# Define the directory and file path for storing metrics\ndir_path="/var/data/wadmp_client/custom_metrics"\nfile_path="$dir_path/custom_str1"\n\n# -----------------------------------------------------------------------------\n# Ensure the required directory and file exist\n# -----------------------------------------------------------------------------\n# Check if the directory exists; if not, create it\nif [ ! -d "$dir_path" ]; then\n    mkdir -p "$dir_path"\nfi\n\n# Check if the file exists; if not, create it\nif [ ! -f "$file_path" ]; then\n    touch "$file_path"\nfi\n\n# -----------------------------------------------------------------------------\n# Retrieve the primary network interface\n# -----------------------------------------------------------------------------\ninterface=$(ip route show | awk \'/default/ {print $NF}\')\n\n# Verify if a valid interface was found\nif [[ -z "$interface" ]]; then\n  echo "No interface" > "$file_path"\n  exit 1\nfi\n\n# Output the network interface name\necho "Primary network interface: $interface"\n\n# Write the interface name to the specified file\necho "$interface" > "$file_path"\nEOF\n\n# -----------------------------------------------------------------------------\n# Make the script executable\n# -----------------------------------------------------------------------------\nchmod +x /var/scripts/script.sh\n\n# -----------------------------------------------------------------------------\n# Schedule the script to run daily using cron\n# -----------------------------------------------------------------------------\n# Append the script to the root crontab to execute at midnight daily\necho "* * * * * root /var/scripts/script.sh" >> /etc/crontab\n\n# -----------------------------------------------------------------------------\n# Ensure the cron service is started\n# -----------------------------------------------------------------------------\nservice cron start\n\n')])])]),t("ul",[t("li",[t("p",[e._v("And also set the WADMP3 Client monitoring interval to 1 minute to achieve the fastest reporting of the change of the WAN interface:\n"),t("img",{attrs:{src:a(525),alt:"MWAN"}})])]),e._v(" "),t("li",[t("p",[e._v("After this step you would need to reboot the Router and after reboot you should be able to see the WAN interface in the WADMP3:\n"),t("img",{attrs:{src:a(526),alt:"MWAN"}})])]),e._v(" "),t("li",[t("p",[e._v("If this solution is suitable for you, you can create the configuration profile from the Router and distribute it to the other routers if needed.")])])])])}),[],!1,null,null,null);t.default=i.exports}}]);