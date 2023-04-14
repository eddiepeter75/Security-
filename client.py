#!/usr/bin/python3
import socket
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = '192.168.2.46'
host = socket.gethostbyname()
port = 4448

clientsocket.connect((host,port))#host = 192.168.2.46

message = clientsocket.recv(1024)#maximum amount of data through the port
clientsocket.close()
print(message.decode(ascii))