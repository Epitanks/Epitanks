import socket
import threading
from threading import RLock
from datetime import datetime
from Queue import Queue
import time

verrou = RLock()
gamers = []

class ClientThread(threading.Thread):
	def __init__(self, ip, port, clientsocket, queue):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.clientsocket = clientsocket
		self.queue = queue
#		print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))
		print("Connection de %s %s" % (self.ip, self.port,))

	def run(self):
		self.clientsocket.send(self.msg)
		self.msg = self.clientsocket.recv(2048)
		with verrou:
			print(self.msg + " send by " + str(self.ip) + " " + str(self.port))



tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

t1 = datetime.now()
while (len(gamers) < 2):
	tcpsock.listen(10)
	print("En ecoute...")
	(clientsocket, (ip, port)) = tcpsock.accept()
	gamers.append(ClientThread(ip, port, clientsocket, queue))
	

for gamer in gamers:
	gamer.start()
	time.sleep(0.5)

for gamer in gamers:
	gamer.join()