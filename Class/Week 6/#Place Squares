import turtle
import TrackMouse

def draw_squares(x, y):
    turtle.penup()
    turtle.setheading(0)
    TrackMouse.report_position(x,y)
    turtle.setposition(x - 50, y - 50)
    turtle.pendown()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.update()

turtle.tracer()
turtle.hideturtle()
turtle.onscreenclick(draw_squares)
turtle.mainloop()