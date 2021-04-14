import socket
import selectors
import types 

c=0

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print("[\033[0;36m*\033[0;0m] - Received...")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    print("\nEvents accept: ",events)
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    print("\nMask conn: ",mask)
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        print("Event Read")
        if recv_data:
            data.outb += recv_data
        else:
            print("\n[\033[0;31!\033[0;0m] - Closing connection to ==> {}".format(data.addr))
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        print("Event Write")
        if data.outb:
            print('\n Echoing: {} to ==> {}'.format(repr(data.outb), data.addr))
            sent = sock.send(data.outb)
            print("\n Sent",sent)
            data.outb = data.outb[sent:]

sel = selectors.DefaultSelector()

host = '127.0.0.1'
port = 2244

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind(( host,port ))
lsock.listen()
print("\n[\033[0;36m*\033[0;0m] - Server listering ==> \t{}:{}\n".format(host,port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

while c < 5:
    events = sel.select(timeout=None)
    print("Events: ",events)
    for key, mask in events:
        c+=1
        print("\nKey {}, mask {}".format(key, mask))
        if key.data is None:
            accept_wrapper(lsock)
        else:
            service_connection(key, mask)
            