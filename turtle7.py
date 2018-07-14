from turtle import reset, pencolor, speed, width, onkey, listen, mainloop, forward, backward, right, left, clear

def main():
    reset()
    pencolor("blue")
    speed(0)
    width(2)
    onkey(clear, "c")
    onkey(lambda: forward(5), "Up")
    onkey(lambda : backward(5), "Down")
    onkey(lambda : right(5), "Right")
    onkey(lambda : left(5), "Left")

    onkey(lambda: forward(5), "w")
    onkey(lambda: backward(5), "s")
    onkey(lambda: right(5), "d")
    onkey(lambda: left(5), "a")
    listen()


if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
