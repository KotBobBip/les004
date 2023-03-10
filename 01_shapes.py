# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def draw_figure(point, amount_angles, angle):
    delta_angle = 360/amount_angles
    for i in range(0, amount_angles, 1):
        cur_angle = angle + (delta_angle * i)
        if i == 0:
            point = point
        else:
            point = v1.end_point
        v1 = sd.get_vector(start_point=point, angle=cur_angle, length=150, width=2)
        v1.draw()

# определить функцию рисования треугольника из заданной точки с заданным наклоном
def triangle(point, angle=0):
    amount_angles = 3
    draw_figure(point, amount_angles, angle)

def squre(point, angle=0):
    amount_angles = 4
    draw_figure(point, amount_angles, angle)

def pentagon(point, angle=0):
    amount_angles = 5
    draw_figure(point, amount_angles, angle)

def hexagon(point, angle=0):
    amount_angles = 6
    draw_figure(point, amount_angles, angle)

point_0 = sd.get_point(100, 100)
triangle(point=point_0, angle=0)
point_0 = sd.get_point(100, 400)
squre(point=point_0, angle=0)
point_0 = sd.get_point(350, 350)
pentagon(point=point_0, angle=0)
point_0 = sd.get_point(350, 50)
hexagon(point=point_0, angle=0)
sd.pause()

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
