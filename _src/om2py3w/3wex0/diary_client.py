# coding:utf-8
# Author: Jeremiah Zhang
# Email: zhangleisuda@gmail.com
# beta 1.0
import socket

def HELP():
    """ # Dear , Here is the Help Doc:

        1 Input: p/past , print past logs
    """

print HELP.__doc__

# pastlog_keyword = "p"

# Creat socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_address = ('localhost', 8001)
sock.connect(host_address)
#
pastlog_keyword = raw_input("Wanna read past logs? Input p --->")
sock.sendto(pastlog_keyword, host_address)

back_message = sock.recv(1024)
print "Here is the past logs:---> \n" , back_message
sock.close()
