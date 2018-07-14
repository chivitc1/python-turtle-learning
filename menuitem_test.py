"""
menuitem_test.py
A simple tester program for menu items.
"""
from turtle import *
from menuitem import MenuItem
from flag import Flag

INDENT = 30
START_Y = 100
ITEM_SPACE = 30

menuClick = Flag()

def changePenColor(c):
    """Changes the system turtle’s color to c."""
    menuClick.value(True)
    color(c)


def createMenu(callback):
    """Displays 6 menu items to respond to the given callback function."""

    x = -(window_width() / 2) + INDENT
    y = START_Y
    colors = ("red", "green", "blue", "yellow", "purple", "black")
    shape = "circle"
    for color in colors:
        MenuItem(x, y, shape, color, callback)
        y -= ITEM_SPACE


def skip(x, y):
    "Moves the pen to the given location without drawing."
    if not menuClick.value():
        up()
        goto(x, y)
        down()
    else:
        menuClick.value(False)  # Reset when menu item selected

def main():
    """Creates a menu for selecting colors."""
    reset()
    shape("triangle")
    createMenu(changePenColor)
    onscreenclick(skip)
    listen()
    return "Done"


if __name__ == '__main__':
    main()
    mainloop()