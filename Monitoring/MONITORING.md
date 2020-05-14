# ANC Network Monitoring

## PRTG Network Monitor

### Overview

ANC uses PRTG Network Monitor by Paessler to track, inventory, and monitor critical services proviced my ANC IT. It is imperative that the network monitoring system remains updated and correctly configured. ANC IT uses SNMP, NetFlow, sFlow, and WMI sensors to monitor device health and to notify ANC IT of any problems that may arise. It is not only the PRTG software that is used for monitoring. 

ANC IT leverages the use of bash, Powershell, and Python scripts to update various aspects of the ANC IT Network. These scripts can be found on the local machine or on the [ANC Github](https://github.com/tpkreepur/ANCDocs/). 

The next sections below are the questions that were asked when developing the network monitoring system.

### Prereqs

- Credentials for the target system in the parent group or device settings
- WMI enabled on probe and target computer for Windows systems
- SNMP enabled on the target device
- Remote Registry Windows service enabled on the target computer
- Remote Procedure Call Windows service enabled on the target computer

### What needs to be monitored in my IT infrastructure?

- Key infrastructure such as core routers, switches,VPN, firewalls, and basic network
	services such as the Dynamic Host Configuration Protocol (DHCP), the
	Domain Name System (DNS), and authentication like the 
	Lightweight Directory Access Protocol (LDAP) and Active Directory Domain Services (ADDS).




### How can I retrieve the needed information? Which technologies and credentials are required?

### Which notification methods do I want to use to get alerted if there is something wrong?

## Monitoring Info
## SNMP Info

## Windows Server Info

## Linux Server Info

## Network Device Info

### General Info

### HP Devices

### Cisco Devices

