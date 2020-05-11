#import network devices from PRTG Report
import xml.etree.ElementTree as ET
tree = ET.parse('networkDevices.xml')
root = tree.getroot()

for host in root.findall('item'):
	ipaddress = host.find('host').text
	print(ipaddress)