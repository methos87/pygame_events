#!/usr/bin/env python

import pygame

from pygame.locals import *
from sys import exit

background_image_location = ""
mouse_image_location = ""

pygame.init()
screen_size = (800, 600)
full_screen = 0  # FULLSCREEN / 0

screen = pygame.display.set_mode(screen_size, full_screen, 32)
pygame.display.set_caption("Hello World")

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []
text_com = " Command:"

while True:

    event = pygame.event.wait()
    event_text.append(str(event))
    # event_text = event_text[-screen_size[1]/font_height:]

    if event.type == QUIT:
        exit()

    screen.fill((255, 255, 255))
    y = screen_size[1] - (font_height * 2)
    screen.blit(font.render(text_com, True, (0, 0, 0)), (0, y))

    z = screen_size[1] - (font_height * 3)

    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, z))
        z -= font_height

    pygame.display.update()
