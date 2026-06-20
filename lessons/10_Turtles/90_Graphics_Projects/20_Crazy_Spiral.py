"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_Flaming_Ninja_Star.py, but use what you've learned about loops
"""

import random
import turtle


def getNextColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def make_a_shape(t):
    """Make a shape with turtle t using a short pattern."""
    t.pencolor(getNextColor())
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(75)
    t.left(90)
    t.forward(35)


window = turtle.Screen()
window.bgcolor("black")

s = turtle.Turtle()
s.shape("turtle")
s.speed(0)
s.width(2)

for i in range(120):
    make_a_shape(s)
    s.forward(i)
    s.left(15)


turtle.done()
turtle.exitonclick()