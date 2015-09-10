import socket
import json
import time
"""
Testing the way OVSDB receives json RPC from a client 
"""
value = {'method':'echo','id':'echo','params':[]}

def pingSwitch(IP, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP,port))


	print "Sending JSON to server ->"
	s.send(json.dumps(value))

	result = json.loads(s.recv(1024))
	print "Server replied with the following"
		
	print "======================"

	print str(result)
	
	print "======================"
	time.sleep(2)

while True:
	pingSwitch("127.0.0.1",6640)


s.close()
