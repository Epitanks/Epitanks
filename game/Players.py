import pygame, sys
from pygame.locals import *

class Players:
    def __init__(self):        
        self.tanks = []
        self.rect = []
        self.me = ""

    def setMe(self, value):
        self.me = value

    def display(self, display):
        for tank, rect in zip(self.tanks, self.rect):
            display.blit(tank['img'], (rect.x, rect.y))
       
    def getx(self):
        return self.rect[self.getTank(self.me)].x

    def gety(self):
        return self.rect[self.getTank(self.me)].y

    def setNewEnemy(self, key, asset, x, y):
        tank = {'key': key, 'img': pygame.image.load(asset)}
        rect = tank['img'].get_rect()
        rect = rect.move(int(x), int(y))
        self.tanks.append(tank)
        self.rect.append(rect)

    def move(self, key, x, y):
        if key != -1:
            i = self.getTank(key)
            tmp = self.rect[i].move(int(x), int(y))
            liste = list(self.rect)
            liste.remove(self.rect[i])
            if tmp.collidelist(liste) == -1:
                self.rect[i] = self.rect[i].move(int(x), int(y))

    def moveEnemy(self, key, x, y):
        i = self.getTank(key)
        x = int(x) - self.rect[i].x
        y = int(y) - self.rect[i].y
        if key != -1:
            self.rect[i] = self.rect[i].move(int(x), int(y))

    def getTank(self, key):
        i = 0
        for tank in self.tanks:
            if tank['key'] == key:
                return i
            i += 1
        return None