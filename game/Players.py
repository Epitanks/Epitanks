import pygame, sys
from pygame.locals import *

class Players:
    def __init__(self):        
        self.tanks = []
        self.rect = []
        self.me = ""
        self.life = True

    def setMe(self, value):
        self.me = value

    def display(self, display):
        for tank, rect in zip(self.tanks, self.rect):
            display.blit(tank['img'], (rect.x, rect.y))
       
    def getx(self):
        if self.getTank(self.me) == None:
            return -1
        x = self.rect[self.getTank(self.me)].x
        return x

    def gety(self):
        if self.getTank(self.me) == None:
            return -1
        y = self.rect[self.getTank(self.me)].y
        return y

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

    def dead(self, player, rect):
        self.tanks.remove(player)
        self.rect.remove(rect)
        self.life = False

    def disconnect(self, key):
        print(key)
        i = self.getTank(key)
        self.tanks.remove(self.tanks[i])
        self.rect.remove(self.rect[i])
        self.life = False


    def getTank(self, key):
        i = 0
        for tank in self.tanks:
            if tank['key'] == key:
                return i
            i += 1
        return None