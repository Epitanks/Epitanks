import pygame, sys, math
from pygame.locals import *

class Bullets:
    def __init__(self):
        self.bullets = []
        self.rect = []
        self.toSend = ""
    
    def rotate(self, i):
        img = self.bullets[i]['img']
        rect = self.rect[i]
        rot_image = pygame.transform.rotate(img, float(self.bullets[i]['dir']))
        rot_rect = rot_image.get_rect(center=rect.center)
        self.rect[i] = rot_rect
        return rot_image, rot_rect

    def display(self, display):
        i = 0
        for bullet, rect in zip(self.bullets, self.rect):
            img, r = self.rotate(i)
            display.blit(img, r)
            i += 1
    
    def add(self, t, dire, prect):
        try:
            bullet = {'img': pygame.image.load('Assets/PNG/bulletRed3_outline.png'), "path": 'Assets/PNG/bulletRed3_outline.png', 'dir': float(dire), 'x': 0, 'y': 0}
            rect = bullet['img'].get_rect()
            print(dire, math.cos(math.radians(dire)), math.sin(math.radians(dire)))
            b = (math.cos(math.radians(dire))) + prect.y + (prect.h / 2) - (rect.h / 2)
            a = (math.sin(math.radians(dire))) + prect.x + (prect.w / 2) - (rect.w / 2)
            bullet['x'] = float(a)
            bullet['y'] = float(b)
            rect = rect.move(a, b)
            self.rect.append(rect)
            self.bullets.append(bullet)
            self.toSend += "&" + bullet['path'] + "&" + str(a) + "&" + str(b) + "&" + str(bullet['dir']) + "&\n"
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

    def addEnemy(self, t, x, y, d):
        bullet = {'img': pygame.image.load(t), "path": t, 'dir': float(d), 'x': float(x), 'y': float(y)}
        rect = bullet['img'].get_rect()
        rect = rect.move(float(x), float(y))
        self.rect.append(rect)
        self.bullets.append(bullet)

    def move(self, x, y, players):
        i = 0
        for bullet, rect in zip(self.bullets, self.rect):
            b = math.cos(math.radians(bullet['dir'])) * 5
            a = math.sin(math.radians(bullet['dir'])) * 5
            self.rect[i] = rect.move(a, b)
            if self.rect[i].x < 0 or self.rect[i].y < 0 or self.rect[i].x > x or self.rect[i].y > y:
                self.bullets.remove(bullet)
                self.rect.remove(self.rect[i])
            else:
                i += 1
            
    def toStringBullet(self):
        msg = self.toSend
        self.toSend = ""
        return msg

