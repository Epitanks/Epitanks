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