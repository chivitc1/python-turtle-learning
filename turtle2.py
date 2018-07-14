from turtle import *
from random import randint

def main():
    radian_pattern(regular_polygon)

def radian_pattern(polygon_func):
    for count in range(10):
        polygon_func(70, 4)
        left(36)

def randomcolor():
    """Return a random RGB color."""
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def regular_polygon(length, num_sides):
    """
    Draws a regular polygon with the given length
    and number of sides.
    """
    interior_angle = 360 / num_sides
    for count in range(num_sides):
        forward(length)
        left(interior_angle)

if __name__ == '__main__':
    main()
    mainloop()

