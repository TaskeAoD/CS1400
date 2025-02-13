import turtle
import random

def polygon(sides, length, x, y, color="black", fill=False):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.color(color)
    if fill:
        turtle.begin_fill()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360//sides)
    if fill:
        turtle.end_fill()
        
turtle.hideturtle()
turtle.tracer(0)

polygon(3, 30, 10, 10)
polygon(4, 30, 50, 50, "blue")
polygon(5, 30, 100, 100, "green", True)
polygon(6, 30, -200, -200, 'purple', False)
polygon(12, 30, 200, 10, "#BB7FFF", True) #wanted to use hex, make sure to include '#' for it to work

turtle.update()
turtle.exitonclick()