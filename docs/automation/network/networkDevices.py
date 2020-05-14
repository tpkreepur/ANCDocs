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

#sw01 = switch("Test01","10.16.86.100","switches")
#sw01.showName()

for host in root.findall('item'):
	name = host.find('device').text
	ipaddress = host.find('host').text
	print(name + "," + ipaddress)