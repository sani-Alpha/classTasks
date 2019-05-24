#!/usr/bin/python3
import socket

ip="13.234.66.67"
port=8888

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg=input("enter the message to be sent")
n=msg.enocde('ascii')

s.sendto((ip,port))
print(s.recvfrom(1000))
