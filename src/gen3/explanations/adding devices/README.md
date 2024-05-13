# Adding devices
xxxxxxxxxxxxxxxxxxxxxxx


##	1. Register a device (on-premises only)
cccccccccccccccc

##	2. Claim a device
ccccccccccccccccccccc

##	3. Install a WebAccess/DMP client app
**have not written it yet**

##	4. Firewall considerations (ports & addresses to whitelist)

This section lists the Fully Qualified Domain Names (FQDNs), corresponding IP addresses, and ports that customers must whitelist in their firewall settings.

**Warning:**
Please note that IP addresses are subject to change due to updates in our infrastructure. For stable connectivity, rely on the FQDNs.

<div align="center">

| FQDN                  | IP        | Port | Accessed from router?      |
| ---------------------| -------------- | ---- | -------------------------- |
| management.wadmp3.com | <center> 3.73.182.61<br>3.124.54.255<br>52.29.40.29</br> </center> | 8883 | <center> Yes </center> |
| bootstrap.wadmp3.com  | <center> 3.124.228.128<br>52.28.186.90<br>3.67.107.51</br> </center>  | 8884  | <center> Yes </center>     |
| content.wadmp3.com    | <center> 3.72.206.176<br>3.124.104.54<br>52.29.166.166</br> </center> | 443  | <center> Yes </center>     |
| gateway.wadmp3.com    | 52.57.47.37   | 443  | <center> Yes </center>     |

</div>

**Please ensure that: these specifications are accurately configured to avoid any disruptions in service.**
