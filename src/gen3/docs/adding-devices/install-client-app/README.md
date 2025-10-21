---
next: ../../device-management/
---

## Install/Upgrade a WebAccess/DMP Client App

If you want to migrate your device from 2.x.x instance, you need to upgrade the Router App to 3.x.x version via 2.x.x WebAccess/DMP Instance - go to [Migration from 2.x.x to 3.x.x Instance](../../migration/). <!-- new link -->

If you do not have the WebAccess/DMP Router App client installed, or you are not sure if you have the client installed, follow these steps:

**Step 1:** Check for the Installed client Router App:

- Log in to your router's web interface (the default IP is 192.168.1.1 on the ETH0 local interface).
- Navigate to Customization > Router Apps in the menu.

![APP-1](../../images/RouterAPP/APP-1.png)

::: tip 📌 Note:
If you see the WebAccess/DMP Client Router App installed, it should be able to connect to the WebAccess/DMP instance. Check the version and upgrade to the latest one if necessary (recommended). You can upgrade directly from WebAccess/DMP by selecting managed version on Desired Configuration tab on device page, or apply Configuration Profile with desired Client App version for multiple devices.
:::

**Step 2:** If you do not see the WebAccess/DMP Router App installed in your(?) device, you need to download it first and install.

![APP-2](../../images/RouterAPP/APP-2.png)

**Step 3:** Download the Client Router App from WebAccess/DMP Instance here:

![APP-3](../../images/RouterAPP/APP-3.png)

- This will direct you to the **download link** on our website: [WebAccess/DMP Client 3.x.x](https://icr.advantech.com/products/software/user-modules#webaccessdmp-client-3xx)

- **Note:** An Application Note is available for reference and settings of the client Router App if needed.

**Step 4:** Download the appropriate ".tgz" Router App file based on your device platform and install it manually through your device user interface.

![APP-4](../../images/RouterAPP/APP-4.png)

**Step 5:** Installation finished

- Your device should now be able to connect to the WebAccess/DMP instance.
- For manual upgrades of the client, follow the same steps and reinstall by adding the file to the device via Customize > Router Apps page.
  ![APP-5](../../images/RouterAPP/APP-5.png)

:::warning Caution:
If you are having difficulties to connect your device to WebAccess/DMP, please try [Troubleshooting page](../../troubleshooting/) or [FAQ](../../faq/). <!-- new links. -->
:::
