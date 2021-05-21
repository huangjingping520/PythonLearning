import turtle
import math

w, h = 720, 580
length, heading_ = 200, 90


def fractal_tree(length, heading, diff_value=50):
    turtle.pensize(length/10)
    turtle.seth(heading)
    turtle.forward(length)
    turtle.left(30)
    turtle.forward(length-diff_value)
    turtle.backward(length-diff_value)
    if length-diff_value > diff_value-1:
        fractal_tree(length-diff_value, turtle.heading())
    turtle.pensize(length/10)
    turtle.right(60)
    turtle.forward(length-diff_value)
    turtle.backward(length-diff_value)
    if length-diff_value > diff_value-1:
        fractal_tree(length-diff_value, turtle.heading())
    turtle.pensize(length/10)
    turtle.seth(heading)
    if length-diff_value > diff_value-1:
        heart(length-diff_value)
    turtle.backward(length)


def heart(length, r=15, angle=40):
    turtle.penup()
    turtle.forward(length)
    turtle.fillcolor("red")
    turtle.begin_fill()
    heading_bk = turtle.heading()
    turtle.right(angle)
    turtle.forward(2*r/math.sin(math.pi/180*angle))
    turtle.seth(heading_bk)
    turtle.circle(r, 180)
    turtle.seth(heading_bk)
    turtle.circle(r, 180)
    turtle.left(angle)
    turtle.forward(2*r/math.sin(math.pi/180*angle))
    turtle.end_fill()
    turtle.pendown()
    turtle.seth(heading_bk)


turtle.setup(w, h)
turtle.penup()
turtle.goto(0, -h/2)
turtle.pendown()
fractal_tree(length, heading_)
turtle.done()
