#!/usr/bin/python3
import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip,int(port)))
    s.settimeout(5)
    print(str(s.recv(1024))).strip('b')


def main():
    ip = input("Enter ip:")
    port = str(input("enter port:"))
    banner(ip, port)
main()
