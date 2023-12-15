# 2.1.1: 24th April 2020

This release added support for WISE-6610 LoRaWAN Gateways.

### Code

* REST API change: New endpoint to delete a section of an application.
* Bugfix: Default permissions for company admins have been updated.

### Content

* Added support for the latest router firmware: 6.2.3.
* Added the latest version of the WA/DMP Client User Module: 2.0.4.
* Added support for WISE-6610 LoRaWAN Gateways.
* Bugfix: Removed historical WLAN section from all firmware > 6.2.0.
* Bugfix: Firmware binaries were not associated with SPECTRE-v3L-LTE-US devices.
* Bugfix: Firmware binaries were not associated with XR5i-v2e devices.

### docs.wadmp.com

* New Jupyter Notebooks:
  - plot_monitoring_data.ipynb [[1]](https://github.com/wadmp/wadmp.github.io/blob/master/jupyter_notebooks/plot_monitoring_data.ipynb)
  - company_hierarchy.ipynb [[2]](https://github.com/wadmp/wadmp.github.io/blob/master/jupyter_notebooks/company_hierarchy.ipynb)
* Added first example Node-RED flow to consume the REST API. [[3]](https://github.com/wadmp/wadmp.github.io/tree/master/node-red_flows)
* New Python scripts: to create and claim devices based on CSV files. [[4]](https://github.com/wadmp/wadmp.github.io/tree/master/python_scripts/csv_utilities)