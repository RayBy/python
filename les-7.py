# coding UTF-8

import turtle
import random
import math

def pengoto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def circle_paint(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

turtle.speed(0)

pengoto(0, 0)
turtle.circle(80)
pengoto(0, 160)
circle_paint(5, "red")

phi = 360/7
r = 50

for i in range(0, 7):
    phi_rad = phi*i*math.pi/180
    pengoto(math.sin(phi_rad)*r, math.cos(phi_rad)*r+60)
    turtle.circle(22)


pengoto(math.sin(phi_rad)*r, math.cos(phi_rad)*r+60)
circle_paint(22, "green")


answer = ''
while answer != "N":
    answer = turtle.textinput("Нарисовать окружность?", "Y/N")
    if answer == 'Y':
        turtle.penup()
        turtle.goto(random.randrange(1, 100), random.randrange(1, 100))
        turtle.pendown()
        turtle.fillcolor(random.random(), random.random(), random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(1, 250))
        turtle.end_fill()
    else:
        pass