
## More details

OAuth is an *authorization* framework.
OAuth 2.0 is defined in [RFC 6749](https://tools.ietf.org/html/rfc6749) and Bearer Token Usage is in [RFC 6750](https://tools.ietf.org/html/rfc6750).

```
Protocol Flow

     +--------+                               +---------------+
     |        |--(A)- Authorisation Request ->|   Resource    |
     |        |                               |     Owner     |
     |        |<-(B)-- Authorisation Grant ---|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(C)-- Authorisation Grant -->| Authorization |
     | Client |                               |     Server    |
     |        |<-(D)----- Access Token -------|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(E)----- Access Token ------>|    Resource   |
     |        |                               |     Server    |
     |        |<-(F)--- Protected Resource ---|               |
     +--------+                               +---------------+
```

* The end-user is called the "Resource Owner".
* The "Client" is any application that the Resource Owner uses to access WebAccess/DMP.
* The Client receives an authorization "Grant" from the Resource Owner, which is a credential representing the Resource Owner's authorisation.
* Several Grant types are supported. Each type has its own protocol "flow".
* The "Authorisation Server" is a micro-service within WebAccess/DMP that authenticates the client, validates the authorisation grant, and if valid, issues an access token.
* The "Resource Server" is another micro-service within WebAccess/DMP that hosts the various resources that the end-user wants to access.

We also use [OpenID Connect](https://openid.net/connect/), an *authentication* layer built on OAuth 2.0.

* WebAccess/DMP is an "OpenID Provider" (OP). i.e., It is an OAuth 2.0 authorization server capable of authenticating the end-user and providing claims to a Relying Party (RP) about the authentication event and the end-user.
* When you create a new website or application that consumes the WebAccess/DMP API, your app is called a "Relying Party" (RP). i.e., It is an OAuth 2.0 client application requiring end-user authentication and claims from an OpenID Provider.

WebAccess/DMP uses [IdentityServer4](https://identityserver4.readthedocs.io/en/aspnetcore2/), which is an [open-source](https://github.com/IdentityServer/IdentityServer4), [certified](https://openid.net/developers/certified/) OpenID Provider for C# and ASP.NET Core.

![alt text](./openid_certified.png "OpenID Certified logo")

### Grant type

The model for the payload for the `POST /api-clients` endpoint looks like this:

![alt text](./grant_type_model.png "Model for POST endpoint")

`grant_type` is usually one of the following:
* `Implicit`. See the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) and [IdentityServer4](https://identityserver4.readthedocs.io/en/aspnetcore2/topics/grant_types.html#implicit) documentation. For example, this is the type used by the SWHWebApp and swagger_ui clients.
* `Code`. Called "Authorisation Code" in [OAuth 2.0](https://tools.ietf.org/html/rfc6749) and [IdentityServer4](https://identityserver4.readthedocs.io/en/aspnetcore2/topics/grant_types.html#authorization-code). For example, this is the type used by the grafana client.
* `ResourceOwnerPassword`. See the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) and [IdentityServer4](https://identityserver4.readthedocs.io/en/aspnetcore2/topics/grant_types.html#resource-owner-password) documentation. For example, this is the type used by the python client.