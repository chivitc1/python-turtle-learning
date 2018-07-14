from turtle import *


def make():
    shape = Shape("compound")
    fuselage = ((0, 0), (25, 0), (25, 10), (0, 10))
    noseCone = ((25, 0), (35, 5), (25, 10))
    fin1 = ((0, 10), (-5, 30), (10, 10))
    fin2 = ((0, 0), (-5, -20), (10, 0))
    shape.addcomponent(noseCone, "pink", "black")
    shape.addcomponent(fuselage, "red", "black")
    shape.addcomponent(fin1, "green", "black")
    shape.addcomponent(fin2, "green", "black")
    addshape("rocket", shape)


def main():
    reset()
    hideturtle()
    make()
    Mercury = Turtle(shape="rocket")
    Mercury.tilt(90)
    Mercury.left(90)


if __name__ == '__main__':
    main()
    mainloop()