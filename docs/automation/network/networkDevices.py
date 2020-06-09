#import network devices from PRTG Report
import xml.etree.ElementTree as ET
tree = ET.parse('networkDevices.xml')
root = tree.getroot()

class netDevice:
	def __init__(self, hostname, ipAddress, group):
		self.hostname = hostname
		self.ipAddress = ipAddress
		self.group = group

	def showName(self):
		print("Device Hostname: " + self.hostname)

	def showIP(self):
		print("Device IP Address: " + self.ipAddress)

	def showGroup(self):
		print("Device Group: " + self.group)

class switch(netDevice):
	pass

class router(netDevice):
	pass

for host in root.findall('item'):
	ipaddress = host.find('host').text
	print(ipaddress)