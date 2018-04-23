#!/usr/bin/env python
# -*-coding:utf-8 -*

import pygame
import math
from pygame.locals import *


def rot_center(image, rect, angle):
	"""rotate an image while keeping its center"""
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = rot_image.get_rect(center=rect.center)
	#print "rect=", rect.center, " rect2=", rot_rect.center
	return rot_image, rot_rect


def change_image(image, rect, cible, rect_cible):
	rect.center = rect_cible.center
	cible = image
	rect_cible = rect_cible.fit(rect)
	rect_cible.center = rect.center
	return cible, rect_cible


pygame.init()
pygame.key.set_repeat(30, 50)
# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

# Chargement et collage du fond
fond = pygame.image.load("Assets/background_example.png").convert()
fond = pygame.transform.scale(fond, (640, 480))
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
base = pygame.image.load("Assets/PNG/tank_dark.png").convert_alpha()
base2 = pygame.image.load("Assets/PNG/tank_dark.png").convert_alpha()
coord_base = base.get_rect()
coord_base2 = base2.get_rect()
#print coord_base.center, "||", coord_base2.center
coord_base2.center = coord_base.center
#print coord_base.center, "||", coord_base2.center

tourelle = pygame.image.load("Assets/PNG/tank_dark.png").convert_alpha()
coord_tourelle = tourelle.get_rect()

base_scr = base
tourelle_scr = tourelle
coord_base_scr = base_scr.get_rect()
coord_tourelle_scr = tourelle_scr.get_rect()

coord_tourelle_scr.center = coord_base_scr.center

fenetre.blit(base_scr, coord_base_scr)
fenetre.blit(tourelle_scr, coord_tourelle_scr)

# Rafraîchissement de l'écran
pygame.display.flip()

# BOUCLE INFINIE
continuer = 1
x = 0
y = 0

while continuer:
	pygame.time.Clock().tick(50)
	for event in pygame.event.get():  # Attente des événements
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			keys = pygame.key.get_pressed()
			if keys[K_LEFT]:
				base_scr, coord_base_scr = change_image(base2, coord_base2, base_scr, coord_base_scr)
				coord_tourelle_scr.center = coord_base_scr.center
				coord_base_scr = coord_base_scr.move(-10, 0)
				coord_tourelle_scr = coord_tourelle_scr.move(-10, 0)

			if keys[K_RIGHT]:
				base_scr, coord_base_scr = change_image(base2, coord_base2, base_scr, coord_base_scr)
				coord_tourelle_scr.center = coord_base_scr.center
				coord_base_scr = coord_base_scr.move(10, 0)
				coord_tourelle_scr = coord_tourelle_scr.move(10, 0)

			if keys[K_UP]:
				base_scr, coord_base_scr = change_image(base, coord_base, base_scr, coord_base_scr)
				coord_tourelle_scr.center = coord_base_scr.center
				coord_base_scr = coord_base_scr.move(0, -10)
				coord_tourelle_scr = coord_tourelle_scr.move(0, -10)

			if keys[K_DOWN]:
				base_scr, coord_base_scr = change_image(base, coord_base, base_scr, coord_base_scr)
				coord_tourelle_scr.center = coord_base_scr.center
				coord_base_scr = coord_base_scr.move(0, 10)
				coord_tourelle_scr = coord_tourelle_scr.move(0, 10)

			coord_base.center = coord_base_scr.center
			coord_tourelle.center = coord_tourelle_scr.center

	x, y = pygame.mouse.get_pos()

	dx = x - coord_tourelle_scr.center[0]
	dy = y - coord_tourelle_scr.center[1]

	rads = math.atan2(-dy, dx)
	degs = math.degrees(rads) - 90  # decalage de 90° de l'image rapport au 0°
	angle = degs

	print(x, y)
	print(angle)
	tourelle_scr, coord_tourelle_scr = rot_center(tourelle, coord_tourelle, angle)

	fenetre.blit(fond, (0, 0))
	fenetre.blit(base_scr, coord_base_scr)
	fenetre.blit(tourelle_scr, coord_tourelle_scr)
	pygame.display.flip()
