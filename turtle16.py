"""
animate2.py
The turtle turns 180 degrees when it reaches the window edges.
"""
from turtle import *


def act():
    """Bounce back and forth, forever."""
    if window_height() // 2 - 20 <= abs(ycor()) or \
        window_width() // 2 - 20 <= abs(xcor()):
        left(180)
    forward(4)
    ontimer(act, 1)


def main():
    """Start the timer with the move function.
    A user click exits the program."""
    reset()
    shape("turtle")
    speed(0)
    up()
    exitonclick() # Quit the program when the user clicks the mouse
    listen()
    ontimer(act, 1)
    return "Done!"


if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()