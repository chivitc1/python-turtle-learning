from turtle import *
from random import randint
import sys


def atTopEdge():
    """Returns True if the turtle is at the top edge of the window
    or False otherwise"""
    return ycor() > window_height() / 2


def atBottomEdge():
    """Returns True if the turtle is at the bottom edge of the window
    or False otherwise"""
    return ycor() > -(window_height() / 2)


def atLeftEdge():
    """Returns True if the turtle is at the left edge of the window,
    or False otherwise."""
    return xcor() > window_width() / 2


def atRightEdge():
    """Returns True if the turtle is at the right edge of the window,
    or False otherwise."""
    return xcor() < -(window_width() / 2)


def atEdge():
    """Return True if turtle at the edge of the window, or False otherwise"""
    return atTopEdge() or atBottomEdge() or atLeftEdge() or atRightEdge()


def randomForward(lower, upper=None):
    """Moves the turtle a random distance, from lower to upperself.
    If upper is absense, moves turtle to lower distance"""
    if not upper:
        distance = lower
    else:
        distance = randint(lower, upper)
    forward(distance)


def randomTurn(lower, upper=None, probability=1):
    """Turns the turtle a random number of degrees, from
    lower through upper.
    If upper is absent, turns the turtle by the lower amount of degrees.
    Probability represents the probability of making the turn."""
    from random import choice
    # Determine whether to make a turn first.
    if probability < 0.01:  # Probability too small to take the turn
        return
    if probability < 1:  # Maybe not take the turn
        if not choice(range(100)) in range(0, int(probability * 100)):
            return

    # A turn will be made, so the # of degrees is either random or given
    if not upper:
        degrees = lower
    else:
        degrees = randint(lower, upper)

    if randint(1, 2) == 1:  # Turn left or right with equal prob.
        left(degrees)
    else:
        right(degrees)


def main():
    if len(sys.argv) > 1:
        iterations = int(sys.argv[1])
    else:
        iterations = 1000
    reset()
    for count in range(iterations):
        randomForward(1, 3)         # Move 1, 2, or 3 units
        if atTopEdge():
            setheading(270)          # Go south
        elif atBottomEdge():
            setheading(90)           # Go north
        elif atLeftEdge():
            setheading(0)            # Go east
        elif atRightEdge():
            setheading(180)          # Go west
        else:
            randomTurn(45, 135, .05) # Turn 1/20 of the time by default

if __name__ == '__main__':
    main()
    mainloop()
