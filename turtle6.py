from turtle import *


def skip(x, y):
    """Moves the pen to the given location without drawing."""
    up()
    goto(x, y)
    down()


def main():
    shape("circle")
    width(2)
    speed(0)
    pencolor("blue")
    ondrag(goto)
    onscreenclick(skip)
    listen()
    return "Done!"


if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()