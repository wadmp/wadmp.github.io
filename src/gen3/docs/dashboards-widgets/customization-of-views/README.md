---
prev: ../../dashboards-widgets/
---

## Customization Of Views

The Company Dashboard (home page) allows you to create different views, and the Device Dashboard lets you similarly customize views for data per single device.

### Structure of Company Dashboard

The dasboard UI is structured into four main areas:

![Router informations](<../../images/dashboards/generalUI(1).png>)

&nbsp;  
&nbsp;

**A: The Title Panel**

- The Title Panel contains a link to the context panel, where you can specify your output on panel C.

![General UI Structure](../../images/dashboards/General-UI2.png)

- It also includes a link to the documentation, client router App, version and information about the currently logged-in user.

![link to the documentation](../../images/dashboards/LinkToTheDocumentation.png)

&nbsp;  
&nbsp;

**B: The Views Panel**

- This is where you can create empty views or select already defined settings for panels C and D.

![views](<../../images/dashboards/Addview(1).png>)

- To create a new view, click on the "+" add icon, enter the name of your view, and click "Create".

![Create View](../../images/dashboards/CreateView.png)

- You can edit, duplicate, or delete a view by clicking on the _three dots icon_ next to the name of the view you want to modify.

![Add & Ediet Views](../../images/dashboards/AddEdietView.png)

&nbsp;  
&nbsp;

**C: The Details Panel**
This is the central panel of information. The details presented here depend on the context and actions selected. You can access the Edit View menu by clicking the top icon.

![Access Edit View](../../images/dashboards/accesstheEditView.png)

- You can specify your desired widgets, including Company Stats Widgets, Chart Widgets, and columns in the Table. All of these can be moved at will. By clicking on the floppy disc icon, you save your current view.

![Edit View](../../images/dashboards/EditView.png)

&nbsp;  
&nbsp;

**D: The Filter Panel**
In this section, you can filter based on any available parameters. You can also export, import (from CSV file), add devices, delete devices, reboot devices, create configuration profiles, and configure your current filters at will.

![Filter Panel](../../images/dashboards/FilterPanel.png)

- When there are online devices for the selected company, you should see aggregated company data like this:

![online devices](../../images/dashboards/company-dashboard-01.png)

- When there are no online devices, the dashboard looks like this:

![no online devices](../../images/dashboards/company-dashboard-02.png)

&nbsp;  
&nbsp;

**Description of Individual Fields:**
For detailed information about the fields, visit [Fields](https://docs.wadmp.com/gen3/docs/device%20management/fields).<!-- new link -->

#### Searching And Filtering

You can search, filter, and sort your devices at will, but remember that this only applies to your active view.

![ActiveView](../../images/dashboards/ActiveView.png)

#### Searching for a Specific Device

To search for a specific device:

1. Choose the appropriate column.
2. Enter your desired parameter.

- For example, to find devices with "Description 2" in the _Description_ column:

![Filter Search](../../images/dashboards/FilterSearch.png)

#### Sorting Devices

To sort devices by a specific column, such as _Description_:

1. Click the _Description_ column header.
2. Choose either descending or ascending mode.

![Sorting Filter](../../images/dashboards/SortingFilter.png)

#### Filtering

- You can interact with graphs by clicking on specific parts of them.

![Filter/Click-Change](../../images/dashboards/filter-click-change.png)

- For example, to display only devices of the "Vodafone CZ" operator, click on the section of the graph representing "Vodafone CZ" devices. This action will apply an active filter.

![Filter/Change](../../images/dashboards/filter-change.png)

- To remove this filter, click the "Clear Filters" button.

![Filter Clear](../../images/dashboards/clear-filter.png)

#### Customizing Columns

You can edit, show/hide, or add more columns in the Edit View mode, as detailed in the **General Structure of the UI >> C: The Details Panel** section.

![Fields](../../images/dashboards/Fields.png)

To customize your table fields, press the "Add field" button.

![AddFields](../../images/dashboards/AddFields.png)

&nbsp;  
&nbsp;

### Device Dashboard

- To see the device dashboard, go to the Dashboard section → Filter Panel → And select a specific device (By clicking on the device name).

![select Device](../../images/dashboards/SelectaDevice.png)

- When you're configuring your first device, the page will be blank with no monitoring data to be displayed:

![Device Dashboard with no data](../../images/dashboards/NoMonitoringData.png)

- To add Tables to the device's dashboard, press _Edit View_.

![Edit View](../../images/dashboards/DevicesEditView.png)

- press _Table_ and make your already added Tables visible. You can add more by clicking the _+ Add Field_ button.

![device table](../../images/dashboards/01-device-table.png)

- To add Charts to the device's dashboard, press Edit View → Charts, select either Line Chart or Map (this is only functional when the device has GPS active), and choose your desired Field that will appear as graph widget on the device's dashboard. Click the "Save" button.

![device charts](../../images/dashboards/device-charts.png)

> **NOTE:** Remember that every action in the _Edit View_ must be saved by clicking the Floppy Disc icon.

&nbsp;  
&nbsp;
