"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
Mario = turtle.Turtle()                  # Create a turtle named Mario

# Use Mario.forward() and Mario.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# Mario.pencolor()

... # Your code here

Mario.forward(100)
Mario.left(72)
Mario.forward(100)
Mario.left(72)
Mario.forward(100)
Mario.left(72)
Mario.forward(100)
Mario.left(72)
Mario.forward(100)
Mario.right(180)
turtle.exitonclick()                    # Close the window when we click on it