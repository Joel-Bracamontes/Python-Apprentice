""" A simple turtle program that moves the turtle randomly in the grid 

This program will perform a "random walk" by moving the turtle randomly in the grid.

Implement the random_walk function that will move the turtle randomly in the grid.

"""
import turtle
turtle.setup(600,600,0,0)               # Set the size of the window
MJ = turtle.Turtle()
MJ.shape('turtle')                    # Set the shape of the turtle to a turtle

for i in range(1):
    MJ.left(180)
    MJ.forward(40)
    MJ.right(110)
    MJ.forward(200)
    MJ.right(75)
    MJ.forward(50)
    MJ.right(45)
    MJ.forward(90)
    MJ.right(80)
    MJ.forward(100)
    MJ.left(80)
    MJ.forward(43)
    
    turtle.exitonclick()