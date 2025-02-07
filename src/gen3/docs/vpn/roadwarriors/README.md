---
next: ../../device-monitoring/
---

# Roadwarriors

Roadwarriors refer to a VPN configuration designed for mobile users (Windows, Android, macOS, iOS, Linux and basically any device where [WireGuard](https://www.wireguard.com/install/) can be installed) who need secure remote access to a private network from various locations. Unlike site-to-site VPNs, which connect fixed networks, a Roadwarrior setup allows individual devices with dynamic IP addresses to establish encrypted connections over untrusted networks, such as public Wi-Fi or mobile data. This approach ensures secure access to corporate resources, protects sensitive data, and enhances online privacy.

- Start by navigating to the VPN section in the Context Panel, then select the Roadwarriors section.

<p align="center">
  <img src="../../images/vpn/vpn_roadwarrior_panel.png" alt="VPN Road Warriors">
</p>

- Next, add your Roadwarrior by clicking the **ADD ROADWARRIOR** button.

![VPN Road Warriors](../../images/vpn/vpn_roadwarriors_add.png)

- Enter the name and description, then select the specific networks you want your Roadwarrior to be part of.

![VPN Road Warriors](../../images/vpn/vpn_roadwarrior_adding2.png)

- Click the **ADD** button to confirm and proceed.

![VPN Road Warriors](../../images/vpn/vpn_roadwarrior_adding.png)

- Now you have 2 options:

![VPN Road Warriors](../../images/vpn/vpn_roadwarrior_edit.png)

1. You can view your Roadwarrior's details by clicking on its name and specify the configuration here.

- In the Roadwarrior's details, you can edit its configuration, including the name, description, and networks → essentially the same parameters as when it was created. You can also disable/enable or delete it. Below, you’ll find information about its *Data Usage* and *Connection History*.

![VPN Road Warriors](../../images/vpn/vpn_roadwarrior_detail.png)

2. From here, you can view the WireGuard configuration, edit, or delete your Roadwarrior.

- If you choose to view the WireGuard configuration, a form will display your configuration details. You can also download them as a configuration file by clicking the **DOWNLOAD CONFIG FILE** button.

![VPN Road Warriors](../../images/vpn/vpn_roadwarrior_config-file.png)

- **Note that only the creator of the Roadwarrior can view its configuration.**
