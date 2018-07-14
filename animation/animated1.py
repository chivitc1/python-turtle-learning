"""
File: animate1.py
Creates two animated turtles. One bounces back and forth, while
the other revolves in a circular pattern.
"""
from animation.animatedturtle import AnimatedTurtle
from turtle import hideturtle, listen, mainloop, onscreenclick, window_height, window_width, reset, colormode
from random import choice, randint


FORWARD_DISTANCE = 4
TURN_DEGREE = 8
TURN_DISTANCE = 8

COLORS = ("black", "green", "blue", "yellow", "red")

def pauseOrResume(turtles):
    """Pauses or resumes the animation."""
    for t in turtles:
        t.animated(not t.animated)


def rebound(aTurtle):
    """Callback function that fires on each timer event.
    Moves forward until an edge is encountered, then turns
    about face."""
    if window_height() // 2 - 20 <= abs(aTurtle.ycor()) or \
        window_width() // 2 - 20 <= abs(aTurtle.xcor()):
        aTurtle.left(180)
    aTurtle.forward(FORWARD_DISTANCE)


def twirl(aTurtle):
    """Callback function that fires on each timer event.
    Turns and moves forward, as in a circle."""
    aTurtle.left(TURN_DEGREE)
    aTurtle.forward(TURN_DISTANCE)


def randomColor():
    """Returns a random RGB value."""
    # return choice(COLORS)
    return randint(0, 255), randint(0, 255), randint(0, 255)


def main():
    reset()
    hideturtle()
    colormode(cmode=255)
    sleepyTurtle = AnimatedTurtle(heading=0, fillColor=randomColor(), callback=rebound)
    speedyTurtle = AnimatedTurtle(heading=90, fillColor=randomColor(), callback=twirl)

    turtles = (sleepyTurtle, speedyTurtle)
    onscreenclick(lambda x, y: pauseOrResume(turtles))
    listen()
    return "Done"


if __name__ == '__main__':
    main()
    mainloop()