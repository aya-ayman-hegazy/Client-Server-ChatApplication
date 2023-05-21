import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
host = 'localhost'
port = 20095
ThreadCount = 0
# try to
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(8)
# handiling multiple clients requests
def multi_threaded_client(connection):
    connection.send(str.encode('welcome to server to quit please type ""CLOSE CONNECTION""'))
    while True:
        data = connection.recv(2048)


        if data:
            connection.sendall(data.upper())
        else:
            break

    connection.close()
while True:
    # accept incomming connection from TCP
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    # establish new client thread
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()