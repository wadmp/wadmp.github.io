# Troubleshooting

### Introduction

**Connecting to Bootstrap Server** is a process that enables the router to acquire certificates and keys, which are essential for connecting to the Management Server.


### <font size="4"><b>Three different scenarios when a router fails to connect are described bellow:</b></font>

## Scenario 1: Router Stuck in Bootstrap

* **Problem:** 
   * The router lacks an internet connection because it is stuck in the permanent Bootstrap Server process and is not receiving any successful response from the server. This issue could arise if the router was not loaded into DMP during the manufacturing process.


* **Potential Causes and Solutions:**
   * This issue may arise if the router was not properly registered in **DMP** during manufacturing.
   * Contact [DMP support](mailto:wadmp@advantech.com) to request registration of the router in the DMP instance.

## Scenario 2: Failure to Connect to Bootstrap Server

* **Problem:** 
  * The router can't connect to the Bootstrap Server and shows the message: "Connection to Bootstrap Server failed."

* **Potential Causes and Solutions:**

   1. **Firewall Blockage:** A firewall may be preventing the router from connecting to the endpoint.
   
   2. **Incorrect Default Bootstrap Server Value:** Verify that the Bootstrap Server configuration on the customer's router matches the public configuration if connecting to the public server. If using a private DMP server, ensure the address is correct and reachable.

   3. **No Internet Connection:** Check the customer's internet connection.

## Scenario 3: Failure Post-Bootstrap

* **Problem:** 
  * The router successfully connects to the Bootstrap Server, completing the Bootstrap Server process, but it fails to connect to the Management Server.

* **Potential Causes and Solutions:**

   1. **Firewall Blockage:** A firewall may be preventing the router from connecting to the Internet.

   2. **Incorrect Time Setting:** The router's time may differ significantly from the server's, causing issues with the certificate's validity. Ensure the router's time is correctly set.

## Firewall considerations (ports & addresses to whitelist)

### WADMP Ports/Addresses

This section provides a list of addresses and ports that **customers need to whitelist** in their firewall.

:::warning Caution:
Please be aware that IP addresses may change with updates to our infrastructure.
Only the FQDN names will remain stable.
:::

<div align="center">

| FQDN                  | IP                                                          | Port | Accessed from router?      |
| --------------------- | ----------------------------------------------------------- | ---- | -------------------------- |
| management.wadmp3.com | <center>3.73.182.61<br>3.124.54.255<br>52.29.40.29</center> | 8883 | <center>Yes</center>       |
| bootstrap.wadmp3.com  | <center>3.124.228.128<br>52.28.186.90<br>3.67.107.51</center> | 8884 | <center>Yes</center>       |
| content.wadmp3.com    | <center>3.72.206.176<br>3.124.104.54<br>52.29.166.166</center> | 443  | <center>Yes</center>       |
| gateway.wadmp3.com    | 52.57.47.37                                                 | 443  | <center>Yes</center>       |

</div>