import pygame, sys
from pygame.locals import *
import WindowManager
import Button
import Input
import os
import subprocess
import time


class Menu:
	def __init__(self, w):
		self.w = w
		self.background = pygame.image.load('Assets/Accueil.png')
		self.keys = [KEYUP, KEYDOWN]
		self.DISPLAYSURF = w.getDisplay()
		self.buttonNewGame = Button.Button("New Game", w.width / 2 - 200, w.height / 2, 400, 100,
										   "Assets/button/green_button00.png", "Assets/button/green_button01.png",
										   "Assets/Song/click1.ogg")
		self.buttonJoinGame = Button.Button("Join Game", w.width / 2 - 200, w.height / 2 + 150, 400, 100,
											"Assets/button/green_button00.png", "Assets/button/green_button01.png",
											"Assets/Song/click1.ogg")
		self.buttonExit = Button.Button("Exit", w.width / 2 - 200, w.height / 2 + 300, 400, 100,
										"Assets/button/green_button00.png", "Assets/button/green_button01.png",
										"Assets/Song/click1.ogg")

	def clear(self):
		self.DISPLAYSURF.fill((0, 0, 0))
		self.DISPLAYSURF.blit(self.background, (0, 0))

	def display(self):
		self.clear()
		self.buttonNewGame.display(self.DISPLAYSURF)
		self.buttonJoinGame.display(self.DISPLAYSURF)
		self.buttonExit.display(self.DISPLAYSURF)
		pygame.display.update()

	def getevent(self):
		events = []
		get_events = pygame.event.get()
		for event in get_events:
			if event.type in self.keys:
				events.append(event)
		for event in events:
			if event.type == QUIT or event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
		if pygame.mouse.get_pressed()[0]:
			self.buttonJoinGame.on_click(pygame.mouse.get_pos())
			self.buttonNewGame.on_click(pygame.mouse.get_pos())
			self.buttonExit.on_click(pygame.mouse.get_pos())
		self.buttonJoinGame.check_hover()
		self.buttonNewGame.check_hover()
		self.buttonExit.check_hover()

	def check_clicked(self, button):
		if (button.clicked == True):
			button.clicked == False
			return True
		return False

	def joinGame(self):
		self.clear()
		done = False
		inputs = []
		input_ip = Input.InputBox(self.w.width / 2 - 100, self.w.height / 2 - 120, 140, 32)
		input_port = Input.InputBox(self.w.width / 2 - 100, self.w.height / 2 + 30, 140, 32)
		inputs = [input_ip, input_port]
		clock = pygame.time.Clock()
		events = [KEYDOWN, MOUSEBUTTONDOWN]
		font = pygame.font.SysFont("monospace", 50)
		IP_TEXT = font.render("Enter server ip address", 2, (255, 0, 0))
		PORT_TEXT = font.render("Enter server port", 2, (255, 0, 0))
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				if event.type in events:
					if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
						for box in inputs:
							box.handle_event(event)
			for box in inputs:
				box.update()
			self.DISPLAYSURF.fill((30, 30, 30))
			self.DISPLAYSURF.blit(IP_TEXT, (self.w.width / 2 - 320, self.w.height / 2 - 200))
			self.DISPLAYSURF.blit(PORT_TEXT, (self.w.width / 2 - 320, self.w.height / 2 - 50))
			for box in inputs:
				box.draw(self.DISPLAYSURF)
			pygame.display.flip()
			clock.tick(60)


	def start(self):
		tmp = False
		while not tmp:
			self.getevent()
			self.display()
			if self.check_clicked(self.buttonNewGame):
				ls_output = subprocess.Popen(["python", "server.py"], stdin=subprocess.PIPE)
				time.sleep(1)
				break
			if self.check_clicked(self.buttonJoinGame):
				self.joinGame()
				break
			if self.check_clicked(self.buttonExit):
				pygame.quit()
				sys.exit()
