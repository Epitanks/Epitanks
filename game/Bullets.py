import pygame, sys, math
from pygame.locals import *

class Bullets:
    def __init__(self):
        self.bullets = []
        self.toSend = ""
    
    def add(self, t, x, y, d):
        bullet = {'img': pygame.image.load('Assets/PNG/bulletRed3_outline.png'), "path": 'Assets/PNG/bulletRed3_outline.png', 'x': int(x), 'y': int(y), 'dir': int(d)}
        self.bullets.append(bullet)
        self.toSend += "&" + bullet['path'] + "&" + str(bullet['x']) + "&" + str(bullet['y']) + "&" + str(bullet['dir']) + "&\n"

    def addEnemy(self, t, x, y, d):
        bullet = {'img': pygame.image.load(t), "path": t, 'x': int(x), 'y': int(y), 'dir': int(d)}
        self.bullets.append(bullet)

    def display(self, display):
        for bullet in self.bullets:
            display.blit(bullet['img'], (bullet['x'], bullet['y']))

    def move(self):
        for bullet in self.bullets:
            bullet['x'] += 5 * math.cos(bullet['dir'])
            bullet['y'] += 5 * math.sin(bullet['dir'])


    def toStringBullet(self):
        msg = self.toSend
        self.toSend = ""
        return msg

