---
prev: ../
next: ../audit-logs/
---

## Company Structure

Each company hierarchy consists of a single Root company and zero or more Child companies (also called sub-companies).

- Users may create new Root companies (and thus separate hierarchies) only if all the following conditions are met:

  - They are not members of any companies.
  - They have not reached the limit of three created hierarchies per user account.
  - Their last created hierarchy no longer exists.

- Any companies created while the user is a member of another company become sub-companies of the currently active company.

- Child companies may create their own sub-companies. There is no limit on the number of child companies or the number of levels the company hierarchy may have.

### Managing Child Companies

- Each company must have at least one user with a "Company Admin" role. This role provides full permissions over the company and includes the following abilities for direct sub-companies:

  - Delete sub-company (deletes the entire sub-hierarchy).
  - View the device count for the sub-hierarchy (does not include any details beyond the count).

- Users automatically become Company Admins of any company they create.

- Users may give up access to a child company by removing themselves from it.

- It is not possible to change a company’s parent (to move it between parents).
