import pygame, sys, math
from pygame.locals import *

class Bullets:
    def __init__(self):
        self.bullets = []
        self.rect = []
        self.toSend = ""
    
    def add(self, t, x, y, d):
        try:
            bullet = {'img': pygame.image.load('Assets/PNG/bulletRed3_outline.png'), "path": 'Assets/PNG/bulletRed3_outline.png', 'dir': int(d)}
            rect = bullet['img'].get_rect()
            rect = rect.move(int(x) - 20, int(y))
            self.rect.append(rect)
            self.bullets.append(bullet)
            self.toSend += "&" + bullet['path'] + "&" + str(rect.x) + "&" + str(rect.y) + "&" + str(bullet['dir']) + "&\n"
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    def addEnemy(self, t, x, y, d):
        bullet = {'img': pygame.image.load(t), "path": t, 'dir': int(d)}
        rect = bullet['img'].get_rect()
        rect = rect.move(int(x) - 20, int(y))
        self.rect.append(rect)
        self.bullets.append(bullet)

    def display(self, display):
        for bullet, rect in zip(self.bullets, self.rect):
            display.blit(bullet['img'], (rect.x, rect.y))

    def move(self, x, y, players):
        i = 0
        for bullet, rect in zip(self.bullets, self.rect):
            self.rect[i] = rect.move(5 * math.cos(bullet['dir']), 5 * math.sin(bullet['dir']))
            if self.rect[i].x < 0 or self.rect[i].y < 0 or self.rect[i].x > x or self.rect[i].y > y:
                self.bullets.remove(bullet)
                self.rect.remove(self.rect[i])
            else:
                i += 1
            
    def toStringBullet(self):
        msg = self.toSend
        self.toSend = ""
        return msg

