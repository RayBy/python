# coding UTF-8

import turtle
import random
import math

PHI = 360/7
R = 50


def pengoto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def circle_paint(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def baraban(base_x, base_y):
    # Прорисовка основного круга
    pengoto(base_x, base_y)
    turtle.circle(80)
    # Прорисовка мушки
    pengoto(base_x, base_y+160)
    circle_paint(5, "red")
    # Прорисовка барабана
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180
        pengoto(base_x+math.sin(phi_rad) * R, base_y+math.cos(phi_rad) * R + 60)
        circle_paint(22, 'white')

def roll(base_x, base_y, start):
    for i in range(start, random.randrange(7, 100)):
        phi_rad = PHI * i * math.pi / 180
        pengoto(base_x+math.sin(phi_rad) * R, base_y+math.cos(phi_rad) * R + 60)
        circle_paint(22, 'green')
        circle_paint(22, 'white')

    pengoto(base_x+math.sin(phi_rad) * R, base_y+math.cos(phi_rad) * R + 60)
    circle_paint(22, 'green')

    return i % 7

answer = ''
start = 0
turtle.speed(0)

baraban(100, 100)

while answer != "N":
    answer = turtle.textinput("Сыграем в русскую рулетку?", "Y/N")

    if answer == 'Y':
       start = roll(100, 100, start)

    if start == 0:
        pengoto(-100, -150)
        turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))
    else:
        pengoto(-100, -150)
        turtle.write("Вы победили!", font=("Arial", 18, "normal"))
else:
    pass