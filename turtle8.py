"""
draw a triangle with just three clicks
On the
first mouse click, the turtle skips to that position, without drawing. On the second
mouse click, the turtle draws a line segment connecting the first two vertices. On the
third mouse click, the turtle draws two more line segments to complete the figure

- If the list is empty, skip to the click position and add the click position to the list.
- If the list contains one position, go to the click position (drawing a line segment from
the first position) and add the click position to the list.
- If the list contains two positions, draw line segments from each of them to the click
position, and make the list empty again
"""

from turtle import *


positionHistory = []


def setVertex(x, y):
    """Set vertices and possibly connect them"""
    if len(positionHistory) == 0:
        positionHistory.append((x, y))
        skip(x, y)
    elif len(positionHistory) == 1:
        positionHistory.append((x, y))
        goto(x,y)
    else:
        (xCoord, yCoord) = positionHistory.pop()
        skip(xCoord, yCoord)
        goto(x, y)
        (xCoord, yCoord) = positionHistory.pop()
        goto(xCoord, yCoord)


def skip(x, y):
    """Moves the pen to the given location without drawing."""
    up()
    goto(x, y)
    down()


def main():
    width(2)
    speed(0)
    pencolor("blue")
    onscreenclick(setVertex)
    listen()
    return "Done!"


if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()