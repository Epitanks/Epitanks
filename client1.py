# chat_client.py

import sys
import socket
import select
import time
from game import move


def chat_client():
	if len(sys.argv) < 3:
		print 'Usage : python chat_client.py hostname port'
		sys.exit()

	host = sys.argv[1]
	port = int(sys.argv[2])
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	print(s.type + s.family)
	# connect to remote host
	try:
		s.connect((host, port))
	except:
		print 'Unable to connect'
		sys.exit()

	print 'Connected to remote host. You can start sending messages'
	me = str(s.getsockname()[0]) + ":" + str(s.getsockname()[1])
	print(me)

	game = move.Game()
	i = 0
	while i < 2:
		socket_list = [sys.stdin, s]
		ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0.05)
		for sock in ready_to_read:
			if sock == s:
				# incoming message from remote server, s
				data = sock.recv(4096)
				if not data:
					print '\nDisconnected from chat server'
					sys.exit()
				else:
					data = data.split('\n')
					for enemy in data:
						enemy = enemy.split('#')
						if (len(enemy) > 3):
							game.setNewEnemy(enemy[0], enemy[1], enemy[2], enemy[3])
							i += 1


	while 1:
		socket_list = [sys.stdin, s]
		# Get the list sockets which are readable

		ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0.05)

		for sock in ready_to_read:
			if sock == s:
				# incoming message from remote server, s
				data = sock.recv(4096)
				if not data:
					print '\nDisconnected from chat server'
					sys.exit()
				else:
					if data[0] == '#':
						tmp_split = data[1:].split('#')
						game.setennemies(tmp_split[0], tmp_split[1], tmp_split[2])
			else:
				# user entered a message
				if game.getevent() is not None:
					msg = "#" + me + '#' + game.getpos()
					s.send(msg)

if __name__ == "__main__":
	sys.exit(chat_client())
