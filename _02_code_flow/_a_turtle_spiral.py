import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    turtle = turtle.Turtle()
    # This code sets our shape to a turtle
    turtle.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    turtle.speed(0)
    # Set your turtle's color using .color('green')
    turtle.color('green')
    # Use a loop to repeat a the code below 50 times
    for i in range(50):
        turtle.color(get_random_color())
        turtle.forward(5*i)
        turtle.right(360/7)
        turtle.width(i)
    # Set the turtle color to a random color
    turtle.color(get_random_color())
    # Move the turtle (5*i) pixels. 'i' is the loop variable
        
    # Turn the turtle (360/7) degrees to the right
         
    # Change the turtle width to 'i' (the loop variable)
        
    # Check the pattern against the picture in the recipe. If it matches, you are done!
    turtle.forward(2)
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
