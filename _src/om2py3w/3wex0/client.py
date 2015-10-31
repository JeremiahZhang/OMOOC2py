# -*- coding: utf-8 -*-
# refer to http://openexperience.iteye.com/blog/145701
if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    import time
    time.sleep(1)
    sock.send('1')
    print sock.recv(1024)
    sock.close()