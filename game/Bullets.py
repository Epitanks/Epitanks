import pygame, sys, math
from pygame.locals import *

class Bullets:
    def __init__(self, w):
        self.bullets = []
        self.rect = []
        self.w = w.getDisplay()
        self.toSend = ""
        self.width = w.width
        self.height = w.height
    
    def rotate(self, i):
        img = self.bullets[i]['img']
        rect = self.rect[i]
        rot_image = pygame.transform.rotate(img, float(self.bullets[i]['dir']))
        rot_rect = rot_image.get_rect(center=rect.center)
        self.rect[i] = rot_rect
        return rot_image, rot_rect

    def clear(self, background):
        for rect in self.rect:
            self.w.blit(background, rect, rect)

    def display(self):
        i = 0
        for bullet, rect in zip(self.bullets, self.rect):
            img, r = self.rotate(i)
            self.w.blit(img, r)
   #         pygame.draw.rect(self.w, (255,0,0), r, 2)
            i += 1
    
    def add(self, t, dire, prect):
        try:
            bullet = {'img': pygame.image.load('Assets/PNG/bulletRed3_outline.png'), "path": 'Assets/PNG/bulletRed3_outline.png', 'dir': float(dire), 'type': t}
            rect = bullet['img'].get_rect()
            b = (math.cos(math.radians(dire)) * 120) + prect.y + (prect.h / 2) - (rect.h / 2)
            a = (math.sin(math.radians(dire)) * 120) + prect.x + (prect.w / 2) - (rect.w / 2)
            rect = rect.move(a, b)
            self.rect.append(rect)
            self.bullets.append(bullet)
            self.toSend += "&" + bullet['path'] + "&" + str(a) + "&" + str(b) + "&" + str(bullet['dir']) + "&" + str(bullet['type']) + "&\n"
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

    def addEnemy(self, path, x, y, d, t):
        bullet = {'img': pygame.image.load(path), "path": path, 'dir': float(d), 'type': int(t)}
        rect = bullet['img'].get_rect()
        rect = rect.move(float(x), float(y))
        self.rect.append(rect)
        self.bullets.append(bullet)

    def move(self):
        i = 0
        for bullet, rect in zip(self.bullets, self.rect):
            b = math.cos(math.radians(bullet['dir'])) * 5
            a = math.sin(math.radians(bullet['dir'])) * 5
            self.rect[i] = rect.move(a, b)
            if self.rect[i].x < 0 or self.rect[i].y < 0 or self.rect[i].x > self.width or self.rect[i].y > self.height:
                self.bullets.remove(bullet)
                self.rect.remove(self.rect[i])
            else:
                i += 1
            
    def toStringBullet(self):
        msg = self.toSend
        self.toSend = ""
        return msg

