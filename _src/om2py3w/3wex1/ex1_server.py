# coding=utf-8
# refet to https://docs.python.org/2/library/socket.html?highlight=socket#example
import socket

HOST = 'localhost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print 'connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()