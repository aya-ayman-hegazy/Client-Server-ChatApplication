import socket
host = 'localhost'
port = 20095
size= 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
data = s.recv(size)
if len(data) :
    print(data.decode('utf-8'))
data = " "
while len(data):
    message = input('PLEASE ENTER YOUR MESSAGE :  ')
    s.send(message.encode('utf-8'))
    data = s.recv(size)
    print('OUTPUT FROM SERVER:', data.decode('utf-8'))
    if message == "CLOSE CONNECTION":
        data = ''
s.close()