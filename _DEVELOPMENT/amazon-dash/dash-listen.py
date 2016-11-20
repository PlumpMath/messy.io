from scapy.all import *

def dashPushed(name):
	print "Pushed " + name

def arp_display(pkt):
	if pkt[ARP].op == 1: #who-has (request)
		if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
			if pkt[ARP].hwsrc == '00:bb:3a:5e:97:c1': # Huggies
				dashPushed('smartWater1')
			elif pkt[ARP].hwsrc == '10:ae:60:00:4d:f3': # Elements
				dashPushed('smartWater2')
			else:
				print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=0)
 
