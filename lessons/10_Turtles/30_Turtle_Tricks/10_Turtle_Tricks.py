"""
For this program, you will tell Tina the Turtle to draw a triangle.

You should look at the previous programs to see how to use the turtle commands.
Copy lines of code from those programs to this one to draw a triangle.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

tina.left (180)
tina.forward (40)
tina.right(45)
tina.forward(90)
tina.left(35)
tina.forward(50)
tina.left(90)
tina.forward(25)
tina.circle(25,100)
tina.right(100)
tina.forward(25)
tina.left(180)
tina.forward(85)
tina.left(180)
tina.forward(13)
tina.right(90)
tina.circle(25,180)
tina.left(90)
tina.forward(10)
tina.right(90)
tina.forward(15)
tina.left(90)
tina.forward(30)
tina.left(90)
tina.forward(15)
tina.hideturtle()
turtle.exitonclick()                    # Close the window when we click on it