#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit
from random import *


pygame.init()
screen = pygame.display.set_mode((768, 512), flags=HWSURFACE, depth=32)

points = []


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
    screen.fill((255, 255, 255))

    for _ in range(25):
        random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        random_pos = (randint(0, 639), randint(0, 479))
        random_radius = randint(1, 200)
        pygame.draw.circle(screen, random_color, random_pos, random_radius)
        #pygame.display.update()

    if len(points) >= 3:
        pygame.draw.polygon(screen, (0, 255, 0), points)
    for point in points:
        pygame.draw.circle(screen, (0, 0, 255), point, 5)

    pygame.display.update()
