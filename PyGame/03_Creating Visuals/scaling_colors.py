#!/usr/bin/env python


# Color scaling
def scale_color(color, scale):
    red, green, blue = color
    red = int(red * scale)
    green = int(green * scale)
    blue = int(blue * scale)
    print("Normal scale by x{}: ({}, {}, {})".format(scale, red, green, blue))
    saturate_color(red, green, blue)


# Color saturation
def saturate_color(red, green, blue):
    red = min(red, 255)
    green = min(green, 255)
    blue = min(blue, 255)
    print("Saturated colors: ({}, {}, {})".format(red, green, blue))


# Linear interpolation
def lerp(value1, value2, factor):
    result = value1+(value2-value1)*factor
    print(result)


fireball_orange = (221, 99, 20)

print("Original colors: {}".format(fireball_orange))
scale_color(fireball_orange, 2)

lerp(100, 200, 0)
lerp(100, 200, 1)
lerp(100, 200, 0.5)
lerp(100, 200, 0.25)
