import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

width=400
height=300
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)

background=pygame.image.load('Assets/background_example.png')

sprite=pygame.image.load('Assets/PNG/tank_dark.png')

direction=None
position = {'x': 200,
			'y': 200}

def move(direction, sprite, position):
    if direction:
        if direction == K_UP:
            position['y'] -= 5
            sprite=pygame.image.load('Assets/PNG/tank_dark.png')
        elif direction == K_DOWN:
            position['y'] += 5
            sprite=pygame.image.load('Assets/PNG/tank_dark.png')
        if direction == K_LEFT:
            position['x'] -= 5
            sprite=pygame.image.load('Assets/PNG/tank_dark.png')
        elif direction == K_RIGHT:
            position['x'] += 5
            sprite=pygame.image.load('Assets/PNG/tank_dark.png')
    return sprite, position

while True:
    DISPLAYSURF.blit(background,(0,0))

    DISPLAYSURF.blit(sprite,(position['x'],position['y']))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            direction = event.key
        if event.type == KEYUP:
            if (event.key == direction):
                direction = None
    sprite, position = move(direction, sprite, position)

    pygame.display.update()
    fpsClock.tick(FPS)