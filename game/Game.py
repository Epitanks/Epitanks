import pygame, sys, math
from pygame.locals import *
import Players
import Bullets

class Game:
    def __init__(self, w, p):        
        self.background = pygame.image.load('Assets/epitank.png')
        self.players = p
        self.bullets = Bullets.Bullets()
        self.keys = [KEYUP, KEYDOWN]
        self.DISPLAYSURF = w.getDisplay()
        self.window = w
        self.DISPLAYSURF.blit(self.background, (0, 0))
        pygame.display.update()

    def move(self, key):
        if self.players.life == True:
            if key:
                if key[K_UP]:
                    self.players.move(self.players.me, 7)
                if key[K_DOWN]:
                    self.players.move(self.players.me, -7)
                if key[K_LEFT]:
                    self.players.setDir(10)
                    self.players.move(self.players.me, 7)
                if key[K_RIGHT]:
                    self.players.setDir(-10)
                    self.players.move(self.players.me, 7)
                if key[K_SPACE]:
                    i = self.players.getTank(self.players.me)
                    tank = self.players.tanks[i]
                    rect = self.players.rect[i]
                    self.bullets.add(1, tank['dir'], rect)
                    self.display()
                    return self.bullets.toStringBullet()
            self.display()
            return self.getpos()
        return "error"

    def colision(self):
        i = 0
        for player, rect in zip(self.players.tanks, self.players.rect):
            toDelete = rect.collidelist(self.bullets.rect)
     #       if toDelete != -1:
      #          self.bullets.bullets.remove(self.bullets.bullets[toDelete])
       #         self.bullets.rect.remove(self.bullets.rect[toDelete])
        #        self.players.dead(player, rect)

    def clear(self):
        self.DISPLAYSURF.fill((0,0,0))
        self.DISPLAYSURF.blit(self.background, (0, 0))

    def display(self):
        self.clear()
        self.bullets.move(self.window.width, self.window.height, self.players)
        self.colision()
        self.bullets.display(self.DISPLAYSURF)
        self.players.display(self.DISPLAYSURF)
        pygame.display.update()

    def getevent(self):
        events = []
        get_events = pygame.event.get()
        for event in get_events:
            if event.type in self.keys:
                events.append(event)

        key = None
        tmp = None
        for event in events:
            if event.type == QUIT or event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                key = pygame.key.get_pressed()
            if event.type == KEYUP:
                if event.key == key:
                    key = None
            tmp = self.move(key)

        if len(events) == 0:
            return None
        return tmp

    def getpos(self):
        if self.players.getx() == -1 or self.players.gety() == -1:
            return "error"
        return str(self.players.getx()) + "#" + str(self.players.gety()) + "#" + str(self.players.getDir())
