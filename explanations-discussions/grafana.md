# Grafana - Company Dashboard, Device Dashboard

## WebAccess/DMP Client - Enable Monitoring

When a router has the “WebAccess/DMP Client” User Module installed, the client may optionally be configured to send monitoring data to the server. The data is displayed with Grafana. Grafana is used in WADMP on two places: Home Dashboard → Company Dashboard and individual Device Dashboard.

On the WADMP client the “Enable Monitoring” checkbox must be checked (the default is yes) and note the “Monitoring Interval”.

![WebAccess/DMP Client](/images/explanations-discussions/grafana/01client.png "WebAccess/DMP Client")


&nbsp;    
&nbsp; 
## Company Dashboard

When there are some online devices for the selected company you should see aggregated company data like this:

![Company Dashboard with data](/images/explanations-discussions/grafana/02compdash.png "Company Dashboard with data")

![Company Dashboard with data](/images/explanations-discussions/grafana/03compdash.png "Company Dashboard with data")

When there is not any online device, the dashboard looks like this:

![Company Dashboard with no data](/images/explanations-discussions/grafana/04compdashempty.png "Company Dashboard with no data")

&nbsp;    
&nbsp; 
### Description of individual graphs

|        Name of graph         |  Trap Attribute  |  Description       |
| :--------------------------  | :--------------- | :----------------- |
| Connection Status | is_online |Indicates if the WA/DMP Client User Module in the devices is connected to the WebAccess/DMP server.|
| Device Type | deviceType | The exact router device type, which also identifies the name of the firmware used.|
| Cellular Connection Type | mobileTechnology | A string identifying the type of cellular connection used. Supported values:<br>"N/A"<br> "GPRS"<br>"EDGE"<br>"UMTS"<br>"HSDPA"<br>"HSUPA"<br>"HSPA+"<br>"LTE"<br>"CDMA"<br>"EV-DO"<br>"EV-DO Rel. 0"<br>"EV-DO Rev. A"<br>"EV-DO Rev. B"|
|Cellular Download | ifInOctets | The total number of octets (bytes) received on the first Mobile WAN interface. This is a counter that is reset when the device is rebooted or the network interface is restarted. |
| Connectivity History | is_online | Shows history of online devices |
| Devices | firmwareVersion | Firmware ver. - last reported firmware version |
|  | is_online | Online - shows last status of the device |
|  | deviceType | Device Type - last reported device type. |
|  | ifInOctets | Down - The total number of octets (bytes) received on the first Mobile WAN interface. |
|  | ifOutOctets | Up - The total number of octets (bytes) transmitted on the first Mobile WAN interface. |
|  | mobileTechnology | Tech - A string identifying the type of cellular connection used. |
|  | mobilePLMN | PLMN - A numeric identifier for the mobile operator, or "Public Land Mobile Network". Composed of the 3-digit Mobile Country Code (MCC) followed by the 2- or 3-digit Mobile Network Code (MNC). E.g. “27201” is Ireland (272), Vodafone (01). |
|  | mobileCell | Cell - The cell ID of the cell tower to which the device is connected. The string value is the hexadecimal representation of an integer. |
|  | mobileSignalStrength | Strength - Received Signal Strength Indication (RSSI) in dBm. Should correlate with mobileCSQ. |
|  |  mobileSignalQuality | Quality - Varies by cellular module type, but typically represents the “Energy per chip per power density” value (Ec/Io), in dBm. |
|  | mobileCSQ | CSQ - Signal strength number (0 to 31).<br>0 to 7: Bad<br>8 to 15: Marginal<br>16 to 23: Good<br>24 to 31: Excellent<br>99: No signal! |
|  | mobileUpTime | UpTime - The time in seconds since a connection was established to the mobile network. |
|  | mobileConnect | Connect  - Time stamp of latest connection to the cellular network. The device uses “Unix Epoch Time”, which is the number of seconds that have elapsed since the Unix epoch, which is 00:00:00 UTC on 1 January 1970. |
|  | mobileDisconnect | Disconnect - Time stamp of latest disconnection from the cellular network. 0 (“1970-01-01 00:00:00”) means that the device has not disconnected from the cellular network (since the last reboot or network restart). |
|  | mobileCard | Card - Which SIM card is in use:<br>0: “1st”<br>1: “2nd”<br>2: “3rd”<br>3: “4th” |
|  |  mobileReportPeriod | Period - Interval in minutes between MQTT messages or SNMP traps. This is a configuration setting called “Monitoring Interval” or “Trap Period”. |
|  | mobileTodayCells | CellsToday - Number of changes in mobileCell today. |
|  | statusTemperature | Temp - Internal temperature within the device, in degrees Celcius. Note that this will always be higher than the external (ambient) temperature, by around 20 degrees. |
|  | statusVoltage | Voltage - Voltage of the input power supply to the device. |

&nbsp;    
&nbsp; 
## Device Dashboard

To see the device dashboard go to Device → My Devices → And you select a specific device

When the device is online, there should be displayed data like this:

![Device Dashboard](/images/explanations-discussions/grafana/05dev1.png "Device Dashboard")
![Device Dashboard](/images/explanations-discussions/grafana/05dev2.png "Device Dashboard")
![Device Dashboard](/images/explanations-discussions/grafana/05dev3.png "Device Dashboard")
![Device Dashboard](/images/explanations-discussions/grafana/05dev4.png "Device Dashboard")
![Device Dashboard](/images/explanations-discussions/grafana/05dev5.png "Device Dashboard")
![Device Dashboard](/images/explanations-discussions/grafana/05dev6.png "Device Dashboard")


When the device has never been online there are no monitoring data to be displayed:

![Device Dashboard with no data](/images/explanations-discussions/grafana/06devnodata.png "Device Dashboard with no data")

&nbsp;    
&nbsp; 
### Description of individual graphs

|        Name of graph         |  Trap Attribute  |  Description       |
| :--------------------------  | :--------------- | :----------------- |
| Device Title | deviceTitle | String created by user describing the router |
| Device Type | deviceType | The exact router device type |
| Firmware Version | firmwareVersion | Last reported firmware version |
| Source Address | snmpTrapAddress | The IP address of the device. More exactly, it is the IP address of the particular interface on the device that was used to send the MQTT message or SNMP trap. |
| Cellular Data Usage | ifInOctets<br>ifOutOctets | The total number of octets (bytes) received  or sent on the Mobile WAN interface since last interface restart.|
| Instantaneous Mobile Speed | ifInOctets<br>ifOutOctets | Speed of the mobile connection computed as:<br>Download: Non negative derivation of  ifInOctets * 8<br>Upload: Non negative derivation of ifOutOctets * 8 |
| Per Carrier | ifInOctets<br>ifOutOctets | Transferred mobile data computed as:<br>Down: Non negative difference of ifInOctets<br>Up: Non negative difference of ifOutOctets |
| Device Uptime | sysUpTimeInstance | Time from the last reboot of the router |
| Cellular Up-Time | mobileUpTime | The time since a connection was established to the mobile network. |
| Download Total | ifInOctets | The total number of octets (bytes) received on the first Mobile WAN interface since last interface restart. |
| Upload Total | ifOutOctets | The total number of octets (bytes) transmitted on the first Mobile WAN interface since last interface restart. |
| Serial Number | infoSN | The last reported serial number of the device |
| IMEI | infoIMEI | "International Mobile Station Equipment Identity". Unique number which identifies the cellular module hardware. |
| Last Cellular Connect | mobileConnect | Time stamp of latest connection to the cellular network since the last reboot or network restart. The device uses “Unix Epoch Time”, which is the number of seconds that have elapsed since the Unix epoch, which is 00:00:00 UTC on 1 January 1970. E.g. 1576587282 = Tuesday 17 December 2019 12:54:42 UTC. |
| Last Cellular Disconnect | mobileDisconnect | Time stamp of latest disconnection from the cellular network since the last reboot or network restart in Unix Epoch Time. |
| Current SIM | mobileCard | Last reported SIM card in use |
| Current Cell | mobileCell | The cell ID of the cell tower to which the device is connected. The string value is the hexadecimal representation of an integer. |
| Current Channel | mobileChannel | Cellular channel number |
| Current Cellular Technology | mobileTechnology | A string identifying the type of cellular connection used. Supported values:<br>"N/A"<br>"GPRS"<br>"EDGE"<br>"UMTS"<br>"HSDPA"<br>"HSUPA"<br>"HSPA+"<br>"LTE"<br>"CDMA"<br>"EV-DO"<br>"EV-DO Rel. 0"<br>"EV-DO Rev. A"<br>"EV-DO Rev. B" |
| Current Cellular Operator | mobilePLMN | A numeric identifier for the mobile operator, or "Public Land Mobile Network". Composed of the 3-digit Mobile Country Code (MCC) followed by the 2- or 3-digit Mobile Network Code (MNC). E.g. “27201” is Ireland (272), Vodafone (01). |
| Last SNMP Received | ifInOctets | Age of the last download | 
| SNMP Report Period | mobileReportPeriod | Last reported reporting period. |
| ESN | infoESN | Last reported Electronic Serial Number of the cellular module. Applies only to CDMA modules. Currently not supported. |
| MEID |  | Currently not supported. | 
| Signal Quality | mobileSignalStrength | Received Signal Strength Indication (RSSI) in dBm. |
|  | mobileCSQ | Signal strength number (0 to 31). |
|  | mobileSignalQuality | Represents the “Energy per chip per power density” value (Ec/Io), in dBm. |
| Internal Conditions | statusTemperature | Internal temperature within the device, in degrees Celcius. Note that this will always be higher than the external (ambient) temperature, by around 20 degrees. |
|  | statusVoltage | Voltage of the input power supply to the device |
| Today Cells | mobileTodayCells | Mean of number of changes in mobileCell, that represents the cell ID of the cell tower to which the device is connected. |
| Neighbours Channel (only valid when on GPRS/EDGE) | mobileChannelN1<br>mobileChannelN2 | Cellular channel number for neighboring channel #1 to #5 |
| Neighbours Signal Strength (only valid when on GPRS/EDGE) | mobileSignalStrengthN1 to mobileSignalStrengthN5 | Signal Strength for neighboring channel #1 to #5. |

&nbsp;    
&nbsp; 
## Grafana tips & tricks

&nbsp;    
&nbsp; 
### View

If you press an arrow near the name of the graph. A small menu pops up:

![View](/images/explanations-discussions/grafana/07view1.png "View")

If you then press “View” you will get focused on the one graph only:

![View](/images/explanations-discussions/grafana/07view2.png "View")

To get the focus back, simply press “Esc” key.

&nbsp;    
&nbsp; 
If you press “Esc” once more, a side bar will appear:

![Side](/images/explanations-discussions/grafana/08side1.png "Side")

To close it press a “Cycle view mode” button twice. The button is in the upper part of Grafana:

![Side](/images/explanations-discussions/grafana/08side2.png "Side")

Also on some graphs you can zoom in if you select a part of a graph.

&nbsp;    
&nbsp; 
### Share

Grafana allows you to share a graph or snapshot of a graph or even to embed that graph in your own page.

To do that open the menu with arrow near the graph title:

![Share](/images/explanations-discussions/grafana/07view1.png "Share")

If you press the “Share” option a Share panel will appear:

![Share](/images/explanations-discussions/grafana/09share2.png "Share")

If you copy the link, you can send it to anyone so he can access the graph:

![Share](/images/explanations-discussions/grafana/09share3.png "Share")

You can find more information [here](https://grafana.com/docs/grafana/latest/sharing/share-panel/).

&nbsp;    
&nbsp; 
### Data download

Grafana allows you to inspect a graph and download a CSV of the data presented.

To do that open the menu with arrow near the graph title and choose “Inspect”:

![Download](/images/explanations-discussions/grafana/07view1.png "Download")

If you choose “Data” you get to this panel, where you can download the data in CSV format:

![Download](/images/explanations-discussions/grafana/10down.png "Download")

You can find more information [here](https://grafana.com/docs/grafana/latest/panels/inspect-panel/).

