# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

dir_color = {1:sd.COLOR_RED,
             2:sd.COLOR_ORANGE,
             3:sd.COLOR_YELLOW,
             4:sd.COLOR_GREEN,
             5:sd.COLOR_CYAN,
             6:sd.COLOR_BLUE,
             7:sd.COLOR_PURPLE,}

def draw_figure(point, amount_angles, angle, color, lenght):
    delta_angle = 360/amount_angles
    for i in range(0, amount_angles, 1):
        cur_angle = angle + (delta_angle * i)
        if i == 0:
            point = point
        else:
            point = v1.end_point
        v1 = sd.get_vector(start_point=point, angle=cur_angle, length=lenght, width=2)
        v1.draw(color)

# определить функцию рисования треугольника из заданной точки с заданным наклоном
def triangle(point, color, angle=0, lenght = 150):
    amount_angles = 3
    draw_figure(point, amount_angles, angle, color, lenght)

def squre(point, color, angle=0, lenght = 150):
    amount_angles = 4
    draw_figure(point, amount_angles, angle, color, lenght)

def pentagon(point, color, angle=0, lenght = 150):
    amount_angles = 5
    draw_figure(point, amount_angles, angle, color, lenght)

def hexagon(point, color, angle=0, lenght = 150):
    amount_angles = 6
    draw_figure(point, amount_angles, angle, color, lenght)
print("Доступные цвета",
    "1 : RED",
    "2 : ORANGE",
    "3 : YELLOW",
    "4 : GREEN",
    "5 : CYAN",
    "6 : BLUE",
    "7 : PURPLE",
    sep = "\n")
user_input = input("Выберите цвет:")
if user_input.isdigit():
    user_input = int(user_input)
    if user_input in dir_color:
        my_color = dir_color[user_input]
        point_0 = sd.get_point(100, 100)
        triangle(point_0, my_color, 0)
        point_0 = sd.get_point(100, 400)
        squre(point_0, my_color, 0)
        point_0 = sd.get_point(350, 350)
        pentagon(point_0, my_color, 0)
        point_0 = sd.get_point(350, 50)
        hexagon(point_0, my_color, 0, 50)
        sd.pause()
    else:
        print("Введите значение из списка")
else:
    print("Введено некорректное значени")
# point_0 = sd.get_point(100, 100)
# triangle(point=point_0, angle=0)
# point_0 = sd.get_point(100, 400)
# squre(point=point_0, angle=0)
# point_0 = sd.get_point(350, 350)
# pentagon(point=point_0, angle=0)
# point_0 = sd.get_point(350, 50)
# hexagon(point=point_0, angle=0)
#

