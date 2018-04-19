import pygame, sys
from pygame.locals import *
import Players
import Bullets

class Game:
    def __init__(self, w, p):        
        self.background = pygame.image.load('Assets/background_example.png')
        self.players = p
        self.bullets = Bullets.Bullets()
        self.keys = [KEYUP, KEYDOWN]
        self.DISPLAYSURF = w.getDisplay()
        self.window = w

    def move(self, key):
        if key:
            if key[K_UP]:
                self.players.move(self.players.me, 0, -10)
            if key[K_DOWN]:
                self.players.move(self.players.me, 0, 10)
            if key[K_LEFT]:
                self.players.move(self.players.me, -10, 0)
            if key[K_RIGHT]:
                self.players.move(self.players.me, 10, 0)
            if key[K_SPACE]:
                self.bullets.add(1, self.players.getx(), self.players.gety(), 90)
                self.display();
                return self.bullets.toStringBullet()
        self.display();
        return self.getpos()

    def clear(self):
        self.DISPLAYSURF.fill((0,0,0))
        self.DISPLAYSURF.blit(self.background, (0, 0))

    def display(self):
        self.clear()

        self.bullets.move(self.window.width, self.window.height)

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
        return str(self.players.getx()) + "#" + str(self.players.gety())
