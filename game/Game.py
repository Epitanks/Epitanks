import pygame, sys, math
from pygame.locals import *
import Players
import Bullets
import Info

class Game:
    def __init__(self, w, p):
        self.background = pygame.image.load('Assets/epitank.png')
        self.players = p
        self.bullets = Bullets.Bullets(w)
        self.keys = [KEYUP, KEYDOWN]
        self.DISPLAYSURF = w.getDisplay()
        self.window = w
        self.font = pygame.font.SysFont("monospace", 50)
        self.wait = self.font.render("Waiting for players...", 2, (255, 0, 0))
        self.IP_server = self.font.render("IP_SERVER : " + str(Info.getinfoserver()['IP_ADDRESS']), 2, (255, 0, 0))
        self.PORT_server = self.font.render("PORT_SERVER : " + str(Info.getinfoserver()['PORT']), 2, (255, 0, 0))
        self.tabpressed = False
        self.DISPLAYSURF.blit(self.background, (0, 0))
        pygame.display.update()

    def clearbackground(self):
        self.DISPLAYSURF.blit(self.background, (0, 0))
        pygame.display.update()

    def printwaiting(self):
        self.DISPLAYSURF.blit(self.wait, (self.window.width / 2 - 300, 30))
        pygame.display.update()

    def geteventtab(self):
        get_events = pygame.event.get()
        for event in get_events:
                keys = pygame.key.get_pressed()
                if event.type == KEYUP and event.key == K_TAB and self.tabpressed is True:
                    self.DISPLAYSURF.blit(self.background, (0, 0))
                    self.DISPLAYSURF.blit(self.background, (0, 0))
                    pygame.display.update()
                    self.tabpressed = False
                if event.type == KEYDOWN and keys[K_TAB] and self.tabpressed is False:
                    self.DISPLAYSURF.blit(self.IP_server, (10, self.window.height / 2))
                    self.DISPLAYSURF.blit(self.PORT_server, (10, self.window.height / 2 + 50))
                    pygame.display.update()
                    self.tabpressed = True


    def move(self, key):
        if self.players.life == True:
            if key:
                self.players.clear(self.background)
                if key[K_UP]:
                    self.players.move(self.players.me, 7)
                if key[K_DOWN]:
                    self.players.move(self.players.me, -7)
                if key[K_LEFT]:
                    self.players.setDir(10)
                if key[K_RIGHT]:
                    self.players.setDir(-10)
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

    def moveEnemy(self, key, x, y, dire):
        self.players.clear(self.background)
        self.players.moveEnemy(key, x, y, dire)
        self.display()

    def colision(self):
        i = 0
        for player, rect in zip(self.players.tanks, self.players.rect):
            toDelete = rect.collidelist(self.bullets.rect)
            if toDelete != -1:
                self.bullets.bullets.remove(self.bullets.bullets[toDelete])
                self.bullets.rect.remove(self.bullets.rect[toDelete])
                self.players.dead(player, rect)

    def display(self):
   #     self.colision()
        self.bullets.clear(self.background)
        self.bullets.move()
        self.bullets.display()
        self.players.display()
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
