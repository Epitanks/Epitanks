import pygame, sys
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        self.width = 400
        self.height = 300
        self.DISPLAYSURF = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.background = pygame.image.load('Assets/background_example.png')
        self.sprite = pygame.image.load('Assets/PNG/tank_dark.png')
        self.sprite2 = pygame.image.load('Assets/PNG/tank_red.png')
        self.direction = None
        self.position = {'x': 200,
                         'y': 200}

    def move(self):
        if self.direction:
            if self.direction == K_UP:
                self.position['y'] -= 5
                self.sprite = pygame.image.load('Assets/PNG/tank_dark.png')

            elif self.direction == K_DOWN:
                self.position['y'] += 5
                self.sprite = pygame.image.load('Assets/PNG/tank_dark.png')

            if self.direction == K_LEFT:
                self.position['x'] -= 5
                self.sprite = pygame.image.load('Assets/PNG/tank_dark.png')

            elif self.direction == K_RIGHT:
                self.position['x'] += 5
                self.sprite = pygame.image.load('Assets/PNG/tank_dark.png')

    def getevent(self):
        self.DISPLAYSURF.blit(self.background, (0, 0))
        self.DISPLAYSURF.blit(self.sprite, (self.position['x'], self.position['y']))

        for event in pygame.event.get():
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
        self.fpsClock.tick(self.FPS)
        if len(pygame.event.get()) == 0:
            return None
        return "OK"

    def getpos(self):
        return str(self.position['x']) + ":" + str(self.position['y']) + "\n"

    def displayennemies(self, pos_x, pos_y):
        self.DISPLAYSURF.blit(self.sprite2, (int(pos_x), int(pos_y)))
        pygame.display.update()
        self.fpsClock.tick(self.FPS)


