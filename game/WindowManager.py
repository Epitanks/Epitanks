import pygame, sys
from pygame.locals import *

class WindowManager:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(30, 50)
        self.width = 1920
        self.height = 1080
        self.DISPLAYSURF = pygame.display.set_mode((self.width, self.height), 0, 32)

    def getDisplay(self):
        return self.DISPLAYSURF
