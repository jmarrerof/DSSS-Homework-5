import turtle
import numpy as np
import random


def main(speed=0, bg_color="grey"):
    # create Turtle object
    turtle_screen = turtle.Screen()
    myTurtle = turtle.Turtle()
    
    # set speed to 'fastest = 0'
    myTurtle.speed(speed)
    # change background color
    turtle_screen.bgcolor(bg_color)

    # define colors as tuples of RGB values
    turtle_screen.colormode(255)
    colors = [(0, 0, 0),  # black
              (255, 255, 255),  # white
              (255, 0, 0),  # red
              (0, 255, 0),  # green
              (0, 0, 255),  # blue
              (128, 0, 128),  # purple
              (255, 128, 0),  # orange
              (0, 0, 128),  # navy
              (255, 255, 0),  # yellow
              (255, 0, 255)]  # magenta

    for _ in range(10):
        # define some params
        size = 18
        pos = [np.random.randint(-300, 300), np.random.randint(-300, 300)]

        # set snowflake color as one of the colors defined above
        myTurtle.pencolor(random.choice(colors))

        # Go to the start position of the snowflake
        myTurtle.penup()
        myTurtle.goto(pos[0], pos[1])
        myTurtle.pendown()

        # draw the snowflake
        for _ in range(8):
            snowflake_branch(size, myTurtle)
            myTurtle.left(45)

    turtle_screen.exitonclick()


def snowflake_branch(size, myTurtle):
    # This function draws one branch of the snowflake.
    for _ in range(3):
        for _ in range(3):
            myTurtle.forward(size / 3)
            myTurtle.backward(size / 3)
            myTurtle.right(45)
        myTurtle.left(90)
        myTurtle.backward(size / 3)
        myTurtle.left(45)
    myTurtle.right(90)
    myTurtle.forward(size)


if __name__ == "__main__":
    main()
