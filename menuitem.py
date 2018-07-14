"""
File: menuitem.py
Defines a class for menu items.

A menu item has a position in the window, a shape, a color, and a callback function.
A callback function is triggered when a user event, such as a mouse click, occurs
"""
from turtle import Turtle


class MenuItem(Turtle):
    """Represent a menu item"""
    def __init__(self, x, y, shape, color, callback):
        """Initialize states of menu item"""
        Turtle.__init__(self, shape=shape, visible=False)
        self.speed(0)
        self.up()
        self.goto(x, y)
        self.color(color, color)
        self._callback = callback

        # Pass my color to the callback function when I’m clicked
        self.onclick(lambda x, y: self._callback(color))
        self.showturtle()