# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd

# определить функцию рисования треугольника из заданной точки с заданным наклоном
def triangle(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=300, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=300, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=300, width=3)
    v3.draw()


point_0 = sd.get_point(300, 300)

for angle in range(0, 361, 90):
    triangle(point=point_0, angle=angle)

sd.pause()