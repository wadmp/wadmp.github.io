(window.webpackJsonp=window.webpackJsonp||[]).push([[14],{482:function(e,t,r){e.exports=r.p+"assets/img/sign-in_examples.dede05c2.png"},483:function(e,t,r){e.exports=r.p+"assets/img/wadmp_sign-in.2e8a5314.png"},484:function(e,t,r){e.exports=r.p+"assets/img/grafana_sign-in.bf767b54.png"},485:function(e,t,r){e.exports=r.p+"assets/img/APIClients_endpoints.f33977e7.png"},486:function(e,t,r){e.exports=r.p+"assets/img/swagger_auth.1ae091df.png"},487:function(e,t,r){e.exports=r.p+"assets/img/openid_certified.39f27216.png"},488:function(e,t,r){e.exports=r.p+"assets/img/grant_type_model.c844552e.png"},589:function(e,t,r){"use strict";r.r(t);var a=r(10),n=Object(a.a)({},(function(){var e=this,t=e._self._c;return t("ContentSlotsDistributor",{attrs:{"slot-key":e.$parent.slotKey}},[t("h1",{attrs:{id:"understanding-oauth"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#understanding-oauth"}},[e._v("#")]),e._v(" Understanding OAuth")]),e._v(" "),t("h2",{attrs:{id:"introduction"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#introduction"}},[e._v("#")]),e._v(" Introduction")]),e._v(" "),t("p",[e._v("You are probably already familiar with the concept. When you visit a particular website or use a specific mobile app, instead of asking you to create a new account, "),t("em",[e._v("it prompts you to log in using an existing account on some other service")]),e._v(", such as Google, Facebook, or Twitter.")]),e._v(" "),t("p",[t("img",{attrs:{src:r(482),alt:"alt text",title:"Example screenshot showing sign-in options"}})]),e._v(" "),t("p",[e._v("There are several advantages:")]),e._v(" "),t("ul",[t("li",[e._v("You do not have to create and remember yet another password!")]),e._v(" "),t("li",[e._v("You do not have to give your password to a website or app you possibly do not trust.")]),e._v(" "),t("li",[e._v('Only the "identity provider" (in this case, Google, Facebook, or Twitter) handles your user credentials.')])]),e._v(" "),t("p",[e._v("WebAccess/DMP uses the same concept.")]),e._v(" "),t("blockquote",[t("p",[e._v("Remember that the User Interface or web app that you see at "),t("a",{attrs:{href:"%5Bhttps://wadmp.com"}},[e._v("wadmp.com")]),e._v(" is only one example\nof a client application that consumes the WebAccess/DMP API.")])]),e._v(" "),t("p",[e._v('WebAccess/DMP (the platform) acts as the "identity provider" for users. '),t("em",[e._v("Any")]),e._v(" client application that consumes the WebAccess/DMP API should redirect to our built-in Sign-In page. You can see this when you connect to "),t("a",{attrs:{href:"%5Bhttps://wadmp.com"}},[e._v("wadmp.com")]),e._v(" for the first time (or try it in an Incognito window). The browser is redirected to "),t("a",{attrs:{href:"https://gateway.wadmp.com/public/auth/public/auth/login",target:"_blank",rel:"noopener noreferrer"}},[e._v("gateway.wadmp.com/public/auth/public/auth/login"),t("OutboundLink")],1),e._v(":")]),e._v(" "),t("p",[t("img",{attrs:{src:r(483),alt:"alt text",title:"WA/DMP sign-in page"}})]),e._v(" "),t("p",[e._v("Another good example is Grafana. Our main UI utilizes Grafana to display dashboards for device monitoring data. These dashboards are embedded in the "),t("a",{attrs:{href:"https://wadmp.com",target:"_blank",rel:"noopener noreferrer"}},[e._v("wadmp.com"),t("OutboundLink")],1),e._v(" web pages, but you can also access Grafana directly at "),t("a",{attrs:{href:"https://grafana.wadmp.com",target:"_blank",rel:"noopener noreferrer"}},[e._v("grafana.wadmp.com"),t("OutboundLink")],1),e._v(".\nNote that "),t("em",[e._v("you do not have to create an account")]),e._v(' with Grafana: click "Sign in with OAuth":')]),e._v(" "),t("p",[t("img",{attrs:{src:r(484),alt:"alt text",title:"Grafana sign-in page"}})]),e._v(" "),t("p",[e._v("You are automatically redirected to the WebAccess/DMP sign-in page.")]),e._v(" "),t("h2",{attrs:{id:"api-clients-endpoints"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#api-clients-endpoints"}},[e._v("#")]),e._v(" API Clients Endpoints")]),e._v(" "),t("p",[e._v("The public REST API provides the following endpoints which allow you to manage your OAuth clients:")]),e._v(" "),t("p",[t("img",{attrs:{src:r(485),alt:"alt text",title:"APIClients endpoints"}})]),e._v(" "),t("p",[e._v("The API Client is an abstraction for the type of authentication procedure that will be started after the calling authorization endpoint. For example, it governs whether you need to provide a username and password directly in the payload or if you will be redirected to a Login screen.")]),e._v(" "),t("p",[e._v("Some OAuth clients are provided by default in every WebAccess/DMP instance:")]),e._v(" "),t("ul",[t("li",[e._v('"SWHWebApp" is the client used by our built-in User Interface, '),t("a",{attrs:{href:"https://wadmp.com",target:"_blank",rel:"noopener noreferrer"}},[e._v("wadmp.com"),t("OutboundLink")],1),e._v(";")]),e._v(" "),t("li",[e._v('"grafana" is the client used by Grafana, '),t("a",{attrs:{href:"https://grafana.wadmp.com",target:"_blank",rel:"noopener noreferrer"}},[e._v("grafana.wadmp.com"),t("OutboundLink")],1),e._v(";")]),e._v(" "),t("li",[e._v('"swagger_ui" is the client used by the "Try it out" feature on '),t("a",{attrs:{href:"https://api.wadmp.com",target:"_blank",rel:"noopener noreferrer"}},[e._v("api.wadmp.com"),t("OutboundLink")],1),e._v(" (for browsing API in a web browser);")]),e._v(" "),t("li",[e._v('"python" is the client used by the example Python scripts provided as part of the documentation in '),t("a",{attrs:{href:"https://docs.wadmp.com",target:"_blank",rel:"noopener noreferrer"}},[e._v("docs.wadmp.com"),t("OutboundLink")],1),e._v(". It can be used for calling API endpoints from your application. It is not limited to python.")])]),e._v(" "),t("h3",{attrs:{id:"authorization"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#authorization"}},[e._v("#")]),e._v(" Authorization")]),e._v(" "),t("ul",[t("li",[t("p",[e._v("When using the Web UI, you do this by clicking on authorize, typing in “swagger_ui”, ticking all scopes, and pressing Authorize, then entering your DMP user credentials (if not already signed in). We advise to use all four Scopes at all times, since the Scopes feature will soon be replaced with an improved system.\n"),t("img",{attrs:{src:r(486),alt:"alt text",title:"APIClients endpoints"}})])]),e._v(" "),t("li",[t("p",[e._v("When using a script or an application, you can do this by using the following endpoint:")]),e._v(" "),t("ul",[t("li",[e._v("URL: https://gateway.wadmp.com/public/auth/connect/authorize (replace wadmp.com with your domain name if not using our public server)")]),e._v(" "),t("li",[e._v("Content type: json")]),e._v(" "),t("li",[e._v("Data:")])]),e._v(" "),t("div",{staticClass:"language- extra-class"},[t("pre",{pre:!0,attrs:{class:"language-text"}},[t("code",[e._v("{\n'username': username,\n'password': password,\n'client_id': 'python',\n'grant_type': 'password'\n}\n")])])])])]),e._v(" "),t("p",[e._v("API authorization will only succeed for those users who have the appropriate permission.")]),e._v(" "),t("h2",{attrs:{id:"more-details"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#more-details"}},[e._v("#")]),e._v(" More details")]),e._v(" "),t("p",[e._v("OAuth is an "),t("em",[e._v("authorization")]),e._v(" framework.\nOAuth 2.0 is defined in "),t("a",{attrs:{href:"https://tools.ietf.org/html/rfc6749",target:"_blank",rel:"noopener noreferrer"}},[e._v("RFC 6749"),t("OutboundLink")],1),e._v(" and Bearer Token Usage is in "),t("a",{attrs:{href:"https://tools.ietf.org/html/rfc6750",target:"_blank",rel:"noopener noreferrer"}},[e._v("RFC 6750"),t("OutboundLink")],1),e._v(".")]),e._v(" "),t("div",{staticClass:"language- extra-class"},[t("pre",{pre:!0,attrs:{class:"language-text"}},[t("code",[e._v("Protocol Flow\n\n     +--------+                               +---------------+\n     |        |--(A)- Authorisation Request ->|   Resource    |\n     |        |                               |     Owner     |\n     |        |<-(B)-- Authorisation Grant ---|               |\n     |        |                               +---------------+\n     |        |\n     |        |                               +---------------+\n     |        |--(C)-- Authorisation Grant --\x3e| Authorization |\n     | Client |                               |     Server    |\n     |        |<-(D)----- Access Token -------|               |\n     |        |                               +---------------+\n     |        |\n     |        |                               +---------------+\n     |        |--(E)----- Access Token ------\x3e|    Resource   |\n     |        |                               |     Server    |\n     |        |<-(F)--- Protected Resource ---|               |\n     +--------+                               +---------------+\n")])])]),t("ul",[t("li",[e._v('The end-user is called the "Resource Owner".')]),e._v(" "),t("li",[e._v('The "Client" is any application that the Resource Owner uses to access WebAccess/DMP.')]),e._v(" "),t("li",[e._v('The Client receives an authorization "Grant" from the Resource Owner, which is a credential representing the Resource Owner\'s authorisation.')]),e._v(" "),t("li",[e._v('Several Grant types are supported. Each type has its own protocol "flow".')]),e._v(" "),t("li",[e._v('The "Authorisation Server" is a micro-service within WebAccess/DMP that authenticates the client, validates the authorisation grant, and if valid, issues an access token.')]),e._v(" "),t("li",[e._v('The "Resource Server" is another micro-service within WebAccess/DMP that hosts the various resources that the end-user wants to access.')])]),e._v(" "),t("p",[e._v("We also use "),t("a",{attrs:{href:"https://openid.net/connect/",target:"_blank",rel:"noopener noreferrer"}},[e._v("OpenID Connect"),t("OutboundLink")],1),e._v(", an "),t("em",[e._v("authentication")]),e._v(" layer built on OAuth 2.0.")]),e._v(" "),t("ul",[t("li",[e._v('WebAccess/DMP is an "OpenID Provider" (OP). i.e., It is an OAuth 2.0 authorization server capable of authenticating the end-user and providing claims to a Relying Party (RP) about the authentication event and the end-user.')]),e._v(" "),t("li",[e._v('When you create a new website or application that consumes the WebAccess/DMP API, your app is called a "Relying Party" (RP). i.e., It is an OAuth 2.0 client application requiring end-user authentication and claims from an OpenID Provider.')])]),e._v(" "),t("p",[e._v("WebAccess/DMP uses "),t("a",{attrs:{href:"https://identityserver4.readthedocs.io/en/aspnetcore2/",target:"_blank",rel:"noopener noreferrer"}},[e._v("IdentityServer4"),t("OutboundLink")],1),e._v(", which is an "),t("a",{attrs:{href:"https://github.com/IdentityServer/IdentityServer4",target:"_blank",rel:"noopener noreferrer"}},[e._v("open-source"),t("OutboundLink")],1),e._v(", "),t("a",{attrs:{href:"https://openid.net/developers/certified/",target:"_blank",rel:"noopener noreferrer"}},[e._v("certified"),t("OutboundLink")],1),e._v(" OpenID Provider for C# and ASP.NET Core.")]),e._v(" "),t("p",[t("img",{attrs:{src:r(487),alt:"alt text",title:"OpenID Certified logo"}})]),e._v(" "),t("h3",{attrs:{id:"grant-type"}},[t("a",{staticClass:"header-anchor",attrs:{href:"#grant-type"}},[e._v("#")]),e._v(" Grant type")]),e._v(" "),t("p",[e._v("The model for the payload for the "),t("code",[e._v("POST /api-clients")]),e._v(" endpoint looks like this:")]),e._v(" "),t("p",[t("img",{attrs:{src:r(488),alt:"alt text",title:"Model for POST endpoint"}})]),e._v(" "),t("p",[t("code",[e._v("grant_type")]),e._v(" is usually one of the following:")]),e._v(" "),t("ul",[t("li",[t("code",[e._v("Implicit")]),e._v(". See the "),t("a",{attrs:{href:"https://tools.ietf.org/html/rfc6749",target:"_blank",rel:"noopener noreferrer"}},[e._v("OAuth 2.0"),t("OutboundLink")],1),e._v(" and "),t("a",{attrs:{href:"https://identityserver4.readthedocs.io/en/aspnetcore2/topics/grant_types.html#implicit",target:"_blank",rel:"noopener noreferrer"}},[e._v("IdentityServer4"),t("OutboundLink")],1),e._v(" documentation. For example, this is the type used by the SWHWebApp and swagger_ui clients.")]),e._v(" "),t("li",[t("code",[e._v("Code")]),e._v('. Called "Authorisation Code" in '),t("a",{attrs:{href:"https://tools.ietf.org/html/rfc6749",target:"_blank",rel:"noopener noreferrer"}},[e._v("OAuth 2.0"),t("OutboundLink")],1),e._v(" and "),t("a",{attrs:{href:"https://identityserver4.readthedocs.io/en/aspnetcore2/topics/grant_types.html#authorization-code",target:"_blank",rel:"noopener noreferrer"}},[e._v("IdentityServer4"),t("OutboundLink")],1),e._v(". For example, this is the type used by the grafana client.")]),e._v(" "),t("li",[t("code",[e._v("ResourceOwnerPassword")]),e._v(". See the "),t("a",{attrs:{href:"https://tools.ietf.org/html/rfc6749",target:"_blank",rel:"noopener noreferrer"}},[e._v("OAuth 2.0"),t("OutboundLink")],1),e._v(" and "),t("a",{attrs:{href:"https://identityserver4.readthedocs.io/en/aspnetcore2/topics/grant_types.html#resource-owner-password",target:"_blank",rel:"noopener noreferrer"}},[e._v("IdentityServer4"),t("OutboundLink")],1),e._v(" documentation. For example, this is the type used by the python client.")])])])}),[],!1,null,null,null);t.default=n.exports}}]);