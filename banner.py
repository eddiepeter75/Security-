#!/usr/bin/python3
import socket

s = socket.socket()
ip = input("enter ip:")
port = str(input("enter port:"))

s.connect((ip,int(port)))

print(s.recv(1024))
