# Troubleshooting

### Introduction

> <font size="4"><b> Bootstrap Server: is a process that enables the router to acquire certificates and keys, which are essential for connecting to the Management Server. </b></font> 


### <font size="4"><b>We explore three different scenarios when a router fails to connect:</b></font>

## Scenario 1: Router Stuck in Bootstrap

* **Problem:** 
   * The router lacks an internet connection and remains stuck in the Bootstrap Server process without receiving any successful response.

* **Potential Causes and Solutions:**
   * This issue may arise if the router was not properly registered in **DMP** during manufacturing.
   * Contact [DMP support](mailto:wadmp@advantech.com) to request registration of the router in the DMP instance.

## Scenario 2: Failure to Connect to Bootstrap Server

* **Problem:** 
  * The router displays the error: "Connection to Bootstrap Server failed."

* **Potential Causes and Solutions:**

   1. **Firewall Interference:** A firewall may be blocking the router’s connection to the server.
   
   2. **Incorrect Bootstrap Server Configuration:** Verify that the Bootstrap Server settings on your router match the public configuration if connecting to a public server. For private DMP servers, ensure the address is correct and accessible.

   3. **No Internet Connection:** Ensure that the router has a stable internet connection.

## Scenario 3: Failure Post-Bootstrap

* **Problem:** 
  * The router connects to the Bootstrap Server and completes the process successfully, but it fails to connect to the Management Server.

* **Potential Causes and Solutions:**

   1. **Firewall and Internet Issues:** Check for any firewall settings that might be blocking internet access.

   2. **Incorrect Router Time Settings:** If the router's time setting is significantly different from the server’s (by months or more), it could affect the validity of the certificates. Adjust the router’s time settings accordingly.
