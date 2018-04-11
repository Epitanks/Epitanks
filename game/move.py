import pygame, sys
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(30, 50)
        self.FPS = 30
        self.fpsClock = pygame.time.Clock()
        self.width = 1280
        self.height = 512
        self.DISPLAYSURF = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.background = pygame.image.load('Assets/background_example.png')
        self.tanks = pygame.image.load('Assets/PNG/tank_dark.png')
        self.enemy = {}
        self.direction = None
        self.position = {'x': 200,
                         'y': 200}
        self.eposition = {};
        self.keys = [KEYUP, KEYDOWN]

    def move(self):
        if self.direction:
            if self.direction == K_UP:
                self.position['y'] -= 5

            elif self.direction == K_DOWN:
                self.position['y'] += 5

            if self.direction == K_LEFT:
                self.position['x'] -= 5

            elif self.direction == K_RIGHT:
                self.position['x'] += 5

    def getevent(self):
        self.DISPLAYSURF.blit(self.background, (0, 0))
        self.DISPLAYSURF.blit(self.tanks, (self.position['x'], self.position['y']))
        for enemy in self.enemy:
            self.DISPLAYSURF.blit(self.enemy[enemy], (int(self.eposition[enemy]['x']), int(self.eposition[enemy]['y'])))
         
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
        return str(self.position['x']) + "#" + str(self.position['y'])

    def setennemies(self, player, pos_x, pos_y):
        if player != -1:
            self.eposition[player]['x'] = int(pos_x)
            self.eposition[player]['y'] = int(pos_y)

    def setNewEnemy(self, key, asset, x, y):
        self.enemy[key] = pygame.image.load(asset);
        self.eposition[key] = {'x':x, 'y':y}

    def printEnemy(self):
        msg = ""
        for enemy in self.enemy:
            msg += enemy + " " + self.eposition[enemy]['x'] + " " + self.eposition[enemy]['x'] + "\n"
        return msg


