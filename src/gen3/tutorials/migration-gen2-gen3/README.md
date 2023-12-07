# Migration from 2.x.x to 3.x.x Version

The migration feature is meant to export data from version 2.x.x Company and import them to version 3.x.x Company. This means that migration data is independent of the structure of companies, and only data exported from the selected company in the 2.x.x version can be imported to the selected company in the 3.x.x version. Company Edit permission is needed for export/import to be available.

**What is migrated**:

- Devices - will be claimed to 3.x.x Company.
- Tags and Groups - Will be both added as _Fields_ of type _Tag - True/False_ in 3.x.x version, and Devices belonging to this Tag/Group will be marked as True.
- Alerts, including Alert Endpoints - will be added as Alerts and Alert Endpoints in the 3.x.x version.

## Export Data from 2.x.x Version

When logged in to your WebAccess/DMP version 2.x.x account,
go to _Companies_, find the company you want to export data from and click the Export icon on the right:

![Gen2Export](./gen2-export.png)

The dialog will appear with information about the export. Save the file _company_name_export.data_ to your computer.

![Gen2ExportDialog](./gen2-export-dialog.png)

## Import Data to 3.x.x Version

Log in to your WebAccess/DMP version 3.x.x account. Select or create the company you want data to be imported to. Go to _Companies_ in the menu and select the company detail. On the Company Profile page, click on the _Import_ button:

![Gen3Import](./gen3-import.png)

Choose the data file with exported data from version 2.x.x and submit.

![Gen3File](./gen3-file.png)

After a while (depending on the data file size) the result of import will appear with an overview like this:

![Gen3Result](./gen3-result.png)

You can review the result of import - numbers of what was added in every category, what was skipped (the reason for skipping is e.g. that the same Device/Tag/Alert is already present in the company), and most importantly what failed. For failed items, you can click on the number and see error messages with information about why it failed. Also, you can save this report in CSV file using the export icon at the top, so you can solve it later.

![Gen3DetailCsv](./gen3-detail-csv.png)
