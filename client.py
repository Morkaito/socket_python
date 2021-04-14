import socket

HOST = '127.0.0.1'
PORT = 64432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(( HOST, PORT ))
    s.sendall(b'Hello World Server =D')
    data = s.recv(1024)

print('[\033[0;32m+\033[0;0m] - Data received ==>', repr(data))