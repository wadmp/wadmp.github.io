# 2.5.2: March 30, 2023

This release contains improvements and bug fixes.

### Improvements:

* Added an option to pay the WADMP service through the Advantech WISE Marketplace.

### Bug Fixes: 

* Fixed Playbooks getting stuck in Running state when some of the actions failed .

* Fixed Playbooks getting stuck in Running state when multiple playbooks targetting the same device were started simultaneously.

* Fixed Playbook date and time showing “0” instead of the proper value for Start and Completion time.

* Fixed user permissions not being automaticly ticked when repeatedly ticking a Company Admin flag.

* Fixed GET /companies/\<id\> endpoint returning Internal Error when targeting a nonexisting company.

* Fixed User Signed In and User Signed Out audit logs showing a wrong IP address. Due to the service being behind NAT, they will no longer show IP addresses.

### Content

* Fixed WIFI AP DHCP Pool settings not being applied to router.

* Added support for ICR-324x-1n device types.
  