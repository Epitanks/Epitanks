import socket
import threading
from threading import RLock
from datetime import datetime
import time

verrou = RLock()
gamers = []
mapp = "1 2 3 4 5"
class ClientThread(threading.Thread):
	def __init__(self, ip, port, clientsocket):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.clientsocket = clientsocket
		print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

	def run(self):
		global mapp
		print("Connection de %s %s" % (self.ip, self.port,))
		print(str(mapp))
		while 1:
			self.clientsocket.send(mapp)
			r = self.clientsocket.recv(2048)
			if (r == 'a'):
				mmap += "a"
			with verrou:
				print(r + " send by " + str(self.ip) + " " + str(self.port))
				mmap = str(r)
		print("Client deconnecte...")



tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

t1 = datetime.now()
while (len(gamers) < 2):
	tcpsock.listen(10)
	print("En ecoute...")
	(clientsocket, (ip, port)) = tcpsock.accept()
	tmp = "Connected with " + str(ip) + " " + str(port)
	clientsocket.send(tmp)
	gamers.append(ClientThread(ip, port, clientsocket))

for gamer in gamers:
	gamer.start()
	time.sleep(0.3)
