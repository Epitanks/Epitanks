import pygame, sys
from pygame.locals import *
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 1111))

def sendMsg(msg):
	s.send(msg.encode())
	
a = s.recv(1000)
print(a)
sendMsg(a)
