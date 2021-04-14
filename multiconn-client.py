import socket
import selectors
import types

msg = ['message 1 from cleint.','message 2 from client.']

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        conn_id = i += 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("\n[\033[0;36m*\033[0;0m] - Connect initial {} to ==> {}".format(conn_id,server_addr))
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(conn_id=conn_id,
                                     msg_total=sum(len(m) for m in msg),
                                     recv_total=0,
                                     messages=msg,
                                     outb=b'')
        sel.register(sock, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        
    

"""def encryption_message(msg):
    key = 18
    letters = 'QAZXSWEDCVFRTGBNHYUJMKILOÇP,.~><:;}][}{ÀÁÂÃÉÈÊÒÓÔÕÙÚÛÎÍÌ@!?/\$()%-_'
    message = msg.upper()
    translated = ''
    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol)
            num += key
            if num >= len(letters):
                num -= len(letters)
            elif num < 0:
                num += len(letters)
            translated += letters[num]
        else:
            translated += symbol
    return translated.encode()
"""