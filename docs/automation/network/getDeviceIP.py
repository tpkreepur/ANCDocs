#PRTG uses API calls to get data. As of 5/11/20 PRTG does not
#allow for reports to display the ip address of the devices
#that we need for Ansible.

https://ancnetmon:8443/api/\
networkDevices.xml?content=devices\
&columns=device,host\
&count=*\
&username=ansible&passhash=275124935\
&tags=networkDevice&show=text

https://ancnetmon:8443/api/\
table.xml?content=devices\
&columns=device,host\
&sortby=host\
&count=*\
&username=ansible&passhash=275124935


https://ancnetmon:8443/api/\
/api/getobjectproperty.htm?id=objectid&name=propertyname&show=text\
&username=ansible&passhash=275124935