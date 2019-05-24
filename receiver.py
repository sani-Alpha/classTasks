#!/usr/bin/python3

import socket

ip="13.234.66.67"
port=8888

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((ip,port))

while True:
    msg=s.recvfrom(100)
    print(msg)
    s.sendto("1".encode('ascii'),msg[1])
