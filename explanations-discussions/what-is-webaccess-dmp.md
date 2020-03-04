# What is WebAccess/DMP...? 

WebAccess/DMP Generation 2 is an advanced Enterprise-Grade platform solution for Provisioning, Monitoring, Managing and Configuring Advantech’s routers and IoT gateways.  It provides a zero-touch enablement platform for each remote device. 

With WebAccess/DMP, secure zero-touch pre-provisioning and pre-configuration is simple, regardless of how large your deployment is: from one device to thousands. 

The platform supports full multi-tenancy, with the possibility of permissions-enabled power-user oversight across tenancies. 

## Performance at Scale

WebAccess/DMP Generation 2 has been built for scale and performance.  The backend service architecture includes high-availability broker clusters, with load-balancing and elastic scale enablement.  Rest assured that your needs will be met, as you grow and scale your business. 



## Extensible Architecture

The platform has been designed for extensibility. Using leading-edge micro-services enabled architectural best practices, together with leading-edge elastic scale technologies, load balancing and brokerage services, the platform will scale-out as necessary.  The user-interface is built on our publicly available API, via our publicly available API Gateway, which enables real-time extensibility to available functionality, and the ability to integrate functionality with your existing services and infrastructure seamlessly: plug in, build-out.   



## AssureAuth™ PKI

Security is built-in by design: we have built a full Public Key Infrastructure (PKI) stack into the product suite:  your connected devices are securely provisioned, certified and authenticated. 

### Provisioning

AssureAuth™ PKI is used during the device provisioning sequence. Both device and server must mutually authenticate, using Advantech’s Certificate Authority as the root of trust.  Once successfully provisioned via a successful bootstrapping sequence, the devices will automatically connect with the platform. 



## Multi Tenancy

Every User must belong to at least one Company (aka "Tenant"). Every User may belong to one or more Companies (aka "Tenancies").  Every Company has at least one “CompanyAdmin” User, who decides on how to grant user-permissions (aka "Authorisation") 

For each User, and for each Company that User belongs to, unique user permissions may be granted.   



## AssureSync™ Configuration Management

WebAccess/DMP Generation 2 has incorporated industry best-practice Digital Twin Device Model concepts and combined them with real-time user-interface configuration status indicators.  It is possible to granularly configure every possible configuration item on every device, as a Desired State.  Every device will report its actual configuration, for every configuration item, which will be stored as a Reported State.  Our AssureSync™ Configuration Management engine will detect differences between Desired and Reported states, and automatically reconcile differences. 



## Edge Intelligence App management

Deploy one or many of our pre-prepared Edge Intelligence applications (aka “user modules” or “Apps”) directly from WebAccess/DMP, to one or many of your remote devices. Manage the Apps and versions you deploy: you can “pin” a specific App version, for each of your selected devices, as a Desired State, and you can manage the configuration settings for each App, for each device it’s deployed onto.

Use the device’s SDK to build your own Edge Intelligence Apps, then use the WebAccess/DMP API to publish and deploy your own Apps, at scale: WebAccess/DMP enables you to build your own required platform-side user-interface automatically. 

Any Apps that you create yourself will be managed through our AssureSync™ configuration management engine, just like our native Apps. 



## Secure Device Health Monitoring

Every remote device has build-in secure health-monitoring status indicators, that are reported to WebAccess/DMP, and stored in a Time-Series database: by default you get a minimum of 3-months history data, which you can zoom-in on and analyse at will, in real-time. 

Location Monitoring is also available, and can be enabled to show you precise GPS based geographic-location for each of your remote devices. 



## Built for Interoperability

WebAccess/DMP Generation is Fully API Enabled : in fact, we built our entire user-interface application using the publicly-available secure REST based API, via our publicly available API gateway, which you can find at [https://api.wadmp.com](https://api.wadmp.com/)

This means that you have the power of interoperability with your existing infrastructure: integrate the available services that we provide with the services you wish to observe or consume. 

