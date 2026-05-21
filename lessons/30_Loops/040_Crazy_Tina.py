"""
Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help
"""
import turtle                          # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(200000)                           # Make the turtle move as fast, but not too fast. 

sides = 12
angle = 360 / sides

for i in range(200):
    if i == 100:
        tina.width(2)
    if i == 200:
        tina.width(3)
    tina.forward(i)
    tina.right(angle + 1)

turtle.exitonclick()  