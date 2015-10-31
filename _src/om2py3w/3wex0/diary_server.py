# coding:utf-8
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_address = ('localhost', 8001)
sock.bind(host_address)
sock.listen(3)

while True:
    connection, address = sock.accept()
    receive_message= connection.recv(1024)      # reveive message from client
    print receive_message

    back_message = "Dear Jeremiah See you next time! >-<"   # send message to client
    connection.sendall(back_message)

connection.close()