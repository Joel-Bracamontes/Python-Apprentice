"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

t = turtle.Turtle()                  # Create a turtle named tina

for i in range(4):                       # Repeat the following four times
    t.forward(100)                     # Move tina forward by the forward distance
    t.left(90)                         # Turn tina left by the left turn
    

# Move tina forward by the forward distance
# Turn tina left by the left turn

turtle.exitonclick()                    # Close the window when we click on it