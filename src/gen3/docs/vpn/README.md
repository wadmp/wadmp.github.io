---
prev: ../device-management/device-configuration/
next: ./overview/
---

# Introduction to WADMP VPN Service

WADMP VPN is a secure networking feature designed to facilitate encrypted communication between industrial routers, IoT gateways, and the WebAccess/DMP platform. By leveraging WireGuard, WADMP VPN ensures a secure and private connection for remote device management, configuration, and data transfer.

As part of the WADMP GEN 3 ecosystem, this feature simplifies the deployment of VPN connections without requiring complex manual configurations. It provides a centralized management interface that allows administrators to set up, monitor, and troubleshoot VPN connections across multiple devices efficiently.

WADMP VPN utilizes WireGuard, a modern and high-performance VPN protocol known for its simplicity, speed, and strong cryptographic security. The service enhances cybersecurity by enforcing strong encryption, authentication mechanisms, and secure tunneling, reducing the risk of data breaches and unauthorized access.

This section will guide you through the key functionalities of WADMP VPN, its setup process, and best practices for ensuring secure and reliable connectivity within your network infrastructure.

- Start by navigating to the title panel and selecting the VPN section.
<p align="center">
  <img src="../images/vpn/dashboard_vpn.png" alt="VPN Selection">
</p>

- Click the INITIALIZE button to start your 31-day free trial with 100MB of starting data for your company. If you don’t upgrade to the premium company plan, the feature will be disabled after the trial period.
  ![VPN Initialize](../images/vpn/vpn_initialize.png)

- In the initialization form when configuring a VPN, selecting the correct network address is crucial. The VPN address defines the entire network for the company, including all connected devices. This address must be specified in CIDR notation, which determines the size of the network and how many devices can be accommodated.

  ⚠️ Note, that if VPN is initialized for your company, the number of VPN Devices is also maximum number of all devices that can be added to the Company.

- Additionally, the CIDR range and Addresses per Device settings influence the total number of available device connections. As you adjust these values, the system automatically recalculates the maximum number of devices that can be supported within the network.

- Next, complete the initialization form with your corresponding configuration. Once done, click the Initialize button to proceed.

![VPN Initialize](../images/vpn/vpn_initialize_form.png)

- For detailed information on billing, go to [Billing](../companies/billing/) and navigate to the VPN Billing Summary section.
