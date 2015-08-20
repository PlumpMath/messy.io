#!/usr/bin/env python 

import socket 
from scapy.all import *

def dashPushed(name):
	print "Pushed " + name

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port where the server is listening
	server_address = ('localhost', 50001)
	print >>sys.stderr, 'connecting to %s port %s' % server_address
	sock.connect(server_address)

	try:
		# Send data
		message = 'pushed ' + name
		print >>sys.stderr, 'sending "%s"' % message
		sock.sendall(message)

	finally:
		print >>sys.stderr, 'closing socket'
		sock.close()
				
def arp_display(pkt):
	if pkt[ARP].op == 1: #who-has (request)
		if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
			print "ohARP"
			if pkt[ARP].hwsrc == '00:bb:3a:5e:97:c1': 
				print "hoSS#$#"
				dashPushed('smartWater1')
			elif pkt[ARP].hwsrc == '10:ae:60:00:4d:f3': # Elements
				dashPushed('smartWater2')
			else:
				print "ARP Probe from unknown device: " + pkt[ARP].hwsrc


sniff(prn=arp_display, filter="arp", store=0, count=0)


