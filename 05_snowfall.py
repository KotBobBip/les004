# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
active_snowflakes = 20
listDeathSnowflakes = []

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def appentSnowflake(point_list):
    x = sd.random_number(0, 600)
    y = sd.random_number(300, 600)
    snow_len = sd.random_number(10, 100)
    point_list.append([sd.get_point(x, y), snow_len])
    # len_list.append(snow_len)

list_point = []
# list_len = []
i = 0


while i <= N:
    # x = sd.random_number(0, 600)
    # y = sd.random_number(400, 600)
    # snow_len = sd.random_number(10, 100)
    # list_point.append(sd.get_point(x, y))
    # list_len.append(snow_len)
    appentSnowflake(list_point)
    i += 1

while True:
    # sd.clear_screen()
    sd.start_drawing()

    for curPoint in list_point:
        sd.snowflake(curPoint[0], curPoint[1], sd.background_color)

    for curPoint in list_point:

        delta_x = sd.random_number(-10, 10)
        delta_y = sd.random_number(1, 10)
        if curPoint[0].y > curPoint[1]/2:
            curPoint[0].y = curPoint[0].y - delta_y
            curPoint[0].x = curPoint[0].x - delta_x
        else:
            curPoint[0].y = curPoint[1]/2

            if curPoint not in listDeathSnowflakes:
                listDeathSnowflakes.append(curPoint)
                appentSnowflake(list_point)

        sd.snowflake(curPoint[0], curPoint[1])

    sd.finish_drawing()
    sd.sleep(0.1)

    if sd.user_want_exit():
        break


sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


