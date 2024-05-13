# Adding devices
xxxxxxxxxxxxxxxxxxxxxxx


##	1. Register a device (on-premises only)
cccccccccccccccc

##	2. Claim a device
ccccccccccccccccccccc

##	3. Install a WebAccess/DMP client app
**Installing WebAccess/DMP Client App**

To connect a device to the platform, the WebAccess/DMP router app (client) needs to be installed first. Below are the steps to install the client app:

1. **Download Client App:**
   - The WebAccess/DMP client app can be downloaded from the following link: [WebAccess/DMP Client App](https://docs.wadmp.com/gen3/client/)
   - Alternatively, you can access the client app download link through our website: [WebAccess/DMP Client Download](https://icr.advantech.com/products/software/user-modules#webaccessdmp-client-3xx)
   
2. **Installation Process:**
   - The installation process for the client app is detailed in the configuration manual. Refer to the specific configuration manual for your router model. 
   - Access the Configuration Manual, for example: [ICR-3200 Configuration Manual](https://icr.advantech.com/support/router-models/download/299/icr-3200-configuration-manual-20240327.pdf)
   - Navigate to the section titled "Customization -> Router Apps" to find instructions on how to load and install the client app on your device.
   - Note: The installation process may vary depending on the router model, but the section regarding installation of router apps remains consistent across all models.

3. **Pre-Installed Client App:**
   - In most cases, the client app may come pre-installed by default. This means it is already available in the device's router apps section.
   - For older devices or firmware versions, you may need to manually download and install the client app.

4. **Accessing Installed Client App:**
   - After installation, access the device's router apps section. 
   - Log in to the device to view installed apps.
   - The client app should be visible in the router apps section. Here, users can find details for adding the device to the platform and copy necessary information.
   - Below is an example screenshot of the router apps section with the installed client app:


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
