# coding:utf-8
# Author: Jeremiah Zhang
# Email: zhangleisuda@gmail.com
# beta 1.0

import socket
import jeremiah_diary

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_address = ('localhost', 8001)
sock.connect(host_address )


log_name, log_content = jeremiah_diary.read_diary() # past logs
sock.sendall(log_name)
sock.sendall(log_content)

back_message = sock.recv(1024)
print "this is the message from server" , repr(back_message)
sock.close()
