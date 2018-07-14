"""
animate1.py
Animates the turtle using the ontimer function.
"""
from turtle import *


def act():
    """Move forward and turn a bit, forever."""
    left(2)
    forward(2)
    ontimer(act, 1)


def main():
    """Start the timer with the move function.
    The user’s click exits the program."""
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