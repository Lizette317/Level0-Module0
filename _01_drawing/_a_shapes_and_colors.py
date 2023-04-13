import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    my_turtle = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    turtle.shape("turtle")
    # Set your turtle's speed using .speed(2)
    turtle.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    turtle.color('green')
    turtle.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)
    # Move your turtle left or right using .left(90) or .right(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    turtle.penup()
    turtle.goto(-200,100)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius=50, steps=30)
    turtle.end_fill()
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    turtle.penup()
    turtle.goto(200,200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("violet")
    turtle.circle(radius=65, steps=30)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-200, -75)
    turtle.pendown()
    turtle.fillcolor("cornflower blue")
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(200, -75)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
