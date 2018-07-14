"""
File: animatedturtle.py
Defines an animated turtle class.
Includes a time interval and a callback function for the timer.
Also includes a Boolean flag to pause or resume the animation.
"""
from turtle import Turtle, ontimer, showturtle


class AnimatedTurtle(Turtle):
    """Represents an animated turtle."""
    def __init__(self, shape="turtle", xPos=0, yPos=0, heading=0,
                 outlineColor="black", fillColor="black", timeInterval=1,
                 animated=True, callback=lambda t: False):
        Turtle.__init__(self, shape=shape, visible=True)
        self.speed(0)
        self.color(outlineColor, fillColor)
        self.up()
        self.goto(xPos, yPos)
        self.setheading(heading)
        self._timeInterval = timeInterval
        self._animated = animated
        self._callback = callback
        showturtle()
        self.act()

    def timeInterval(self, t=None):
        """Getter and setter for time interval."""
        if not t is None:
            self._timeInterval = t
        return self._timeInterval

    def animated(self, flag=None):
        """Getter and setter for the animated flag. If set to True,
        starts or resumes the animation."""
        if not flag is None:
            self._animated = flag
        return self._animated

    def callback(self, func=None):
        """Getter and setter for the callback function. If flag is True,
        also starts or resumes the animation."""
        if not func is None:
            self._callback = func
        return self._callback

    def act(self):
        """Performs the next callback action if the turtle is animated."""
        if not self.animated():
            return
        self._callback(self)
        ontimer(lambda: self.act(), self._timeInterval)