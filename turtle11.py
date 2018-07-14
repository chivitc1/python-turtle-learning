from turtle import *
from random import randint


# Data to track performance
stats = {"calls": 0, "rectangles": 0}


def drawRectangle(x1, y1, x2, y2):
    """Draws a rectangle with the given corner points
    using a random color."""
    stats["rectangles"] = stats["rectangles"] + 1
    (red, green, blue) = randomColor()
    pencolor(red, green, blue)
    up()
    goto(x1, y1)
    down()
    goto(x1, y2)
    goto(x2, y2)
    goto(x2, y1)
    goto(x1, y1)


def randomColor():
    return (randint(1, 255), randint(1, 255),randint(1, 255))


def mondrian(x1, y1, x2, y2, level):
    """Draws a Mondrian-like painting at the given level."""
    stats["calls"] = stats["calls"] + 1

    if level > 0:
        drawRectangle(x1, y1, x2, y2)
        vertical = randint(1, 2)
        if (vertical == 1):
            mondrian(x1, y1, (x2-x1) / 3 + x1, y2, level - 1)
            mondrian((x2 - x1) / 3 + x1, y1, x2, y2, level - 1)
        else:
            mondrian(x1, y1, x2, y1 - (y1 - y2) / 3, level - 1)
            mondrian(x1, y1 - (y1 - y2) / 3, x2, y2, level - 1)


def main():
    # Reset the stats on each call of main.
    stats["calls"] = 0
    stats["rectangles"] = 0

    # Obtain the level from the user.
    level = numinput("Input dialog", "Enter the level", default=1, minval=1)

    if not level:
        level = 1
    paintingWidth = window_width() // 2 - 20
    paintingHeight = window_height() // 2 - 20

    hideturtle()
    speed(0)
    pensize(2)

    # Delay drawing if level is greater than 6.
    if level > 6:
        tracer(False)

    mondrian(-paintingWidth, paintingHeight, paintingWidth, -paintingHeight, level)

    # Draw now if level is greater than 6.
    if level > 6:
        update()

if __name__ == '__main__':
    main()
    mainloop()