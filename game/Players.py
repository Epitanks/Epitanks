import pygame, sys
from pygame.locals import *

class Players:
    def __init__(self):        
        self.tanks = {}
        self.me = ""
        self.direction = None
        self.eposition = {}

    def setMe(self, value):
        self.me = value

    def display(self, display):
        for enemy in self.tanks:
            display.blit(self.tanks[enemy], (int(self.eposition[enemy]['x']), int(self.eposition[enemy]['y'])))
       
    def getx(self):
        return self.eposition[self.me]['x']

    def gety(self):
        return self.eposition[self.me]['y']