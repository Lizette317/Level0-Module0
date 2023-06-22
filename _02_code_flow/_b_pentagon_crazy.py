import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def get_next_color(i):
    return colors[i % len(colors)]


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('black')
    window.setup(width=0.75, height=0.9, startx=0, starty=0)

    colors = ('red', 'blue', 'green', 'yellow', 'orange')

    # Make a new turtle
    t = turtle.Turtle()
    # Make the turtle shape 'turtle', .shape('turtle')
    t.shape('turtle')
    # Set the turtle speed to max (0)
    t.speed(0)
    # Set the turtle width to 1
    t.width(1)
    # Create a variable to hold the number of sides in a pentagon
    p = 5
    # Create a variable to be the angle of 360 divided by the sides variable
    r = 360 / p
    # Use a for loop to repeat ALL the following lines of code 360 times. 
    for i in range(360):
        t.forward(79)
