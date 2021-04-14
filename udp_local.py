import socket, argparse
from datetime import datetime

MAX_BYTES = 65535

def server(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('127.0.0.1',port))
	print('Servidor escutando em {}'.format(sock.getsockname()))
	while True:
		data, address = sock.recvfrom(MAX_BYTES)
		text = data.decode('ascii')
		print('O cliente {} diz {!r}'.format(address, text))
		text = 'Seus dados tem {} bytes'.format(len(data))
		data = text.encode('ascii')
		sock.sendto(data, address)

def client(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	text = 'O tempo e {}'.format(datetime.now())
	data = text.encode('ascii')
	sock.sendto(data, ('127.0.0.1',port))
	print('O OS atribui este enderço {}'.format(sock.getsockname()))
	data, address = sock.recvfrom(MAX_BYTES)
	text = data.decode('ascii')
	print('O servidor {} respondeu {}'.format(address, text))

if __name__ == '__main__':
	choices = {'client': client, 'server': server}
	parser = argparse.ArgumentParser(description='UDP local protocolo')
	parser.add_argument('role', choices=choices, help='O papel a desempenhar')
	parser.add_argument('-p', metavar='PORT', type=int, default=1060,
						help='Porta do protocolo')
	args = parser.parse_args()
	function = choices[args.role]
	function(args.p)
