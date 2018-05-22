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
        self.background = pygame.image.load('Assets/Accueil.png')
        self.keys = [KEYUP, KEYDOWN]
        self.DISPLAYSURF = w.getDisplay()
        self.buttonNewGame = Button.Button("New Game", w.width / 2 - 200, w.height / 2, 400, 100, "Assets/button/green_button00.png", "Assets/button/green_button01.png", "Assets/Song/click1.ogg")
        self.buttonJoinGame = Button.Button("Join Game", w.width / 2 - 200, w.height / 2 + 150, 400, 100, "Assets/button/green_button00.png", "Assets/button/green_button01.png", "Assets/Song/click1.ogg")
        self.buttonExit = Button.Button("Exit", w.width / 2 - 200, w.height / 2 + 300, 400, 100, "Assets/button/green_button00.png", "Assets/button/green_button01.png", "Assets/Song/click1.ogg")

    def clear(self):
        self.DISPLAYSURF.fill((0,0,0))
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
        if (pygame.mouse.get_pressed()[0] == True):
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

    def start(self):
        tmp = False
        while (tmp == False):
            self.getevent()
            self.display()
            if (self.check_clicked(self.buttonNewGame)):
                ls_output=subprocess.Popen(["python", "server.py"], stdout=subprocess.PIPE)
                time.sleep(1)
                break
            if (self.check_clicked(self.buttonJoinGame)):
               # self.joinGame()
                break
            if (self.check_clicked(self.buttonExit) == True):
                pygame.quit()
                sys.exit()

    def joinGame(self):
        self.clear()
        i = Input.Input(self.DISPLAYSURF)
        i.ask("test")


        