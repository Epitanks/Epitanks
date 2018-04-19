import pygame, sys, math
from pygame.locals import *

class Bullets:
    def __init__(self):
        self.bullets = []
        self.toSend = ""
    
    def add(self, t, x, y, d):
        bullet = {'img': pygame.image.load('Assets/PNG/bulletRed3_outline.png'), "path": 'Assets/PNG/bulletRed3_outline.png', 'dir': int(d), 'rect': ""}
        bullet['rect'] = bullet['img'].get_rect()
        bullet['rect'] = bullet['rect'].move(int(x), int(y))
        self.bullets.append(bullet)
        self.toSend += "&" + bullet['path'] + "&" + str(bullet["rect"].x) + "&" + str(bullet["rect"].y) + "&" + str(bullet['dir']) + "&\n"

    def addEnemy(self, t, x, y, d):
        bullet = {'img': pygame.image.load(t), "path": t, 'dir': int(d), 'rect': ""}
        bullet['rect'] = bullet['img'].get_rect()
        bullet['rect'] = bullet['rect'].move(int(x), int(y))
        self.bullets.append(bullet)

    def display(self, display):
        for bullet in self.bullets:
            display.blit(bullet['img'], (bullet['rect'].x, bullet['rect'].y))

    def move(self, x, y):
        for bullet in self.bullets:
            bullet['rect'] = bullet['rect'].move(5 * math.cos(bullet['dir']), 5 * math.sin(bullet['dir']))
      #      if bullet['x'] < 0 or bullet['y'] < 0 or bullet['x'] > x or bullet['y'] > y:
       #         self.bullets.remove(bullet)

    def toStringBullet(self):
        msg = self.toSend
        self.toSend = ""
        return msg

