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

	# connect to remote host
	try:
		s.connect((host, port))
	except:
		print 'Unable to connect'
		sys.exit()

	print 'Connected to remote host. You can start sending messages'

	game = move.Game()

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
					#    print data
					if data[0:3] != "[127":
						tmp_split = data.split(':')
						game.displayennemies(tmp_split[0], tmp_split[1])
					sys.stdout.write(data)
					sys.stdout.write('[Me] ')
					sys.stdout.flush()

			else:
				# user entered a message
				if game.getevent() is not None:
					msg = game.getpos()
					s.send(msg)


if __name__ == "__main__":
	sys.exit(chat_client())
