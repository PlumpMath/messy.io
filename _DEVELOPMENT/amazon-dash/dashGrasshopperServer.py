#!/usr/bin/env python 

import re, sys, socket

try:
	backlog = 5 
	size = 1024 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', 50001)
	print >>sys.stderr, 'starting up on %s port %s' % server_address
	sock.bind(server_address)

	sock.listen(backlog) 

	pushed = False

	while True: 
		client, address = sock.accept() 

		try:
			data = client.recv(size) 
			if data: 
				if 'pushed' in data:
					pushed = True
				if 'ping' in data:
					if pushed:
						data = 'yes'
						pushed = False
					else:
						data = 'no'
				print client
				print address
				print data
				client.sendall(data)
			else:
				break

		finally:
			client.close()

finally:
	sock.close()
