#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit
from pygame import rect


pygame.init()

screen = pygame.display.set_mode((640, 480))
blank_surface = pygame.display.set_mode((512, 512), flags=HWSURFACE, depth=32)
background_image_filename = "img/clay-banks.jpg"
mouse_image_filename = "img/red.jpg"
my_rect = (100, 100, 200, 150)

mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
background = pygame.image.load(background_image_filename).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        blank_surface.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(my_rect, (200, 200))

        x, y = pygame.mouse.get_pos()
        x-= mouse_cursor.get_width() / 2
        y-= mouse_cursor.get_height() / 2
        screen.blit(mouse_cursor, (x, y))

        pygame.display.update()
