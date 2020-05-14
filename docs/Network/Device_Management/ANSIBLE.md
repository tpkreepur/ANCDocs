# ANC Network Device Mangement
---

## Ansible
---


### Prerequisistes
---

- Ubuntu 20.04 LTS
- Python 3.5 (or higher)
- SSH or SFTP (SSH preferred)

### Installation
--- 

Installs can be done with the OS package manager, pip, or from source. ANC utilizes the Ubuntu package manager as the preferred method of installation. This is to provide ease of installation with as little headaches as possible.

#### Credentials
--- 

username: administrator
password: hd115t42

##### Control Node
--- 

1. Update package manager and update OS kernel.

>`sudo apt update && sudo apt upgrade`

2. Install the common software properties package

>`sudo apt install software-properties-common`

3. Add the Ansible repository

>`sudo apt-add-repository --yes --update ppa:ansible/ansible`

4. Install Ansible from the package manager

>`sudo apt install ansible`

##### Managed Node

---
TODO

### Configuration
---

#### Inventory
--- 

A list of managed nodes. An inventory file is also sometimes called a “hostfile”. 
Your inventory can specify information like IP address for each managed node. An
inventory can also organize managed nodes, creating and nesting groups for easier scaling.

#### Tasks 
--- 

#### Playbooks
---

#### Execution on Control Node
---

Unlike most Ansible modules, network modules do not run on the managed nodes. From a user’s point of view, network modules work like any other modules. They work with ad-hoc commands, playbooks, and roles. Behind the scenes, however, network modules use a different methodology than the other (Linux/Unix and Windows) modules use. Ansible is written and executed in Python. Because the majority of network devices can not run Python, the Ansible network modules are executed on the Ansible control node, where `ansible` or `ansible-playbook` runs.

### Best Practices
---

Below you will find a sample directory layout for Ansible. Please adhere to the best practices unless you have shown adequate reasoning.

```bash
production                # inventory file for production servers
staging                   # inventory file for staging environment

group_vars/
   group1.yml             # here we assign variables to particular groups
   group2.yml
host_vars/
   hostname1.yml          # here we assign variables to particular systems
   hostname2.yml

library/                  # if any custom modules, put them here (optional)
module_utils/             # if any custom module_utils to support modules, put them here (optional)
filter_plugins/           # if any custom filter plugins, put them here (optional)

site.yml                  # master playbook
webservers.yml            # playbook for webserver tier
dbservers.yml             # playbook for dbserver tier

roles/
    common/               # this hierarchy represents a "role"
        tasks/            #
            main.yml      #  <-- tasks file can include smaller files if warranted
        handlers/         #
            main.yml      #  <-- handlers file
        templates/        #  <-- files for use with the template resource
            ntp.conf.j2   #  <------- templates end in .j2
        files/            #
            bar.txt       #  <-- files for use with the copy resource
            foo.sh        #  <-- script files for use with the script resource
        vars/             #
            main.yml      #  <-- variables associated with this role
        defaults/         #
            main.yml      #  <-- default lower priority variables for this role
        meta/             #
            main.yml      #  <-- role dependencies
        library/          # roles can also include custom modules
        module_utils/     # roles can also include custom module_utils
        lookup_plugins/   # or other types of plugins, like lookup in this case

    webtier/              # same kind of structure as "common" was above, done for the webtier role
    monitoring/           # ""
    fooapp/               # ""
```
