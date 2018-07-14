"""
File: app.py
A Tic-Tac-Toe application.
"""

from ticktactoe.grid import Grid
from turtle import bgcolor, hideturtle, mainloop, pencolor, title


def main():
    hideturtle()
    bgcolor("black")
    pencolor("white")
    title("Tic-Tac-Toe")
    Grid(length=70, xPos=-70, yPos=70, outlineColor="blue", fillColor="gray")
    return "Done!"


if __name__ == '__main__':
    main()
    mainloop()