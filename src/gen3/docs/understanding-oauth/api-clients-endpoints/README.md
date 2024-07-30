
## API Clients Endpoints

The public REST API provides the following endpoints which allow you to manage your OAuth clients:

![alt text](./APIClients_endpoints.png "APIClients endpoints")

The API Client is an abstraction for the type of authentication procedure that will be started after the calling authorization endpoint. For example, it governs whether you need to provide a username and password directly in the payload or if you will be redirected to a Login screen.

Some OAuth clients are provided by default in every WebAccess/DMP instance:
* "SWHWebApp" is the client used by our built-in User Interface, [wadmp.com](https://wadmp.com);
* "grafana" is the client used by Grafana, [grafana.wadmp.com](https://grafana.wadmp.com);
* "swagger_ui" is the client used by the "Try it out" feature on [api.wadmp.com](https://api.wadmp.com) (for browsing API in a web browser);
* "python" is the client used by the example Python scripts provided as part of the documentation in [docs.wadmp.com](https://docs.wadmp.com). It can be used for calling API endpoints from your application. It is not limited to python.

### Authorization

* When using the Web UI, you do this by clicking on authorize, typing in “swagger_ui”, ticking all scopes, and pressing Authorize, then entering your DMP user credentials (if not already signed in). We advise to use all four Scopes at all times, since the Scopes feature will soon be replaced with an improved system.
![alt text](./swagger_auth.png "APIClients endpoints")

* When using a script or an application, you can do this by using the following endpoint:
     * URL: https://gateway.wadmp.com/public/auth/connect/authorize (replace wadmp.com with your domain name if not using our public server)
     * Content type: json
     * Data:
     ```
     {
     'username': username,
     'password': password,
     'client_id': 'python',
     'grant_type': 'password'
     }
     ```

API authorization will only succeed for those users who have the appropriate permission.


