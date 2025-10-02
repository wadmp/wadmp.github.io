## CSV Import Guide

This guide explains how to use CSV import features in WADMP3 to claim or update devices in bulk. It covers supported formats, required columns, Excel compatibility, and includes ready-to-use CSV templates.

---

### Example CSV Files

Use the following templates to prepare your CSV files:

- [Claim CSV Template](/assets/claim-template.csv)
- [Update CSV Template](/assets/update-template.csv)

Each file contains proper headers and sample data to help you get started.

---

### Claiming Devices via CSV

To import new devices into the system, use the **Claim CSV** format.

>  You can also copy a pre-filled CSV template for your specific company directly in the WADMP3 interface. This ensures the correct `CompanyId` and column formatting.

#### Required Columns

| Column      | Required | Description                                           |
|-------------|----------|-------------------------------------------------------|
| `Name`      | ✅ Yes   | User-friendly name for the device.                     |
| `Serial`    | ✅ Yes   | Serial number of the device (e.g. ACZ1100001234567).   |
| `MacAddress`| ✅ Yes   | MAC address used to uniquely identify the device.      |
| `Imei`      | ❌ No    | Optional IMEI number (can be left empty).              |
| `CompanyId` | ✅ Yes   | ID of the company to which the device should be assigned. |


#### Notes
- All devices in the CSV must belong to the same company.
- Devices must not already be claimed.
- The CSV must use **semicolon ( ; )** as a separator.
- Save the file using **UTF-8 encoding**.
- Errors during import will be shown in the UI.

---

### Updating Devices via CSV

Use the **Update CSV** format to modify settings or metadata of already existing devices.

> ✅ **Recommended flow:**  
> 1. On the device dashboard, either create the fields you want to update using **"Add Field"**, or simply make existing fields visible using the settings sidebar (eye icon).  
> 2. Click **Export CSV**, make your changes, and import the file back.  
> This ensures correct column names and minimizes errors.

#### Required Columns

| Column       | Required | Description                          |
|--------------|----------|--------------------------------------|
| `MacAddress` | ✅ Yes   | Unique identifier for the device.    |

#### Optional Columns (examples)

| Column                    | Required | Description                                                                  |
|---------------------------|----------|------------------------------------------------------------------------------|
| `ConfigProfile`           | ❌ No    | Name of the configuration profile to assign to the device.                   |
| `Name`                    | ❌ No    | Friendly name of the device.                                                 |
| `settings_ETH_IPADDR_v`  | ❌ No    | IP address to assign to the device (overrides the one from profile if set).  |
| `Description` | ❌ No    | Custom description shown in the dashboard.                                   |

#### Example from Exported Update CSV

| MacAddress         | Name       | settings_ETH_IPADDR_v  | Description                 |
|--------------------|------------|------------------------|-----------------------------|
| 00:11:22:33:44:55  | Router A   | 192.168.1.1            | Office Gateway              |
| 00:11:22:33:44:56  | Router B   | 192.168.1.2            | Backup Router Warehouse     |

#### Notes

- Leave optional values blank to keep current device values.
- The `MacAddress` must always be present and valid.
- Field names like `settings_ETH_IPADDR_v` must exactly match those generated in the exported CSV.
- If a field doesn't exist yet, but the setting ID is correct, WADMP3 will create the field automatically.
- If the device doesn't support the setting (e.g. Wi-Fi on non-Wi-Fi model), the update will be ignored.

---

### Opening CSV Files in Excel

Due to regional settings, Excel may misinterpret **semicolon ( ; )** delimiters.

#### Recommended Way to Import

1. Open Excel.
2. Go to `File → Open` and select your `.csv` file.
3. In the import wizard:
   - Choose **Delimited**.
   - Select **Semicolon ( ; )** as the separator.
   - Check that the preview shows correct column separation.
4. Click **Finish**.

> 💡 Tip: You can also import via `Data → From Text/CSV` in newer versions of Excel for better control.

---

### Import Behavior

- Each row is validated individually.
- Errors are reported with line numbers and reasons.
- Valid rows will be processed, invalid ones skipped.
- Use dashboard export to generate correct format and avoid guesswork.

---

### Best Practices

- Always save as **UTF-8** CSV with **semicolon** separators.
- Avoid Excel features like formulas, merged cells, or formatting.
- Double-check column headers — they are case-sensitive.
- Keep a backup copy of your original file for safety.

---

### Troubleshooting

-  Device not updated? Check for typos in column names.
-  Import failed? Make sure `MacAddress` and other required fields are present.
-  All values in one column? Re-import with correct delimiter selected.
---

 For further assistance, refer to the [Device Configuration](../device-configuration) and [Add a Device](../../adding-devices/add-a-device) pages or contact our support at [wadmp@advantech.com](mailto:wadmp@advantech.com).

