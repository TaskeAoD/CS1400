#Trackmouse

import turtle
def report_position(x, y):
    print(f"x= {x}, y= {y}", flush=True)
    
turtle.onscreenclick(report_position)

turtle.mainloop()