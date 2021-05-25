import socket
def sorting(data):
    arr = data.split(',')
    for i in arr:
        i = int(i)
    arr.sort()
    for i in arr:
        i=str(i)
    d=','.join(arr)
    return d
IP = ""
PORT= 1239

server = socket.socket(socket.AF_INET. socket.SOCK_DGRAM)
server.bind((IP, PORT))
while True:
    data, addr = server.recvfrom(1024)
    print "Message: ", data
    break
print addr

server.sendto(sorting(data).addr)

print "Message sent"
