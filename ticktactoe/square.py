"""
File: square.py
Defines the Square class.
"""
from turtle import Turtle

class Square(Turtle):
    """Represents a Tic-Tac-Toe square."""

    FONT = ('Arial', '12', 'bold')     # Class level variable
    EMPTY = ''

    def __init__(self, index, grid, length, xPos, yPos,
                 outlineColor='black', fillColor='white', text=EMPTY):
        """Sets the initial state of the Tic-Tac-Toe square."""
        Turtle.__init__(self, shape="square", visible=False)
        self.speed(0)
        self.color(outlineColor, fillColor)
        self.up()
        self.goto(xPos, yPos)
        self.resizemode(rmode="user")
        self.shapesize(stretch_wid=length / 20, stretch_len=length / 20)
        self._text = text
        self._index = index
        self._grid = grid
        self.onclick(lambda x, y: self._grid.makeMove(self._index))
        self.showturtle()

    def text(self, text=None):
        """Getter, setter for _text"""
        if not text is None:
            self._text = text
            self.write(text, align='center', font=Square.FONT)

        return self._text