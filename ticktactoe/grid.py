"""
File: grid.py
Defines the TicTacToeGrid class.
"""
from ticktactoe.square import Square
from turtle import goto, tracer, up, update, write, hideturtle


class Grid(object):
    """Represents a Tic-Tac-Toe grid."""

    WIN_O = 'OOO'
    WIN_X = 'XXX'
    EMPTY = ""

    def __init__(self, length, xPos, yPos,
                 outlineColor="black", fillColor="white", letter="X"):
        """Sets the initial state of the Tic-Tac-Toe grid."""
        self._letter = letter
        self._grid = list()
        index = 0
        y = yPos
        tracer(False)
        for row in range(3):
            x = xPos
            for col in range(3):
                square = Square(index=index, grid=self, length=length, xPos=x, yPos=y,
                                outlineColor=outlineColor, fillColor=fillColor)
                self._grid.append(square)
                x += length
                index += 1
            y -= length
        update()
        tracer(True)

    def makeMove(self, index):
        """Responds to a user’s click in a square."""
        square = self._grid[index]
        if square.text() == Grid.EMPTY:
            square.text(self._letter)
            if self._letter == "X":
                self._letter = "O"
            else:
                self._letter = "X"
            winner = self._hasWinner()
            if winner:
                up()
                hideturtle()
                goto(-40, 110)
                write(winner + "wins!", font=("Arial", 24, "bold"))

    def _hasWinner(self):
        """Search for 'XXX' or 'OOO' in the grid, return 'X' or 'O' if found, otherwize return EMPTY string"""
        row0 = self._getString(0, 1, 2)
        row1 = self._getString(3, 4, 5)
        row2 = self._getString(6, 7, 8)
        col0 = self._getString(0, 3, 6)
        col1 = self._getString(1, 4, 7)
        col2 = self._getString(2, 5, 8)
        dia1 = self._getString(0, 4, 8)
        dia2 = self._getString(6, 4, 2)

        if row0 == Grid.WIN_O or row1 == Grid.WIN_O or row2 == Grid.WIN_O or \
            col0 == Grid.WIN_O or col1 == Grid.WIN_O or col2 == Grid.WIN_O or \
            dia1 == Grid.WIN_O or dia2 == Grid.WIN_O:
            return "O"
        elif row0 == Grid.WIN_X or row1 == Grid.WIN_X or row2 == Grid.WIN_X or \
            col0 == Grid.WIN_X or col1 == Grid.WIN_X or col2 == Grid.WIN_X or \
            dia1 == Grid.WIN_X or dia2 == Grid.WIN_X:
            return "X"
        else:
            return Grid.EMPTY

    def _getString(self, one, two, three):
        """Builds and returns a string from a row, column,
        or diagonal of the grid."""
        return self._grid[one].text() + self._grid[two].text() + self._grid[three].text()