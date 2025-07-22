---
prev: ../2fa/
next: ../../companies/
---

## Permissions

### Permissions Management

- User Restrictions:

  - Users cannot edit their own permissions.
  - Users cannot add themselves to any company.

- Leaving a Company:

  - A user can remove themselves from a company if:

    - The company has at least one other Company Admin.
    - The user has the "Edit Users" permission for that company.

- Profile Information Editing:
  - Users may always edit their own profile information (e.g., email, name) regardless of their permissions.

Managing Other Users:

- A user can remove another user from a company if they have "Edit Users" permission on that company.
- A user can edit another user's profile information only if they have "Edit Users" permission for at least one of the companies the user is in.

### Explanations of Individual Permissions

![user_permissions](../../images/user-permissions.png "Permissions")

#### Company Admin - sets a fixed set of permissions:

- User Permissions:

  - View: Allows viewing the list of users the current user has access to.
  - Create: Allows creating new users within the user's company.
  - Edit: Allows editing existing users.
  - Delete: Allows deleting other users within the same company.

- Company Permissions:

  - Create: Allows creating new standalone companies.
  - Edit: Allows editing existing companies.

- Devices Permissions:

  - View: Allows viewing device details.
  - Claim & Release: Allows claiming or releasing a device in the system.
  - Edit: Allows editing device settings.
  - Delete: Allows deleting a device from the company. System-wide device deletion requires sysadmin permissions.

- Alerts, History, Rules & Endpoints Permissions:

  - View: Allows viewing the list of alerts, history entries, rules, and endpoints.
  - Create: Allows creating new alerts, history entries, rules, and endpoints.
  - Edit: Allows editing existing alerts, history entries, rules, and endpoints.
  - Delete: Allows deleting alerts, history entries, rules, and endpoints.

- VPN Networks

  - View: Allows viewing the list of VPN networks.
  - Create: Allows creating new VPN networks.
  - Edit: Allows editing existing VPN networks.
  - Delete: Allows deleting VPN networks.

- VPN Roadwarriors

  - View: Allows viewing the list of VPN roadwarriors.
  - Create: Allows creating new VPN roadwarriors.
  - Edit: Allows editing existing VPN roadwarriors.
  - Delete: Allows deleting VPN roadwarriors.

- VPN Settings

  - View: Allows viewing the VPN settings.
  - Edit: Allows editing the VPN settings.

- Additional Permissions:

  - Auditing: Allows viewing auditing details.
  - Fields: Allows managing fields.
  - Views: Allows managing views.
  - AppStore: Allows managing the AppStore.
  - Billing: Allows managing billing.
