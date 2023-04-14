#!/usr/bin/python3
import socket
##created socket object stored socket type and family
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host= '192.168.2.160'
host = socket.gethostbyname()
port = 4448

##binded address
serversocket.bind((host, port))#host=192.168.2.46

##listener
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print("connection received" % str(address))
    message = 'Thank you for connecting to this server' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()