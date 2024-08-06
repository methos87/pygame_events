#!/usr/bin/env python

background_image_filename = "img/clay-banks.jpg"
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size, 0, 32)
background = pygame.image.load(background_image_filename).convert()

fullscreen = False
x, y = 0, 0
move_x, move_y = 0, 0

my_event = pygame.event.Event(KEYDOWN, key=K_UP, mod=0, unicode=u' ')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = +1
            elif event.key == K_RIGHT:
                move_x = -1
            elif event.key == K_UP:
                move_y = +1
            elif event.key == K_DOWN:
                move_y = -1
            elif event.key == K_m:
                pygame.event.set_blocked(KEYUP)
            elif event.key == K_n:
                pygame.event.set_allowed(KEYUP)
            elif event.key == K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    pygame.display.set_mode((1920, 1080), DOUBLEBUF | HWSURFACE | FULLSCREEN, 32)
                else:
                    pygame.display.set_mode(screen_size, 0, 32)
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0
            elif event.key == K_SPACE:
                pygame.event.post(my_event)

    x += move_x
    y += move_y
    screen.fill((0, 0, 0))

    # screen_width, screen_height = screen_size
    # for wy in range(0, screen_height, background.get_height()):
    #     for wx in range(0, screen_width, background.get_width()):
    #         screen.blit(background, (wx, wy))

    screen.blit(background, (x, y))
    pygame.display.update()
