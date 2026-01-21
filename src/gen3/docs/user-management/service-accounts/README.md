---
prev: ../permissions/
next: ../../companies/
---

## Service Accounts

Service Accounts are a special type of account designed for **programmatic access** to the system. Unlike standard user accounts, service accounts are optimized to be used specifically for automation, scripts, and API integrations.

---

### Key Characteristics

- **No UI Access**: Service accounts cannot log in to the application's user interface. They are used exclusively for authenticated API calls or automated scripts.
- **Bypassing 2-FA**: Because service accounts are intended for non-interactive, machine-to-machine communication, **they bypass two-factor authentication (2-FA)**. This allows scripts to run autonomously without requiring a human to provide a secondary code.
- **Permissions & Roles**: Service accounts are as flexible as human users. You can assign specific permissions to them individually or assign them to a **Role** to inherit a predefined set of capabilities.

---

### Ownership and Cross-Company Access

Our system allows service accounts to manage resources across different organizational boundaries while maintaining a strict "Owner" hierarchy.

#### The Owner Company

Each service account is owned by exactly **one** company. Only the owner company has the authority to:

- Change the account description.
- Reset or update the password/credentials.
- Delete the service account entirely.

#### Cross-Company Permissions

A service account can be granted permissions to multiple companies. This is useful for managed service providers (MSPs) who use a single script to manage routers across several different client organizations.

---

### Managing Service Accounts in the UI

The **Service Accounts** page provides a centralized table of all accounts relevant to your currently active company.

#### Visual Distinction

The interface distinguishes between accounts you own and accounts that are simply "visiting" your company:

- **Owned Accounts**: Full management capabilities are available.
- **External Accounts**: These are accounts owned by another company that have been granted access to your resources.

#### Permission Management

If your active company is not the owner of a service account, your control is limited to your own scope. You can:

- **Edit Permissions**: Modify what that specific service account is allowed to do within your company.
- **Remove Access**: Revoke the account's permissions for your company entirely. You cannot, however, delete the account from the system or change its password.