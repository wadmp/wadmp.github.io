---
prev: ../install-client-app/
next: ../../device-management/
---

## Move Device Between Companies

The **Move Device** feature allows administrators to transfer a router from its current company to another. 

--- 

### Authorization and Requirements

To ensure security and prevent unauthorized transfers, specific permissions are required. To move a device, you must meet the following criteria:

- **Dual Membership**: You must be an active member of both the **Source** company and the Destination company.
- **Source Permission**: You must hold the `RemoveDevices` permission in the company the device is leaving.
- **Destination Permission**: You must hold the `AddDevices` permission in the company the device is joining.

---

### Transfer Options: Data Migration

When initiating a move, you will be prompted to choose how much information should follow the device. You have two options:

#### Full Data Transfer

If you choose to move the device with its data, the following information is preserved and migrated to the new company:

- **Time series data**: Uptime statistics and reported metrics.
- **Identity**: The device name and metadata.
- **Configuration**: The **desired remote configuration settings**, ensuring the router maintains its intended state after the move.

#### Move Device Only

If you choose not to move the data, the device will appear in the new company as a "clean" entity. Previous metrics and configuration history will remain associated with the original company.

---

### How to Move Devices

There are two ways to perform a move depending on whether you are managing a single unit or a fleet.

#### Single Device Move

1. Navigate to the Device Detail page of the router you wish to move.
2. Click the Move Device button (located in the management action area).
3. Select the Destination Company from the dropdown list.
4. Toggle the Transfer Data option if you wish to keep metrics and configuration.
5. Confirm the move.

#### Batch Movement

1. For large-scale migrations, you can move multiple devices simultaneously:
2. Navigate to the Dashboard or Device List page.
3. Use the checkboxes to select all devices you wish to transfer.
4. Click the Move Selected Devices button located above the device table.
5. Follow the prompts to select the destination and data migration preferences.