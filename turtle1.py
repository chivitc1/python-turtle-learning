"""
turtle1.py
Draws a pattern using a hexagon.
"""
from turtle import *


def main():
    reset()
    speed(0)
    pensize(2)
    hideturtle()
    color('blue', 'yellow')
    begin_fill()

    for count in range(10):
        for count in range(6):
            forward(70)
            left(60)
        left(36)
    end_fill()
    return "Done!"


if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()