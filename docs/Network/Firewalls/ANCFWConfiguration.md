# ANC Firewall Configuration
---
## FW01.ancollege.local
---
### Summary
--- 
ANC utilizes two Netgate XG-7100-1U security appliances. These devices leverage pfSense as its core. The following information is geared towards ANC System Administrators. This documents is to serve as a central location for the current system configuration of the two security appliances. All changes to the devices will be tracked using Github.

### FW01
---
PASSWORD: !@Br34k3r@!
Hostname: fw01
Domain: ancollege.local
Primary DNS: 8.8.8.8
Secondary DNS: 8.8.4.4
NTP Server: chronos1.umt.edu
Time Zone: America/Denver
WAN Type: Static
WAN IP Address: 66.113.60.242/28
