# Dashboards & Widgets

## WebAccess/DMP Client - Enable Monitoring

When a router installs the “WebAccess/DMP Client” User Module, the client may be configured to send monitoring data to the server. The data is displayed with Graphs and widgets. Graphs and widgets are used in WADMP: Home Dashboard → Company Dashboard and individual Device Dashboard.

* On the WADMP client, ensure the **Enable Monitoring** checkbox is checked (the default setting is *yes*), and note the **Monitoring Interval**.

![Enable Monitoring](../images/dashboards/DMP-Client.png)

&nbsp;    
&nbsp;

## General Structure of the User Interface

The UI is structured into four main areas:

![Router informations](../images/dashboards/generalUI(1).png)

&nbsp;    
&nbsp;

**A: The Title Panel**

* The Title Panel contains a link to the context panel, where you can specify your output on panel C. 

![General UI Structure](../images/dashboards/General-UI2.png)

* It also includes a link to the documentation, client router App, version and information about the currently logged-in user.

![link to the documentation](../images/dashboards/LinkToTheDocumentation.png)

&nbsp;    
&nbsp;

**B: The Views Panel**
* This is where you can create empty views or select already defined settings for panels C and D.

![views](../images/dashboards/Addview(1).png)

* To create a new view, click on the "+" add icon, enter the name of your view, and click "Create".

![Create View](../images/dashboards/CreateView.png)


* You can edit, duplicate, or delete a view by clicking on the *three dots icon* next to the name of the view you want to modify.

![Add & Ediet Views](../images/dashboards/AddEdietView.png)

&nbsp;    
&nbsp;

**C: The Details Panel**
This is the central panel of information. The details presented here depend on the context and actions selected. You can access the Edit View menu by clicking the top icon.

![Access Edit View](../images/dashboards/accesstheEditView.png)

* You can specify your desired widgets, including Company Stats Widgets, Chart Widgets, and columns in the Table. All of these can be moved at will. By clicking on the floppy disc icon, you save your current view.

![Edit View](../images/dashboards/EditView.png)

&nbsp;    
&nbsp;

**D: The Filter Panel**
In this section, you can filter based on any available parameters. You can also export, import (from CSV file), add devices, delete devices, reboot devices, create configuration profiles, and configure your current filters at will.

![Filter Panel](../images/dashboards/FilterPanel.png)


## Customization Of Views

### Company Dashboard

* When there are online devices for the selected company, you should see aggregated company data like this:

![online devices](../images/dashboards/company-dashboard-01.png)

* When there are no online devices, the dashboard looks like this:

![no online devices](../images/dashboards/company-dashboard-02.png)

&nbsp;    
&nbsp;

**Description of Individual Fields:**
    For detailed information about the fields, visit [Fields](https://docs.wadmp.com/gen3/explanations/device%20management/#_2-fields).


## Device Dashboard

* To see the device dashboard, go to the Dashboard section → Filter Panel → And select a specific device (By clicking on the device name).

![select Device](../images/dashboards/SelectaDevice.png)


* When you're configuring your first device, the page will be blank with no monitoring data to be displayed:

![Device Dashboard with no data](../images/dashboards/NoMonitoringData.png)

* To add Tables to the device's dashboard, press *Edit View*. 

![Edit View](../images/dashboards/DevicesEditView.png)

* press *Table* and make your already added Tables visible. You can add more by clicking the *+ Add Field* button.

![device table](../images/dashboards/01-device-table.png)

* To add Charts to the device's dashboard, press Edit View → Charts, select either Line Chart or Map (this is only functional when the device has GPS active), and choose your desired Field that will appear as graph widget on the device's dashboard. Click the "Save" button.

![device charts](../images/dashboards/device-charts.png)

> **NOTE:** Remember that every action in the *Edit View* must be saved by clicking the Floppy Disc icon.

## Searching And Filtering


## Tips & Tricks


### XXXXXXXX