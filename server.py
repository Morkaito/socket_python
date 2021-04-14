import socket

HOST = '127.0.0.1'
PORT = 64432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(( HOST, PORT ))
    s.listen()
    print('[\033[0;32m+\033[0;0m] - Server listering...')
    conn, addr = s.accept()
    with conn:
        print('\n[\033[0;36m*\033[0;0m] - Conected by ==> {}'.format(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)