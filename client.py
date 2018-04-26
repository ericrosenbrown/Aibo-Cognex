#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5011
BUFFER_SIZE = 1024

xAibo = 0
yAibo = 0
oAibo = 20 #orientation of aibo in degrees
xTar = 5 
yTar = 6

MESSAGE = str(xAibo) + " " + str(yAibo) + " " + str(oAibo) + " " + str(xTar) + " " + str(yTar) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
    raw_input("type anything")
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
