# coding:utf-8
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_address = ('localhost', 8001)
sock.connect(host_address )

receive_message = "Let go! "    # send message to server
sock.sendall(receive_message)

back_message = sock.recv(1024)
print "this is the message from server" , repr(back_message)
sock.close()
