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
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host_address = ('localhost', 8001)
sock.connect(host_address)
# continue interact
done = False
while done==False:
    pastlog_keyword = raw_input("Please write here Dear! --->")
    sock.sendto(pastlog_keyword, host_address)
    back_message = sock.recvform(1024)
    print back_message

sock.close()
