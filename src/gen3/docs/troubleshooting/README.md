# Troubleshooting

### Introduction

**Connecting to Bootstrap Server** is a process that enables the router to acquire certificates and keys, which are essential for connecting to the Management Server.

### <font size="4"><b>Three different scenarios when a router fails to connect are described bellow:</b></font>

## Scenario 1: Router Stuck in Bootstrap

- **Problem:**

  - The router is stuck in the permanent Bootstrap Server process and is not receiving any successful response from the server. This issue could arise if the router was not registered into DMP during the manufacturing process.

- **Potential Causes and Solutions:**
  - This issue may arise if the router was not properly registered in **WebAccess/DMP** during manufacturing.
  - Contact [WebAccess/DMP support](mailto:wadmp@advantech.com) to request registration of the router in the DMP instance.
  - On-Prem only: contact your System Administrator to register the device to the WebAccess/DMP.

## Scenario 2: Failure to Connect to Bootstrap Server

- **Problem:**

  - The router can't connect to the Bootstrap Server and shows the message: "Connection to Bootstrap Server failed."

- **Potential Causes and Solutions:**

  1.  **Firewall Blockage:** A firewall may be preventing the router from connecting to the endpoint.

  2.  **Incorrect Default Bootstrap Server Value:** Verify that the Bootstrap Server configuration on the customer's router matches the public configuration if connecting to the public server. If using a private DMP server, ensure the address is correct and reachable.

  3.  **No Internet Connection:** Check the customer's internet connection.

## Scenario 3: Failure Post-Bootstrap

- **Problem:**

  - The router successfully connects to the Bootstrap Server, completing the Bootstrap Server process, but it fails to connect to the Management Server.

- **Potential Causes and Solutions:**

  1.  **Firewall Blockage:** A firewall may be preventing the router from connecting to the Internet.

  2.  **Incorrect Time Setting:** The router's time may differ significantly from the server's, causing issues with the certificate's validity. Ensure the router's time is correctly set.
