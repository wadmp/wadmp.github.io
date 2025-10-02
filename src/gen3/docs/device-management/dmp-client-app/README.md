---
prev: ../../device-management/
---

## WebAccess/DMP Client App

### Configure Client Application

If you want to propagate your managed configuration to the device, it is recommended to have a device in Synced and Online state. In WebAccess/DMP Client router app, this checkbox has to be enabled for the sync to by working (is enabled by default):

![Fields](../../images/management/client-enable.png)

(Enable monitoring is not necessary for settings propagation, it is for reporting of metrics.)

### Handling Router-side Changes

If a configuration change is made directly on the router locally (via the router's web interface), it will be overridden by WebAccess/DMP only under certain conditions: The particular setting must be set as managed (desired) on WebAccess/DMP.

Managed (desired) value may be defined using a Configuration Profile or via an individual Field from the Configuration category (may be created and setup manually, or looked up and set on Desired Configuration tab of Device page).
