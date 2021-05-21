import turtle
import math


def draw(r, angle=40):
    print((5*r, 0, 5*r))
    turtle.pencolor((5*r, 0, 5*r))
    turtle.seth(45)
    turtle.forward(2*r)
    turtle.circle(r, 180)
    turtle.right(90)
    turtle.circle(r, 180)
    turtle.forward(2*r)
    if r+5 < 100:
        draw(r+5)


turtle.colormode(255)
turtle.pensize(5)
draw(r=10)
