# Gen1 to Gen2 Migration

## Introduction
We consider two different scenarios:

**Scenario 1:** The customer is using the Production instance of **Gen1** [www.hub.bb-smartworx.com](https://hub.bb-smartworx.com/), and wants to move to the Production instance of **Gen2** [wadmp.com](https://wadmp.com). i.e., These are the public multi-tenant instances.

**Scenario 2:** The customer uses a private on-premise instance of **Gen1** and wants to move to a private instance of **Gen2**. i.e., Either an on-premise instance or a “hybrid” (private cloud) instance.

## Ensure that all existing devices have been created on the new Gen2 instance

**Scenario 1:** No work required.

At the moment, when new devices are manufactured, they are automatically created on the Production instance of **Gen1** [hub.bb-smartworx.com](https://hub.bb-smartworx.com/)

::: tip Note:
New manufactured devices on the Production instance of Gen1 are automatically created on the Production instance of Gen2  [wadmp.com](https://wadmp.com). Therefore, devices older than that may need to be created manually.

We already have a SQL migration script that runs daily. New devices on the Production instance of **Gen1** are automatically created on the Production instance of **Gen2** [wadmp.com](https://wadmp.com).

**Scenario 2:** All devices must be created on the new private **Gen2** instance. This may be done via the **Gen2** [UI](https://wadmp.com/) or [API](https://api.wadmp.com/#!/).

If using the API, we provide an example Python script here: [WADMP GitHub](wadmp.github.io/python_scripts/csv_utilities) at master · wadmp/wadmp.github.io 

All required are the credentials of a user with Manufacturing (CreateDevice) permission.

To create a list of the existing devices on the private **Gen1** instance, it should be possible to use a) the **Gen1** [REST API](https://hub.bb-smartworx.com/api/v2/) or b) a SQL query.
:::

## Install the Gen2 WA/DMP Client User Module on all devices
**Scenario 1&2:** The **Gen2** User Module can be installed via **Gen1**. This must be done via the **Gen1** UI, as there is no support for User Modules in the **Gen1** [REST API](https://hub.bb-smartworx.com/api/v2/). If the number of devices involved is large, a Configuration Profile could be used.

The only issue may be getting the latest version of the **Gen2** User Module onto the **Gen1** instance. 

::: tip Note:

From January 2019, all devices leaving the factory will have the **Gen1** WA/DMP Client User Module (wadmp_client) installed.

Devices with a “-SWH” suffix in the order code have the client enabled. All others have the client disabled.

Reference: [Product Change Notification PDF](https://ep.advantech-bb.cz/support/router-models/download/206/pn-2018-10-01-advantech-uploading-of-hmpclient-um-en.pdf)

All new devices leaving the factory also have the **Gen2** WA/DMP Client User Module (wadmp_client) installed and enabled. We do not know when this change was introduced but assume 2019 or 2020.

The “-SWH” suffix also determines if the **Gen2** client is enabled or disabled.
:::

## Configure the Gen2 WA/DMP Client User Module to connect to the new Gen2 instance

::: tip Note:

This step confuses because, by design, a **Gen2** client can NOT be directed to a Management Server directly. It must connect to a Bootstrap Server first, and the Bootstrap Server then a) issues a certificate to the device and b) redirects the device to a Management Server,

The **Gen2** WA/DMP Client User Module has one particular configuration item: "Bootstrap Server Address”. This defaults to [“bootstrap.wadmp.com”](http://bootstrap.wadmp.com/#/login?redirect=%2F). This configuration can NOT be changed from **Gen1** or **Gen2**.
:::

**Scenario 1:** No work required. The **Gen2** User Module will automatically connect to the Production instance of **Gen2**. By default, the Bootstrap Server in the Production instance of **Gen2** will direct all devices to the Management Server in the Production instance of **Gen2**.

**Scenario 2:** We need to sub-divide this scenario as follows:

**Scenario 2A:** The customer is using a private WAN network. i.e., If they are using cellular, they have a Private APN. This means they can re-configure their private DNS server to direct [“bootstrap.wadmp.com”](http://bootstrap.wadmp.com/#/login?redirect=%2F) to the private Bootstrap Server on their new **Gen2** instance. No other work is required. By default, the Bootstrap Server in the private instance of **Gen2** will direct all devices to the Management Server in the same private instance.

**Scenario 2B:** The customer does not have a private DNS server. In this case, there are no easy solutions:

If the customer’s devices have internet access (which is highly likely if they are using a Public APN), it may be acceptable to allow the devices to contact the Bootstrap Server in the (public) Production instance of **Gen2**. Then, we can use the **Gen2** REST API to configure the Bootstrap Server to redirect the customer’s devices to their private Management Server. We would also have to use the **Gen2** REST API to configure the private Management Server to trust devices that present certificates signed by the public Bootstrap Server. However, it is unlikely that a customer who wants the increased security of a private instance will find this acceptable.

We could consider adding [another layer of indirection](https://en.wikipedia.org/wiki/Fundamental_theorem_of_software_engineering). We could allow the public Bootstrap Server to be configured to redirect a device to another Bootstrap Server. This would also require a new version of the **Gen2** User Module to support this functionality. It also breaks the LwM2M architecture.

Manually re-configure the **Gen2** User Module on each device. This requires access to the local web server on every device, either directly, using public IP addresses, or using a VPN.

We could consider allowing the **Gen2** User Module to be configured via **Gen1**.

We could consider building a custom version of the **Gen2** User Module, where the default value of the Boostrap Server Address is changed. Note that this would also have implications for Step 2 above.

:::warning Warning:

Any workaround that involves modifying the Bootstrap Server Address on a device should be avoided. By design, a Bootstrap Server provides a reliable fall-back mechanism if, for any reason, the connection to a Management Server should fail. If you allow the Bootstrap Server Address to be re-configured, you risk losing the device with no recovery mechanism. Therefore, we do NOT allow the Bootstrap Server Address to be remotely configured via **Gen1** or **Gen2**.

In summary, we should advise customers that it only makes sense to deploy a private **Gen2** instance if their devices will be using a private APN!

:::

## Establish what Desired State is required on Gen2 for each device

::: tip Note:

When a device connects to **Gen2**, it will automatically report its current configuration. This is also known as the “Reported State” of the device. In **Gen2**, every device also has a “Desired State” blank by default.

If the device's configuration was changed locally (using the device’s local web server, or an SSH script, etc.), then the default behavior of **Gen2** is to report the change. If a customer needs to ensure that **Gen2** will overwrite any local changes, they need to define the Desired State for each device.

Conversely, if local changes are not possible on the customer’s devices, devices already configured via **Gen1** will not need a Desired State on **Gen2**.

However, if the customer anticipates adding new devices directly to **Gen2**, they will need to define a Desired State.

:::

**Scenario 1&2:** This may be done via the **Gen2** [UI](https://wadmp.com/) or [API](https://api.wadmp.com/#!/).

If you want to configure multiple devices with the same Desired State, then in the UI, we provide the “Playbook” feature. Also, see the public Bulk Configuration scripts [here](https://github.com/wadmp/wadmp.github.io/tree/master/python_scripts/bulk_configure).

::: tip Note:

If the customer was using the “Configuration Profile” feature on **Gen1**, it is essential to explain that this feature is NOT available on **Gen2**. This is not a problem because we believe the **Gen2** design is superior in every respect, but it may confuse.

When a device is a member of a Configuration Profile on **Gen1**, it can NOT be managed individually. i.e., The configuration defined in the Configuration Profile is assumed to be the “Desired State” of the device.

In **Gen2**, every device has its individual “Desired State”, whether or not it is part of a group, Playbook, or anything else. The “Sync Engine” in **Gen2** continuously compares the Reported and Desired States for every device and strives to make them equal.

The “Playbook” feature in **Gen2** only exists to make it easy to configure the Desired State of several devices simultaneously. Once a Playbook has been run once, it has had no effect.

:::

## Disable the Gen1 WA/DMP Client User Module on all devices

A device can maintain simultaneous connections to both **Gen1** and **Gen2**. But this is not recommended long-term, as it is straightforward to get into a situation where the two desired configurations conflict.

It is not possible to configure the **Gen1** User Module via **Gen2**. i.e., We cannot leave the **Gen1** User Module installed and disable it.

**Scenario 1&2:** Use the **Gen2** instance to remove (delete) the **Gen1** User Module (HMPClient) from each device.

Again, this may be done via the **Gen2** [UI](https://wadmp.com/) or [API](https://api.wadmp.com/#!/).

## Ensure that all future devices will be automatically created on the new Gen2 instance

**Scenario 1:** No work required.

As stated above in Step 1, we already have a daily SQL migration script. Therefore, any new devices on the Production instance of **Gen1** are automatically created on the Production instance of **Gen2** [WADMP](https://wadmp.com).

**Scenario 2:** The customer will need to define their workflow for obtaining the required information about new devices. (The minimum information required is Serial Number, MAC Address, and Device Type. IMEI is highly recommended).

For example, this may be available on an Advantech Invoice or Delivery Note.

As stated above in Step 1, we provide a public “create_from_csv.py” script here: [WADMP GitHub Link](wadmp.github.io/python_scripts/csv_utilities) at master · wadmp/wadmp.github.io 

## Ensure that all future devices will be configured to connect to the new Gen2 instance and not Gen1

**Scenario 1&2:** This step may require changes to the customer’s internal policies and procedures.

When purchasing cellular routers, the customer may have been using a particular order code. For example, the “-SWH” prefix ensures that the **Gen1** User Module was installed and enabled. Or the customer may have been paying Advantech (or a channel partner) for some customization of new devices.

**Scenario 2:** Review Step 3 above regarding what is required to direct a device to the new **Gen2** instance. The customer may want to consider customizing new devices to make the process easier.

::: warning Warning:
From a security perspective, it is essential to remember that Factory Bootstrap is always preferred over Client-Initiated Bootstrap. i.e., The ideal scenario is that devices leave the factory already provisioned with a private key and a certificate for their intended Management Server. This applies to Scenario 1 (public instances) and Scenario 2 (private instances). However, we do not have any support for Factory Bootstrap at the time of writing. It would not be difficult to implement this for Scenario 1. For Scenario 2, it would only be possible if the customer allows factory access to their private API and Bootstrap Server.
:::