To use these .http files, you must have the "REST Client" extension installed in VS Code.

AND you must define environment variables in your local settings.json file.
This is usually in `~/.config/Code/User/settings.json`

Altenatively, click on Extensions in the left-hand sidebar,
click on the "Manage" icon for "REST Client",
and select "Configure Extension Settings".
Scroll down to "Environment Variables", and you will see a link to "Edit in settings.json"

Paste the following into the root object:
```
    "rest-client.environmentVariables": {
         "$shared": {
             "BASE_PATH": "api"
         },
         "develop": {
             "BASE_URL": "https://gateway.dev.wadmp.com",
             "USERNAME": "your_username",
             "PASSWORD": "your_password"
         },
         "staging": {
             "BASE_URL": "https://gateway.staging.wadmp.com",
             "USERNAME": "your_username",
             "PASSWORD": "your_password"
         },
         "production": {
             "BASE_URL": "https://gateway.wadmp.com",
             "USERNAME": "your_username",
             "PASSWORD": "your_password"
         }
    }
```

Official Documentation: https://marketplace.visualstudio.com/items?itemName=humao.rest-client
