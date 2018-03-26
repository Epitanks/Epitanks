import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

width=400
height=300
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Animation')
background=pygame.image.load('Assets/background_example.png')


UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

sprite=pygame.image.load('Assets/PNG/tank_blue.png')
spritex=200
spritey=130
direction=None

def move(direction, sprite, spritex, spritey):
    if direction:
        if direction == K_UP:
            spritey-=5
            sprite=pygame.image.load('Assets/PNG/tank_blue.png')
        elif direction == K_DOWN:
            spritey+=5
            sprite=pygame.image.load('Assets/PNG/tank_dark.png')
        if direction == K_LEFT:
            spritex-=5
            sprite=pygame.image.load('Assets/PNG/tank_green.png')
        elif direction == K_RIGHT:
            spritex+=5
            sprite=pygame.image.load('Assets/PNG/tank_red.png')
    return sprite, spritex, spritey

while True:
    DISPLAYSURF.blit(background,(0,0))

    DISPLAYSURF.blit(sprite,(spritex,spritey))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            direction = event.key
        if event.type == KEYUP:
            if (event.key == direction):
                direction = None
    sprite, spritex, spritey = move(direction, sprite, spritex, spritey)

    pygame.display.update()
    fpsClock.tick(FPS)