#!/usr/bin/env python
import rospy
import socket
import std_msgs
from ein.msg import EinState
from ein.msg import EinConsole
import os

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

def main():
    rospy.init_node("aibo_cognex", anonymous=True)
    self.forth_command_publisher = rospy.Publisher("%s/forth_commands" % base_topic, 
                                                       std_msgs.msg.String, queue_size=10)



def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if data: print data
        #conn.send(data)  # echo
conn.close()
