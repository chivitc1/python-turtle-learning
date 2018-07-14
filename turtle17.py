"""
testpoly.py
Illustrates the use of begin_poly, end_poly, and get_poly to
create custom turtle shapes.
"""
from turtle import *


def regularPolygon(length, numSides):
    """Draws a regular polygon.
    Arguments: the length and number of sides."""
    iterationAngle = 360 / numSides
    for count in range(numSides):
        forward(length)
        left(iterationAngle)


def makeShape(length, numSides, shapeName):
    """Creates and registers a new turtle shape with the given name.
    The shape is a regular polygon with the given length and number
    of sides.
    Arguments: the length, number of sides, and shape name."""
    up()
    goto(0,0)
    setheading(0)
    begin_poly()
    regularPolygon(length, numSides)
    end_poly()
    shape = get_poly()
    addshape(shapeName, shape)


def main():
    """Creates two turtles with custom shapes and allows you
    to drag them around the window."""
    hideturtle()
    speed(0)
    makeShape(length=40, numSides=5, shapeName="pentagon")
    makeShape(length=20, numSides=8, shapeName="octagon")
    turtle1 = Turtle(shape="pentagon")
    turtle1.color("brown", "green")
    turtle1.up()
    turtle1.goto(100, 50)
    turtle1.tilt(angle=90)

    turtle2 = Turtle(shape="octagon")
    turtle2.color("blue", "pink")
    turtle2.up()

    turtle1.ondrag(lambda x, y: turtle1.goto(x, y))
    turtle2.ondrag(lambda x, y: turtle2.goto(x, y))
    listen()
    return "Done!"


if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()