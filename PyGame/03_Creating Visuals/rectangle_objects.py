#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit
from random import *


pygame.init()
blank_surface = pygame.display.set_mode((768, 512), flags=HWSURFACE, depth=32)

blank_surface.lock()

points = []

for count in range(10):
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    random_pos = (randint(0, 639), randint(0, 479))
    random_size = (639-randint(random_pos[0], 639), 479-randint(random_pos[1], 479))
    pygame.draw.rect(blank_surface, random_color, Rect(random_pos, random_size))

blank_surface.unlock()

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
