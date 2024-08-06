#! usr/bin/env python

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from sys import exit


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.white,
            highlight_color=color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == 'k':
                print('k button pressed')


def update():
    if held_keys['Esc']:
        exit()


app = Ursina()

for z in range(8):
    for x in range(8):
        voxel = Voxel(position = (x, 0, z))

person = FirstPersonController()

app.run()
