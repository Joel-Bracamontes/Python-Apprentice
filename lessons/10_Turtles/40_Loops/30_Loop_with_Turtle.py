"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )
"""
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.shape('turtle')                    # Set the shape of the turtle to a turtle                        # Make the turtle move as fast, but not too fast.

tina.goto(-200,-200)
tina.begin_fill()
tina.fillcolor("red")
for i in range(10):
    tina.pencolor("red")
    tina.forward(50)
    tina.left(36)
tina.end_fill()

tina.goto(150,-200)
tina.begin_fill()
tina.fillcolor("blue")
for i in range(10):
    tina.pencolor("blue")
    tina.forward(50)
    tina.left(36)
tina.end_fill()

tina.goto(150,125)
tina.begin_fill()
tina.fillcolor("yellow")
for i in range(10):
    tina.pencolor("yellow")
    tina.forward(50)
    tina.left(36)
tina.end_fill()

tina.goto(-200,125)
tina.begin_fill()
tina.fillcolor("green")
for i in range(10):
    tina.pencolor("green")
    tina.forward(50)
    tina.left(36)
tina.end_fill()

tina.goto(0,0)
tina.begin_fill()
tina.fillcolor("black")
for i in range(10):
    tina.pencolor("black")
    tina.forward(40)
    tina.left(36)
tina.end_fill()

turtle.exitonclick()