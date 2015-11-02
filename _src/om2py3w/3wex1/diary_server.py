# coding:utf-8
import socket
import jeremiah_diary

pastlog_keyword = "p"

# main
def main():
    # creat
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host_address = ('localhost', 8001)
    # bind
    sock.bind(host_address)

    # interact

    while True:
        print "Please Wait:---> "

        data = sock.recvfrom(1024)      # reveive message from client
        print "You have received  message from {0}".format(address)

        if data == "p":
            past_logs = jeremiah_diary.read_diary()
            sock.sendto(past_logs, address) # print past logs
        if data == "h":
            help_doc = "balabala"
            sock.sendto(help_doc, address)
        else:
            diary_name = "jeremiah_diary.log"
            diary_writer = open(diary_name, "a+")
            diary_writer.write(data)
            back_message = "Continue to Write:--->"
            sock.sendto(back_message, address)
        # connection.close()

if __name__ == '__main__':
    main()