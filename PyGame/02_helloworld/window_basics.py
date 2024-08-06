#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

background_image_filename = "img/clay-banks.jpg"

pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
background = pygame.image.load(background_image_filename).convert()

message = "       This is a demonstration of the scroll message script.    "

font = pygame.font.SysFont("arial", 40)
text_surface = font.render(message, True, (0, 0, 255))

x = 0
y = screen_size[1] - 60

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            exit()

        if event.type == VIDEORESIZE:
            screen_size = event.size
            screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
            pygame.display.set_caption("Window resized to " + str(event.size))

    screen_width, screen_height = screen_size
    for wy in range(0, screen_height, background.get_height()):
        for wx in range(0, screen_width, background.get_width()):
            screen.blit(background, (wx, wy))

    x -= 0.3
    if x < -text_surface.get_width():
        x = 0

    screen.blit(text_surface, (x, y))
    screen.blit(text_surface, (x + text_surface.get_width(), y))

    pygame.display.update()
