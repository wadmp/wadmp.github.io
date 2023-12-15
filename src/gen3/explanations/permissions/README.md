# Permissions Explained

## Permissions Behaviour

Permissions regarding Companies and Users behave according to these rules:

* A user can not edit his own permissions.
* A user may not add himself to any company.
* A user can remove himself from a company if that company contains at least one other Company Admin and if the user has "Edit Users" permission on the company he is leaving.
* User may always edit his profile information (email, name, etc.), no matter his permissions.
* A user may remove another user from a company only if the change initiating user has "Edit Users" permission on that company.
* A user may edit another user's profile information (email, name, etc.) only if the change-initiating user has "Edit Users" permission for at least one of the companies the user is in.

## Permissions Description

![user_permissions](./user-permissions.png "Permissions")

* Company Admin - sets a fixed set of permissions

* User
  * View - Allows viewing a list of users they have access to
  * Create - Allows the user to create new users for their company in the system
  * Edit - Allows the user to edit an existing user in the system
  * Delete - Allows the user to delete another user in the system

* Company
  * Create - Allows the user to create new standalone companies
  * Edit - Allows the user to edit an existing company
  
* Devices
  * View - Allows the user to view the device's details
  * Claim & Release - Allows the user to claim a device in the system
  * Edit - Allows the user to make changes to a device
  * Delete - Allows the user to delete a device from the company. Delete devices from the system can only be done by a user with sysadmin permissions.

* Alerts History, Rules & endpoints
  
  * View - Allows viewing a list of Alerts History, Rules & Endpoints
  * Create - Allows the user to create new Alerts History, Rules & Endpoints
  * Edit - Allows the user to edit an existing Alerts History, Rules & Endpoints
  * Delete - Allows the user to delete Alerts History, Rules & Endpoints

* Auditing
  * View - Allows the user to view the auditing

* Fields
  * Manage - Allows the user to manage fields in the Fields section

* Views
  * Manage - Allows the user to manage the Views

* AppStore
  * Manage - Allows the user to manage the AppStore 
  
* Billing
  * Manage - Allows the user to manage the billing section
