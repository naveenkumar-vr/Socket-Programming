import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = '172.16.81.92'
port=1239
address = (ip, port)
client.connect(address)
print "connected"
client.send("8,7,6,5,4,3,2,2,1")
print "sent"
print client.recv(1024)
