#!/usr/bin/env python

import signal
import sys
import socket
import math


class AiboServer():
    def __init__(self):
        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = 5015
        self.BUFFER_SIZE = 20  # Normally 1024, but we want fast response
       
        self.threshold = 5 #plus or minus degrees tolerance on whether to turn or not
        
        self.establish_connection()
        signal.signal(signal.SIGINT, self.signal_handler)
        self.listen_to_cognex()

    def establish_connection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.TCP_IP, self.TCP_PORT))
        self.s.listen(1)
       
        conn, addr = self.s.accept()
        self.conn = conn
        self.addr = addr
        print 'Connection address:', addr

    def signal_handler(self,signal, frame):
        print('You pressed Ctrl+C!')
        self.conn.close()
        sys.exit(0)
    
    def control_aibo(self,data):
        if not data:
            print "No input"
            return
        split_data = data.split(" ")
        aibo_x = split_data[0]
        aibo_y = split_data[1]
        aibo_o = split_data[2]
        target_x = split_data[3]
        target_y = split_data[4]
        print aibo_x, aibo_y, aibo_o, target_x, target_y
        
        xDif = float(aibo_x) - float(target_x)
        yDif = float(aibo_y) - float(target_y)
        target_angle = math.tan(yDif/xDif)
        angle_difference = float(aibo_o)-target_angle
 
        if angle_difference >= self.threshold:
            #send aibo right
            print "right"
        elif angle_difference <= -1*self.threshold:
            print "left"
        else: 
            print "move forward doggy!"

    def listen_to_cognex(self):
        while 1:
            data = self.conn.recv(self.BUFFER_SIZE)
            #if not data: break
            self.control_aibo(data)
            self.conn.send(data)  # echo

aibo_server = AiboServer()
