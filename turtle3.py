from turtle import *


def linear(x):
    return 2*x + 10


def quadratic(x):
    return x**2 -2*x + 1


def plot(func, x1, x2, label):
    """Plots f(x) for the domain x1..x2."""
    up()
    y = func(x1)
    goto(x1, y)
    down()
    for x in range(x1 + 1, x2 + 2):
        y = func(x)
        goto(x, y)
    write(label, font=('Arial', 16, 'bold'))


def main():
    reset()
    plot(quadratic, -10, 10, 'Quadratic')


if __name__ == '__main__':
    main()
    mainloop()