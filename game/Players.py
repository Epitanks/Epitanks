import pygame, sys, math
from pygame.locals import *

class Players:
    def __init__(self):        
        self.tanks = []
        self.rect = []
        self.me = ""
        self.life = True

    def setMe(self, value):
        self.me = value

    def rotate(self, key):
        i = self.getTank(key)
        img = self.tanks[i]['img']
        rect = self.rect[i]
        rot_image = pygame.transform.rotate(img, self.tanks[i]['dir'])
        rot_rect = rot_image.get_rect(center=rect.center)
        self.rect[i] = rot_rect
        return rot_image, rot_rect

    def display(self, display):
        for tank in self.tanks:
            img, r = self.rotate(tank['key'])
            display.blit(img, r)
       
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

    def getDir(self):
        return self.tanks[self.getTank(self.me)]['dir']

    def setDir(self, angle):
        self.tanks[self.getTank(self.me)]['dir'] += angle

    def setNewEnemy(self, key, asset, x, y, angle):
        tank = {'key': key, 'img': pygame.image.load(asset), 'dir': angle}
        rect = tank['img'].get_rect()
        rect = rect.move(int(x), int(y))
        self.tanks.append(tank)
        self.rect.append(rect)

    def move(self, key, x, y):
        if key != -1:
            i = self.getTank(key)
            
            tmp = self.rect[i].move(x, y)
            liste = list(self.rect)
            liste.remove(self.rect[i])
            if tmp.collidelist(liste) == -1:
                self.rect[i] = self.rect[i].move(x, y)
            else:
                print('colision')

    def moveEnemy(self, key, x, y, dir):
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