import pygame, sys
from pygame.locals import *

class Players:
    def __init__(self):        
        self.tanks = []
        self.me = ""
        self.rect = {}

    def setMe(self, value):
        self.me = value

    def display(self, display):
        #for enemy in self.tanks:
        #    display.blit(self.tanks[enemy], (self.rect[enemy].x, self.rect[enemy].y))
        for tank in self.tanks:
            display.blit(tank['img'], (tank['rect'].x, tank['rect'].y))
       
    def getx(self):
        return self.tanks[self.getTank(self.me)]['rect'].x

    def gety(self):
        return self.tanks[self.getTank(self.me)]['rect'].y

    def setNewEnemy(self, key, asset, x, y):
        tank = {'key': key, 'img': pygame.image.load(asset), 'rect': ""}
        tank['rect'] = tank['img'].get_rect()
        tank['rect'] = tank['rect'].move(int(x), int(y))
        self.tanks.append(tank)

#        self.tanks[key] = pygame.image.load(asset)
 #       self.rect[key] = self.tanks[key].get_rect()
 #       self.rect[key] = self.rect[key].move(int(x), int(y))

    def move(self, key, x, y):
        if key != -1:
            i = self.getTank(key)
            self.tanks[i]['rect'] = self.tanks[i]['rect'].move(int(x), int(y))
#            self.rect[key] = self.rect[key].move(int(x), int(y))
         #   if (self.rect[key].collidelist

    def moveEnemy(self, key, x, y):
        i = self.getTank(key)
        x = int(x) - self.tanks[i]['rect'].x
        y = int(y) - self.tanks[i]['rect'].y
        if key != -1:
            self.tanks[i]['rect'] = self.tanks[i]['rect'].move(int(x), int(y))

    def getTank(self, key):
        i = 0
        for tank in self.tanks:
            if tank['key'] == key:
                return i
            i += 1
        return None