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
        self.sprite = pygame.image.load('Assets/PNG/tank_dark.png')
        self.sprite2 = pygame.image.load('Assets/PNG/tank_red.png')
        self.direction = None
        self.position = {'x': 200,
                         'y': 200}
        self.eposition = {'x': 0,
                         'y': 0}
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
        self.DISPLAYSURF.blit(self.sprite, (self.position['x'], self.position['y']))
        self.DISPLAYSURF.blit(self.sprite2, (self.eposition['x'], self.eposition['y']))
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
        return "#" + str(self.position['x']) + ":" + str(self.position['y'])

    def setennemies(self, pos_x, pos_y):
        self.eposition['x'] = int(pos_x)
        self.eposition['y'] = int(pos_y)


