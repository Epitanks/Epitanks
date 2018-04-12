import pygame, sys
from pygame.locals import *
import Players

class Game:
    def __init__(self, w, p):        
        self.background = pygame.image.load('Assets/background_example.png')
        self.players = p
        self.keys = [KEYUP, KEYDOWN]
        self.DISPLAYSURF = w.getDisplay()

    def move(self):
        if self.players.direction:
            if self.players.direction == K_UP:
                self.players.eposition[self.players.me]['y'] -= 10

            elif self.players.direction == K_DOWN:
                self.players.eposition[self.players.me]['y'] += 10

            if self.players.direction == K_LEFT:
                self.players.eposition[self.players.me]['x'] -= 10

            elif self.players.direction == K_RIGHT:
                self.players.eposition[self.players.me]['x'] += 10

    def getevent(self):
        self.DISPLAYSURF.blit(self.background, (0, 0))
        for enemy in self.players.tanks:
            self.DISPLAYSURF.blit(self.players.tanks[enemy], (int(self.players.eposition[enemy]['x']), int(self.players.eposition[enemy]['y'])))
        events = []
        get_events = pygame.event.get()

        for event in get_events:
            if event.type in self.keys:
                events.append(event)

        for event in events:
            if event.type == QUIT or event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                self.players.direction = event.key
            if event.type == KEYUP:
                if event.key == self.players.direction:
                    self.players.direction = None
            self.move()

        pygame.display.update()
        if len(events) == 0:
            return None
        return "OK"

    def getpos(self):
        return str(self.players.eposition[self.players.me]['x']) + "#" + str(self.players.eposition[self.players.me]['y'])

    def setennemies(self, player, pos_x, pos_y):
        if player != -1:
            self.players.eposition[player]['x'] = int(pos_x)
            self.players.eposition[player]['y'] = int(pos_y)

    def setNewEnemy(self, key, asset, x, y):
        self.players.tanks[key] = pygame.image.load(asset);
        self.players.eposition[key] = {'x':int(x), 'y':int(y)}

    def toStringTanks(self):
        msg = ""
        for enemy in self.players.tanks:
            msg += enemy + " " + str(self.players.eposition[enemy]['x']) + " " + str(self.players.eposition[enemy]['x']) + "\n"
        return msg

