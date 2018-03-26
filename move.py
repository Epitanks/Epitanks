import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

fond = pygame.image.load("Assets/background_example.png").convert()
fenetre.blit(fond, (0,0))

perso = pygame.image.load("Assets/PNG/tank_dark.png").convert_alpha()
perso_x = 0
perso_y = 0
fenetre.blit(perso, (perso_x, perso_y))

pygame.display.flip()

continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN and event.key == K_UP:
				perso_x += 10
	
	fenetre.blit(fond, (0,0))	
	fenetre.blit(perso, (perso_x, perso_y))
	pygame.display.flip()
