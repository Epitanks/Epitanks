# chat_client.py

import sys
import socket
import select
import time
from game import Game
from game import WindowManager
from game import Players
from game import Menu
from game import Input


class Client:
	def __init__(self, w, ip, port):
		self.w = w
		self.host = ip
		self.port = int(port)
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.me = ""

	#	self.window = window

	def connection(self):
		self.s.settimeout(2)
		try:
			self.s.connect((self.host, self.port))
		except:
			print 'Unable to connect'
			sys.exit()
		print 'Connected to remote host.'
		self.me = str(self.s.getsockname()[0]) + ":" + str(self.s.getsockname()[1])
		print(self.me)

	def game_loop(self):
		self.connection()
		players = Players.Players(self.w)
		game = Game.Game(self.w, players)
		players.setMe(self.me)
		i = 0

		while i < 2:
			game.printwaiting()
			game.geteventtab()
			socket_list = [sys.stdin, self.s]
			ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0.05)
			for sock in ready_to_read:
				if sock == self.s:
					# incoming message from remote server, s
					data = sock.recv(4096)
					if not data:
						print '\nDisconnected from server'
						sys.exit()
					else:
						data = data.split('\n')
						for enemy in data:
							enemy = enemy.split('#')
							if (len(enemy) > 3):
								players.setNewEnemy(enemy[0], enemy[1], enemy[2], enemy[3], 90)
								i += 1
		game.clearbackground()
		game.display()
		while 1:
			socket_list = [sys.stdin, self.s]
			# Get the list sockets which are readable
			ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0.05)

			for sock in ready_to_read:
				if sock == self.s:
					data = sock.recv(4096)
					if not data:
						print '\nDisconnected from server'
						sys.exit()
					else:
						if data[0] == '#':  # position tanks
							tmp_split = data[1:].split('#')
							game.moveEnemy(tmp_split[0], tmp_split[1], tmp_split[2], tmp_split[3])
						elif data[0] == '&':  # balles
							tmp_split = data[1:].split('&')
							game.bullets.addEnemy(tmp_split[0], tmp_split[1], tmp_split[2], tmp_split[3])
						elif data[0] == '$':  # Game
							tmp_split = data[1:].split('$')
							game.players.disconnect(tmp_split[0])
				else:
					game.display()
					msg = game.getevent()
					if msg is not None and msg != "error":
						if (msg[0] != '&'):
							msg = "#" + self.me + '#' + msg + "#"
						self.s.send(msg)


if __name__ == "__main__":
	if len(sys.argv) < 1:
		sys.exit()
	window = WindowManager.WindowManager()

	menu = Menu.Menu(window)
	menu.start()
	ip, port = menu.getInput()
	client = Client(window, ip, port)
	sys.exit(client.game_loop())
