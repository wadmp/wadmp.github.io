---
prev: ../company-structure/
next: ../audit-logs/
---

## Company Contacts

You can now manage designated contact points for each organization at the **Company Detail** page. This feature ensures that the right people—whether they are registered application users or external stakeholders—receive critical information regarding billing, security, and operations.

---

### Contact Roles and Requirements

To ensure consistent communication, every company must have a designated point of contact at all times.

- **Primary Contact**: Each company must have **exactly one** primary contact.
    - By default, the person who fills out the company creation form is assigned this role.
    - The primary contact is automatically subscribed to all notification topics and cannot opt out.
    - To change the primary contact, you must designate another contact as "Primary," which will then allow the previous one to be modified or removed.
- **Non-Primary Contacts**: You may add an unlimited number of additional contacts to a company to ensure various departments are kept in the loop.

---

### Contact Attributes

Contacts in our system are flexible and do not require a registered user account. Each contact record contains:

- **Name**: The full name of the individual or department.
- **Email**: The primary address for all notifications.
- **Phone Number (Optional)**: A secondary way to reach the contact for urgent matters.
- **Subscriptions (Optional)**: A list of topics that the contact wants to be informed about.

--- 

### Subscription Topics

Contacts can be tailored to receive only specific types of information. There are three available email topics:

| Topic       | Description                                                                 | Behavioral Notes                                                                 |
|-------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Billing     | Receives invoices and billing-related details.                              | **Note:** This subscription only functions for **Root Companies**. In child companies, this subscription has no effect. |
| Operations  | Receives alerts regarding scheduled maintenance, temporary downtimes, and new version releases. | Essential for technical staff managing remote routers.                           |
| Security    | Designated for alerts regarding security incidents or vulnerabilities.     | These contacts are only notified in the event of a specific security concern.    |
