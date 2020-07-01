# LDAP
---
## What is LDAP?
---
LDAP stands for Lightweight Directory Access Protocol. As the name suggests, it is a lightweight client-server protocol for accessing directory services, specifically X. 500-based directory services. LDAP runs over TCP/IP or other connection oriented transfer services.

### Whats the difference between this and Windows Active Directory (AD)
Active Directory is the directory service database to store the organizational based data,policy,authentication etc whereas ldap is the protocol used to talk to the directory service database that is ad or adam. LDAP sits on top of the TCP/IP stack and controls internet directory access. It is environment agnostic.

#### Short answer:
--- 
AD is a directory services database, and LDAP is one of the protocols you can use to talk to it.

### What the hell is SLAPD?
--- 
The SLAPD (Standalone LDAP Daemon) and SLURPD (Stand-alone LDAP update replication daemon) originally evolved within the long-running project that developed the LDAP protocol.

Today, many LDAP Server Implementations are derived from the same code base of the original SLAPD and/or evolutions of it.

More info about LDAP can be found in the [OpenLDAP Admin' Guide](https://openldap.org/doc/admin24/guide.html).

## Installation (Desired State/ANC BASELINE LDAP)
---

### Prerequisites
---
1. Ubuntu 20.04 LTS
	- slapd, ldap-utils

### Install And Configure
---

#### install OpenLDAP
```bash
root@dlp sudo apt -y install slapd ldap-utils`

##### set LDAP admin password during installation like follows
 +--------------------------| Configuring slapd |-------------------------+
 | Please enter the password for the admin entry in your LDAP directory.  |
 |                                                                        |
 | Administrator password:                                                |
 |                                                                        |
 | ______________________________________________________________________ |
 |                                                                        |
 |                                 <Ok>                                   |
 |                                                                        |
 +------------------------------------------------------------------------+
```

#### confirm settings
```bash
root@dlp:~# sudo slapcat

dn: dc=srv,dc=world
objectClass: top
objectClass: dcObject
objectClass: organization
o: srv.world
dc: srv
structuralObjectClass: organization
entryUUID: 102bac62-27a4-103a-853d-bb5d839899a7
creatorsName: cn=admin,dc=srv,dc=world
createTimestamp: 20200511072332Z
entryCSN: 20200511072332.363512Z#000000#000#000000
modifiersName: cn=admin,dc=srv,dc=world
modifyTimestamp: 20200511072332Z

dn: cn=admin,dc=srv,dc=world
objectClass: simpleSecurityObject
objectClass: organizationalRole
cn: admin
description: LDAP administrator
userPassword:: e1NTSEF9ekcwNmk4Ny9OZjdEL2RGUlhDcHRWV2hxaVZiaGo0b3c=
structuralObjectClass: organizationalRole
entryUUID: 10303c6e-27a4-103a-853e-bb5d839899a7
creatorsName: cn=admin,dc=srv,dc=world
createTimestamp: 20200511072332Z
entryCSN: 20200511072332.393446Z#000000#000#000000
modifiersName: cn=admin,dc=srv,dc=world
modifyTimestamp: 20200511072332Z
```

#### add base dn for Users and Groups
```bash
root@dlp:~# vi base.ldif
#### create new change to your own suffix for the field [dc=srv,dc=world]
dn: ou=people,dc=srv,dc=world
objectClass: organizationalUnit
ou: people

dn: ou=groups,dc=srv,dc=world
objectClass: organizationalUnit
ou: groups 

root@dlp:~# ldapadd -x -D cn=admin,dc=srv,dc=world -W -f base.ldif
Enter LDAP Password:     # LDAP admin password (set in installation of openldap)
adding new entry "ou=people,dc=srv,dc=world"

adding new entry "ou=groups,dc=srv,dc=world"
```

### Add Users
---

### Confiugure Clients
---

### LDAP over SSL/TLS
---

### Configure LDAP client (AD)
---

### OpenLDAP Replication
---

### Multi-master replication
---

### LDAP account manager
---