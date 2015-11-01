# -*- coding: utf-8 -*-
import socket
import sys

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

# communicate with the client
while 1:
    # receive from client
    d = s.recvfrom(1024)
    data = d[0] # client message
    addr = d[1] # client address addr = (host, port)

    if not data:
        break

    reply = "ok...--->" + data

    s.sendto(reply, addr)
    print "message[ " + addr[0] + ":" + str(addr[1]) + "] - " + data.strip()

s.close()
