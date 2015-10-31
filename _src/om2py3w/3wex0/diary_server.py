# coding:utf-8
import socket
import jeremiah_diary

pastlog_keyword = "p"

# main
def main():
    # creat
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host_address = ('localhost', 8001)
    # bind
    sock.bind(host_address)
    # listen
    sock.listen(3)

    # interact

    while True:
        print "\n Now Please input"

        connection, address = sock.accept()

        data = connection.recv(1024)      # reveive message from client
        print "You have received  message from {0}".format(data)

        if data == "p":
            past_logs = jeremiah_diary.read_diary()
            connection.sendto(past_logs, address) # print past logs
            # write new logs

        connection.close()

if __name__ == '__main__':
    main()