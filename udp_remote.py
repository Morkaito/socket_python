import socket, argparse, sys, random

MAX_BYTES = 65535

def server(hostname, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((hostname, port))
	print('Servidor escutando em {}'.format(sock.getsockname()))
	while True:
		data, address = sock.recvfrom(MAX_BYTES)
		if random.random() < 0.5:
			print('Fingindo não responder o cliente')
			continue
		text = data.decode('ascii')
		print("O cliente em {} diz {}".format(address, text))
		text = 'Seus dados tem {} bytes'.format(len(data))
		data = text.encode('ascii')
		sock.sendto(data, address)

def client(hostname, port):
	hostname = sys.argv[2]
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.connect((hostname, port))
	print('O OS atribui o endereco {}'.format(sock.getsockname()))

	delay = 0.1
	text = 'Esta e a mensagem'
	data = text.encode('ascii')
	while True:
		sock.send(data)
		print("Aguardando o server responder")
		sock.settimeout(delay)
		try:
			sock.recv(MAX_BYTES)
		except:
			delay *= 2
			if delay > 2.0:
				raise RuntimeError
		else:
			break;
	print("O servidor diz {}".format(data.decode('ascii')))

if __name__ == '__main__':
	choices = {'client': client, 'server': server}
	parser = argparse.ArgumentParser(description='UDO remote client and server')
	parser.add_argument('role', choices=choices, help='Qual papel desempenhar')
	parser.add_argument('host', help='IP do servidor ou client')
	parser.add_argument('-p', type=int, metavar='N', default=1060,
						help='Port padrao do server')
	args = parser.parse_args()
	function = choices[args.role]
	function(args.host, args.p)


	