# Release Notes for Client Router App: 

## Latest version:

### v2.1.4 (2022-04-28)
* Added idempotency token for handling repeated request, which have already been handled.
* Added welcome page to the router.

## Download:

We recommend always using the most up-to-date version of the client.

[Download the latest client and Application Note (Manual)](https://icr.advantech.cz/products/software/user-modules#webaccessdmp-client)

The client router app can also be upgraded via WebAccess/DMP.


## Previous versions:

### v2.1.3 (2021-12-08)
* If the router does not measure temperature, send value was modified from 0 degrees to -273 degrees
* Modification of return codes when installation failure occurs.

### v2.1.2 (2021-08-03)
* Added trace log level
* MQTT keepalive is now configurable
* Fixed collision between Use Module settings and FirmWare section settings
* Module download now always resumes
* Fixed issues with upgrade/downgrade settings reporting

### v2.1.1 (2021-06-17)
* Critical library incompatibility bugfix.

### v2.1.0 (2021-05-31)
* Syncing problems fix when configuring scripts.
* MQTT connection is not interrupted when downloading software.
* Reporting settings on connect only if settings were changed or the device is not in sync.

### v2.0.10 (2021-02-11)
* Firmware download is automatically resumed.

### v2.0.9 (2021-01-27)
* Added GPS over MQTT feature

### v2.0.8 (2020-11-02)
* Upgraded Eclipse PAHO MQTT C client library from 1.3.1 to 1.3.6
* Added support for older firmware when compiled with toolchain 7.4.0 and ModulesSDK 1.8.0

### v2.0.7 (2020-09-11)
* bugfix: Downgraded Eclipse Paho MQTT C client library from 1.3.4 to 1.3.1 again to fix connectivity issues

### v2.0.6 (2020-07-06)
* Upgraded Eclipse Paho MQTT C client library from 1.3.1 to 1.3.4
* bugfix: Avoid infinite loop situation when IR/Notify fails
* bugfix: Fix reconnection issue when WAN network fully changed
* bugfix: Replace non-utf8 characters on IR/Notify with Unicode REPLACEMENT CHARACTER

### v2.0.5 (2020-05-28)
* Support change password feature
* bugfix: Sanitize UM version like 'v1.0.0' to '1.0.0'
* Join debug log messages into single line to reduce verbosity

### v2.0.4 (2020-04-16)
* Added WiFi network and network6 calculated fields for firmware 6.2.x


### v2.0.3 (2020-03-30)
* bugfix: Fix stol error when mobile data usage goes over 2GB
* bugfix: Fix LWT message overwriting real device online status

### v2.0.2 (2020-03-11)
* Handle version number with letters, e.g., '1.0.1 alfa'. It is now reported as '1.0.1.'
* Fix Monitoring bug where the client couldn't get the product title

### v2.0.1 (2020-02-25)
* WebAccess/DMP Client first release