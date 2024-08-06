#!/usr/bin/env python

import random
import pygame

from math import *
from datetime import datetime


def area_of_circle(radius):
    return pi*radius**2


def time_now():
    the_time = datetime.now()
    # date_now = datetime.date("now")
    # time_now = datetime.time()

    print(the_time.ctime())
    # print(date_now)
    # print(time_now)


def rand():
    random.seed(100)
    for roll in range(10):
        print(random.randint(1, 6))
    print("Re-seeded")
    random.seed(100)
    for roll in range(10):
        print(random.randint(1, 6))


def pygame_module():
    print("Pygame version: {}".format(pygame.ver))


print(area_of_circle(5))
time_now()
rand()
pygame_module()
