from turtle13 import RegularPolygon
from turtle import mainloop
from time import sleep

def main():
    DELAY = 0.5
    poly = RegularPolygon(length=40, xPos=50, yPos=50, heading=0, sides=6, outlineColor="green", fillColor="red")
    sleep(DELAY)
    poly.translate(20, 20)
    sleep(DELAY)
    poly.translate(-20, -40)

    sleep(DELAY)

    poly.fillOn(True)

    for i in range(10):
        poly.rotate(15)
        sleep(DELAY)

    for i in range(10):
        poly.rotate(-15)
        sleep(DELAY)

    for i in range(5):
        poly.scale(1.2)
        sleep(DELAY)

    for i in range(5):
        poly.scale(1/1.2)
        sleep(DELAY)


if __name__ == '__main__':
    main()
    mainloop()