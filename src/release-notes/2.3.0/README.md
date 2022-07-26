# 2.3.0: 9th April 2021

The significant new feature introduced by this release is **Billing**. 

* The default company billing status is "Free", which includes provisioning and managing up to 5 devices.    

* Company can be upgraded to "Premium", which offers an unlimited number of devices and API access, and is billed monthly.

### UI

* Major new feature: Support of Billing (company type indication, invoices list).
* New feature: External OAuth/OpenID providers are now supported (a new option on the Sign-in form).
* New feature: SIM PIN in the device can be changed from the UI.
* Bugfix: Playbooks can now be sorted, filtered, and searched. The default playbook list is ordered by the creation date.
* Improvement: Sub companies are now shown in the tree hierarchy under their parent company.
* Other minor UI improvements were made (Playbooks pagination, small screen adjustments, etc.).

### Code / API

* REST API: new endpoints for managing Companies (change of the company type regarding Billing).
* Bug fixes: Some numbers on the dashboard were not correctly calculated.

### Content

* Support of the latest WebAccess/DMP Client 2.0.10 and all the previous versions.
* Support of other new Router Apps (User Modules).
* Support of the latest router firmware 6.2.9 and all the previous versions.
* Support of new device models.


### docs.wadmp.com

* Added Billing Explained page. [[1]](https://docs.wadmp.com/explanations-discussions/billing.html)
* Added external authentication provider information to Sign up tutorial page [[2]](https://docs.wadmp.com/tutorials/sign-up.html)
* Updated API clients section in “Understanding OAuth” article. [[3]](https://docs.wadmp.com/explanations-discussions/understanding-oauth.html)
* Improved bulk configure clonnig script [[4]](https://github.com/wadmp/wadmp.github.io/tree/master/python_scripts/bulk_configure_new)
