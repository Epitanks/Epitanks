import pygame, sys
from pygame.locals import *
import Players
import Bullets

class Game:
    def __init__(self, w, p):        
        self.background = pygame.image.load('Assets/background_example.png')
        self.players = p
        self.bullets = Bullets.Bullets()
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

            if self.players.direction == K_SPACE:
                self.bullets.add(1, self.players.getx(), self.players.gety(), 120)
                return self.bullets.toStringBullet()
        return self.getpos()

    def clear(self):
        self.DISPLAYSURF.fill((0,0,0))
        self.DISPLAYSURF.blit(self.background, (0, 0))

    def display(self):
        self.clear()
        self.bullets.display(self.DISPLAYSURF)
        self.players.display(self.DISPLAYSURF)
        pygame.display.update()

    def getevent(self):
        events = []
        get_events = pygame.event.get()
        for event in get_events:
            if event.type in self.keys:
                events.append(event)

        tmp = None
        for event in events:
            if event.type == QUIT or event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                self.players.direction = event.key
            if event.type == KEYUP:
                if event.key == self.players.direction:
                    self.players.direction = None
            tmp = self.move()

        self.bullets.move()
        if len(events) == 0:
            return None
        return tmp

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

