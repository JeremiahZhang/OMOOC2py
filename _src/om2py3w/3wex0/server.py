# -*- coding: utf-8 -*-
import socket, sys, os, glob

def main():
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

        reply = responses(data)
        s.sendto(reply, addr)

        print "message from [ " + addr[0] + ":" + str(addr[1]) + "] is --->" + data.strip()

    s.close()

def help():
    """ # this is the help doc:

                        1- read past logs?      enter:--->  p
                        2- want leave ?          enter:--->  e
                        3- help doc?               enter:--->  h
    """

def responses(mydata):
    if mydata =="e":
        sys.exit()
    elif mydata =="p":
        reply = read_diary()
    elif mydata == "h":
        reply = help.__doc__
    else:
        diary_name = "jeremiah_diary.log"
        diary_writer = open(diary_name, "a+")
        diary_writer.write(mydata + "\n")
        diary_writer.close()
        reply = "Continue to Write:--->"
    return reply

def read_diary():
    current_dir = os.getcwd() # 打印之前日志
    os.chdir(current_dir)

    filename_plus_content =""
    for file in glob.glob("*.log"):

        file_content = open(file, "r")
        diary = file_content.read() + "\n"
        filename_plus_content = filename_plus_content + file + "--->: \n" +diary
    return filename_plus_content

if __name__ == '__main__':
    main()