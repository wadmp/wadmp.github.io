# Release Notes for Client Router App:

## Latest version:

### v3.3.0 (2025-09-25)
- Added reporting of active network interfaces.
- Added reporting of WAN interface name, firmware version, and WADMP client version.
- Added error reporting for synchronization failures due to insufficient space.
- Improved synchronization speed for configuration profiles.
- Fixed issue where the client exhausted all file descriptors, causing it to be unable to read certain metrics after a long reporting period.
- Fixed temperature reporting showing absolute zero instead of null when reading failed.

## Download:

We recommend always using the most up-to-date version of the client.

[Download the latest client and Application Note (Manual)](https://icr.advantech.com/products/software/user-modules#webaccessdmp-client-3xx)

The client router app can also be upgraded via WebAccess/DMP.

## Previous versions:

### v3.2.2 (2025-06-03)

- Added a new CA to default truststore.
- Improved router application installation process.
- Fixed iptables rule duplication.
- Resolved rare issue causing unintended deletion of config profiles upon client restart.
- Fixed VPN traffic denial caused by default firewall settings (applies to firmware version 6.5.2 and newer).

### v3.2.1 (2025-03-27)

- Added support for 'v1' device platform (ICR-16xx).

### v3.2.0 (2025-03-12)

- Added support of VPN features.
- Fixed services sometimes not being restarted after their configuration was changed.
- Fixed incorrect IP being sometimes reported as WAN IP Address.
- Fixed installation of router apps for firmware versions below 6.4.0.
- Fixed metrics sometimes incorrectly reported as "changed".

### v3.1.2 (2024-11-28)

- Improved router application installation.
- Lowered warning message count when loading configuration profile.

### v3.1.1 (2024-10-10)

- Added support for device secure platform (ICR-270x-S1, ICR-283x-S1).
- Added support for new firmware version 6.5.0.
- Improved reading of WanIp field.
- Improved reading of configuration profile to be more resilient.

### v3.1.0 (2024-07-22)

- Upgraded openssl and paho.mqtt libraries.
- Added watchdog.
- Added user role management.
- Reduced missing GPS metrics message count in syslog.
- Removed cumulative metrics from client side.

### v3.0.1 (2023-12-15)

- Decreased the retry timeout for device reconnection.
- Added an automatic configuration of bootstrap address to 3.x.x instance.

### v3.0.0 (2023-09-01)

- WebAccess/DMP Client GEN3 first release.
