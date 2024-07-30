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
