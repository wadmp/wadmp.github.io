---
prev: ../
next: ../getting-started/
---

# Authentication

Most API requests require **OAuth 2.0 authentication** with a valid access token. For automated scripts or server-side routines, we support the **Resource Owner Password Credentials** flow. This allows you to exchange your username and password directly for an access token.

The client ID is named `python` for backward compatibility, but it can be used by scripts or applications **written in any language** (e.g., Bash, Node.js, etc.).

---

### Obtain Access Token

To get an access token, send a **POST** request to the following endpoint:

`POST https://gateway.wadmp3.com/public/auth/connect/token`

`Content-Type: application/x-www-form-urlencoded`

With the following form parameters:

- `grant_type=password`
- `username=<your_username>`
- `password=<your_password>`
- `client_id=python`

#### Example Request:

```bash
curl -X POST https://gateway.wadmp3.com/public/auth/connect/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=password&username=<your_username>&password=<your_password>&client_id=python"
  ```

#### Example Response:

```bash
  {
  "access_token": "<your_access_token>",
  "expires_in": 7200,
  "token_type": "Bearer"
}
```

Save the `access_token` — you’ll need it for subsequent API requests.

### Passing Access Token in API Requests
To authorize your API requests, include the access token in the `Authorization` header:

```bash
Authorization: Bearer <your_access_token>
```

#### Example:

```bash
curl -X GET https://gateway.wadmp3.com/api/applications \
  -H "Authorization: Bearer <your_access_token>"
```  


