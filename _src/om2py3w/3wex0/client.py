# -*- coding: utf-8 -*-
import socket
import sys

def help():

    """ # this is the help doc:

                        1- read past logs?      enter:--->  p
                        2- want leave ?          enter:--->  e
                        3- help doc?               enter:--->  h

    """
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print "Failed to create socket"
    sys.exit()

host = "localhost"
port = 8888

print "please enter h to see the help.-->"

while 1:
    msg = raw_input("Enter message to send: --->   ")

    try :
        # send the whole string
        s.sendto(msg, (host, port)) # send to serve

        # receive data from server
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print "server reply: ---> " + reply

    except socket.error, msg:
        print "error code: " + str(msg[0]) + " message " + msg[1]
        sys.exit()
