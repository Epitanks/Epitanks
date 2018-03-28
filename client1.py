import pygame, sys
from pygame.locals import *
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 1111))
a = s.recv(1000)
print(a)

def sendMsg(msg):
	s.send(msg.encode())
	
while 1:
	a = s.recv(1000)
	print(a)
	time.sleep(1)
	sendMsg(a)
