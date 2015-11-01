# -*- coding: utf-8 -*-
import socket
import sys
import jeremiah_diary

def help():

    """ # this is the help doc:

                        1- read past logs?      enter:--->  p
                        2- want leave ?          enter:--->  e
                        3- help doc?               enter:--->  h

    """

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

# UDP SOCKET
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print "socket created! "
except socket.error, msg :
    print "failed to created socket. ERROR code : " + str(msg[0]) + " message " + msg
    sys.exit()

# bind socket to localhost and port
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print "bind failed. error code: " + str(msg[0]) + " message " + msg[1]
    sys.exit()

print "socket bind complete"

def responses():
    if data =="e":
        sys.exit()
    elif data =="p":
        reply = jeremiah_diary.read_diary()
    elif data == "h":
        reply = help.__doc__
    else:
        diary_name = "jeremiah_diary.log"
        diary_writer = open(diary_name, "a+")
        diary_writer.write(data + "\n")
        diary_writer.close()
        reply = "Continue to Write:--->"
    return reply


# communicate with the client
while 1:
    # receive from client
    d = s.recvfrom(1024)
    data = d[0] # client message
    addr = d[1] # client address addr = (host, port)

    reply=responses()

    s.sendto(reply, addr)

    print "message from [ " + addr[0] + ":" + str(addr[1]) + "] is --->" + data.strip()

s.close()
