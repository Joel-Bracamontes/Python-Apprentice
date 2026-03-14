
"""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""

import turtle                       # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)   

tina.begin_fill()
tina.pencolor("indigo")                  # Make the turtle move as fast, but not too fast. 

def draw_shape(dist, side, t):
    for _ in range(side):
        t.forward(dist)
        t.left(360/side) 
        t.fillcolor("indigo")

draw_shape(100, 5, tina)

tina.end_fill()
    



    




turtle.exitonclick()                     # Close the window when we click on it