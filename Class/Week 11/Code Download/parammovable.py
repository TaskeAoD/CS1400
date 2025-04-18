#parammovable.py
import tkinter as tk

import tkinter.ttk as ttk
from movableLight import MovableLight
from turnlight import TurnLight
class ParameterizedMovable:
    """ Graphical window that allows a user to move and resize
    a traffic light object. """

    def __init__(self, light_class):
        """ Creates a ParameterizedLightTester.
            light_class is the type of light to create;
            it must be MovableLight or one of its subclasses. """
        root = tk.Tk() # Create the main window
        root.title("Movable Traffic Light Test") # Set title bar text
        width, height = 800, 600
        f = ttk.Frame(root, width=width, height=height)
        f.pack()
        # Place traffic light at the center of the window frame
        print("Frame width:", f.winfo_width())
        self.light_width = height//10
        self.light = light_class(f, self.light_width, "green")
        f.bind("<Button-1>", self.mouse_pressed)
        f.bind("<Key>", self.key_pressed)
        f.focus_set() # Allow graphical window to receive key strokes
        print("width//2 =", width//2, " height//2 =", height//2)
        self.light.move_to(width//2, height//2)
        # Start the GUI event loop
        root.mainloop()

    def mouse_pressed(self, event):
        """ The window manager calls this function when the user
            presses the graphical button. """
        self.light.move_to(event.x, event.y)

    def key_pressed(self, event):
        """ The window manager calls this function when the user
            presses the graphical button. """
        ch = event.char
        if ch == ">" or ch == ".":
            self.light_width += 5
            self.light.resize(self.light_width)
        elif ch == "<" or ch == ",":
            self.light_width -= 5
            self.light.resize(self.light_width)
        elif ch == "C" or ch == "c":
            self.light.change()
        print("Key pressed")

# Main program ---------------------------------------------------------------------
# Create and execute a traffic light window
print("What kind of light do you want play with?")
light = input("S)tandard T)urn: ").upper()
if light == 'S':
    ParameterizedMovable(MovableLight) # Passing class, not an instance
elif light == 'T':
    ParameterizedMovable(TurnLight) # Passing class, not an instance
else:
    print(light, "is not a valid choice")