---
prev: ../2fa/
next: ../service-accounts/
---

## Permissions & Roles

Permissions in the system govern what users can view, create, edit, or delete within a company. They are **scoped per company**, meaning a user may belong to multiple companies and have different permissions or roles in each. Permissions can be assigned **individually** or through **roles**.

---

### General Rules

- Users can always edit their own profile information (name, email, etc.), regardless of their assigned permissions.
- Users cannot modify their own permissions.
- Users may modify the permissions of other users only for companies where they have the **Edit Users** permission, and they can assign only those permissions that they themselves currently hold.

---

### Roles

Roles are predefined or custom permission sets that simplify user management. Each user may have **zero or one role per company**.

#### Default Roles

The system provides several **default roles**. Using these roles ensures that any **new permissions added in future releases** are automatically included appropriately.

| Role | Description | Key Capabilities |
|---------------|-----------------------------------------------------------------------------|-----------------------|
| Company Admin | Full access to all company features. System enforces at least one Company Admin per company. | All permissions, including company management, billing, devices, VPN, alerts, and auditing. |
| Operator | Full operational capabilities except company management or billing. | Manage devices, alerts, VPN, fields, views, proxy links, and service accounts. |
| Viewer | Read-only access to company data.| All View permissions only; cannot create, edit, or delete resources.|


#### Custom Roles

- Users may create, edit, or delete custom roles.
- Users can only assign permissions that they themselves possess.
- Custom roles allow precise control over which actions a user may perform within a company.

---

3. Best Practices

- Always assign users to **roles** rather than individual permissions when possible. This ensures easier management as new permissions are added.
- Use **custom roles** for specialized access where default roles are insufficient.
- Avoid granting permissions beyond what users require for their responsibilities.

<!-- DELETE part after -->
