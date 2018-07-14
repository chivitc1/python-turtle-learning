from turtle import *

def main():
    reset()
    pensize(2)
    hideturtle()

    (length, numSides, outline, background) = (30, 6, "blue", "yellow")

    poly_len = numinput("Input Dialog", "Enter the length of polygon",
        default=30, minval=0, maxval=600)
    if poly_len:
        length = int(poly_len)
        print(length)


    poly_sides = numinput("Input Dialog", "Enter the number of sides [1-8]",
        default=6, minval=3, maxval=8)
    if poly_sides:
        numSides = int(poly_sides)
        print(numSides)

    pen_color = textinput("Input Dialog", "Enter the pen color")
    if pen_color:
        outline = pen_color
        print(outline)

    bg_color = textinput("Input Dialog", "Enter the background color")
    if bg_color:
        background = bg_color
        print(background)


    color(outline, background)
    begin_fill()
    regular_polygon(length, numSides)
    end_fill()

def regular_polygon(length, num_sides):
   """
   Draws a regular polygon with the given length
   and number of sides.
   """
   interior_angle = 360 / num_sides
   for count in range(num_sides):
       forward(length)
       left(interior_angle)

if __name__ == '__main__':
    main()
    mainloop()
