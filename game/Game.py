import pygame, sys
from pygame.locals import *

class Game:
    def __init__(self, w):        
        self.background = pygame.image.load('Assets/background_example.png')
        self.tanks = {}
        self.me = ""
        self.direction = None
        self.eposition = {}
        self.keys = [KEYUP, KEYDOWN]
        self.DISPLAYSURF = w.getDisplay()

    def move(self):
        if self.direction:
            if self.direction == K_UP:
                self.eposition[self.me]['y'] -= 5

            elif self.direction == K_DOWN:
                self.eposition[self.me]['y'] += 5

            if self.direction == K_LEFT:
                self.eposition[self.me]['x'] -= 5

            elif self.direction == K_RIGHT:
                self.eposition[self.me]['x'] += 5

    def getevent(self):
        self.DISPLAYSURF.blit(self.background, (0, 0))
        for enemy in self.tanks:
            self.DISPLAYSURF.blit(self.tanks[enemy], (int(self.eposition[enemy]['x']), int(self.eposition[enemy]['y'])))
        events = []
        get_events = pygame.event.get()

        for event in get_events:
            if event.type in self.keys:
                events.append(event)

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                self.direction = event.key
            if event.type == KEYUP:
                if event.key == self.direction:
                    self.direction = None
            self.move()

        pygame.display.update()
        if len(events) == 0:
            return None
        return "OK"

    def getpos(self):
        return str(self.eposition[self.me]['x']) + "#" + str(self.eposition[self.me]['y'])

    def setennemies(self, player, pos_x, pos_y):
        if player != -1:
            self.eposition[player]['x'] = int(pos_x)
            self.eposition[player]['y'] = int(pos_y)

    def setNewEnemy(self, key, asset, x, y):
        self.tanks[key] = pygame.image.load(asset);
        self.eposition[key] = {'x':int(x), 'y':int(y)}

    def printEnemy(self):
        msg = ""
        for enemy in self.tanks:
            msg += enemy + " " + str(self.eposition[enemy]['x']) + " " + str(self.eposition[enemy]['x']) + "\n"
        return msg

    def setMe(self, value):
        self.me = value