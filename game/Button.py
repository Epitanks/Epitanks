import pygame, sys
from pygame.locals import *

class Button():
    def __init__(self, text, x, y, w, h, asset, asset_hovered, song):
        asset = pygame.image.load(asset)
        self.asset = pygame.transform.scale(asset, (w, h))
        rect = self.asset.get_rect()
        rect = rect.move(int(x), int(y))
        self.rect = rect
        myfont = pygame.font.SysFont("monospace", 50)
        self.label = myfont.render(text, 1, (255,255,255))
        self.hovered = False
        asset_hovered = pygame.image.load(asset_hovered)
        self.asset_hovered = pygame.transform.scale(asset_hovered, (w, h))
        self.clicked = False
        self.song = son = pygame.mixer.Sound(song)

    def display(self, display):
        to_display = self.asset
        if (self.hovered):
            to_display = self.asset_hovered
        display.blit(to_display, self.rect)
        text_rect = self.label.get_rect()
        text_rect.center = self.rect.center
        display.blit(self.label, text_rect)

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
        else:
            self.hovered = False

    def on_click(self, pos):
        if self.rect.collidepoint(pos):
            self.clicked = True
            self.song.play()
