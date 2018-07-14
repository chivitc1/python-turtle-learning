"""
File:
Defines a RegularPolygon class.
"""
from turtle import Turtle, bgcolor


class RegularPolygon(object):
    """Represents a regular polygon."""

    def __init__(self, length, xPos, yPos, heading, sides=3,
                 outlineColor="black", fillColor="black",
                 fillOn=False, isVisible=True):
        """Sets the initial state of the polygon."""

        self._turtle = Turtle(visible=False)  # Always hide the turtle
        self._turtle.speed(0)
        self._length = length
        self._xPos = xPos
        self._yPos = yPos
        self._heading = heading
        self._sides = sides
        self._outlineColor = outlineColor
        self._fillColor = fillColor
        self._fillOn = fillOn
        self._isVisible = isVisible
        if isVisible:  # Display the polygon if it’s
            self.show()  # visible

    def _draw(self):
        """Draws a regular polygon with the given turtle,
        length and number of sides."""

        interiorAngle = 360 / self._sides
        self._turtle.up()
        self._turtle.setheading(self._heading)
        self._turtle.color(self.outlineColor(), self.fillColor())
        self._turtle.goto(self._xPos, self._yPos)
        self._turtle.down()
        if self.fillOn():
            self._turtle.begin_fill()
        for count in range(self._sides):
            self._turtle.forward(self._length)
            self._turtle.left(interiorAngle)
        if self.fillOn():
            self._turtle.end_fill()

    def show(self):
        """Displays the polygon."""
        self._draw()
        self._isVisible = True

    def hide(self):
        """Erases the polygon."""
        oldOutline = self.outlineColor()  # Save the current colors
        oldFill = self.fillColor()

        erasingColor = bgcolor()
        self._outlineColor = erasingColor
        self._fillColor = erasingColor
        self._turtle.pensize(3)     # Make sure outline go away
        self._draw()

        self._outlineColor = oldOutline     # Restore color
        self._fillColor = oldFill
        self._turtle.pensize(1)
        self._isVisible = False

    def outlineColor(self, value=None):
        """Getter and setter for the outline color."""
        if value:
            self._outlineColor = value
            if self.isVisible():
                self.show()
        return self._outlineColor

    def fillColor(self, value=None):
        """Getter and setter for fill color"""
        if value:
            self._fillColor = value
            if self.isVisible():
                self.show()
        return self._fillColor

    def fillOn(self, value=None):
        """Getter and setter for fillOn"""
        if value:
            self._fillOn = value
            if self.isVisible():
                self.show()
        return self._fillOn

    def isVisible(self):
        return self._isVisible

    def translate(self, x, y):
        """Move polygon x, y distance"""
        visible = self.isVisible()
        if self.isVisible():
            self.hide()

        self._xPos += x
        self._yPos += y

        if visible:
            self.show()

    def scale(self, factor):
        """Change the size of polygon by given factor"""
        visible = self.isVisible()
        if self.isVisible():
            self.hide()

        self._length *= factor

        if visible:
            self.show()

    def rotate(self, degree):
        """Rotate polygon by degree"""
        visible = self.isVisible()
        if visible:
            self.hide()

        self._heading += degree

        if visible:
            self.show()

    def mainloop(self):
        mainloop()