# Import Library
import turtle
import random

# Preliminary commands.
turtle.title("Rotating Colorful Squares and Disks")
turtle.speed(0)
turtle.colormode(255)
turtle.hideturtle()

# Asks user for Input. Input used as the side length of the square, between 20-60.
length = turtle.numinput("Input", "Please enter the side length of the first square [20-60]:", 40, 20, 60)

# As i'm too lazy to write down double codes, i'm using a function.
# The function asks for parameter (x, y) for coordinates, (alignment) turtle alignment, \n
# (len) length of asked polygon, (deg) degrees varying each polygon
def paint(x, y, alignment, n, len, steps, deg):
    # Precaution for moving the cursor
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(alignment)
    turtle.down()

    for i in range(n):
        # Generates random number between 0-255, for coloring (r, g, b)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.fillcolor(r, g, b)

        # Making the polygon
        turtle.begin_fill()
        if(n == 72):
            for j in range(4): # Making the Rectangle
                turtle.forward(len + i*2)
                turtle.right(90)
        if(n == 36):
            turtle.circle(len - i*2) # Making the Circle
        turtle.end_fill()

        turtle.right(deg)

    # Precaution for moving the cursor
    turtle.up()

paint(-150, 0, 180, 72, length, 4, 5) # For the first task, Squares
paint(250, 0, 0, 36, (length + 72*2)/2, None, -10) # For the second task, Circles

# Writing the comment at the end
turtle.goto(0, -370)
turtle.color("blue")
turtle.write("There are 72 Squares and 36 Disks", True, align = "center", font = ("Arial", 18, "bold"))

# Viewing the program result
turtle.exitonclick()