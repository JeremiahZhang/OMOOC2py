# coding=utf-8
# refer https://docs.python.org/2/library/socket.html?highlight=socket#example
import socket

HOST = 'localhost'# the remote host
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('hello, world')
data = s.recv(1024)
s.close()
print "received", repr(data)