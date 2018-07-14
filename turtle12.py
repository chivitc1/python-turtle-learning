from turtle import *
from random import randint, random


def randomColor():
    """Return random RGB color"""
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def randomDegree():
    return (random() - 0.5) * 180


def randomDistance():
    return int((random() - 0.5) * 100)


def main(iterations=30, numTurtles=4):
    #Initialize list of turtle
    turtles = []

    for i in range(numTurtles):
        t = Turtle(shape="turtle")
        t.color(randomColor())
        turtles.append(t)

    # Make them wander around for a fixed number of iterations
    for i in range(iterations):
        for t in turtles:
            t.left(randomDegree())
            t.forward(randomDistance())


if __name__ == '__main__':
    main()
    mainloop()