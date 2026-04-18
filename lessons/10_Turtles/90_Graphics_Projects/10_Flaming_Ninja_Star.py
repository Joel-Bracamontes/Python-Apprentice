"""Flaming Ninja Star

This program already works; run it to see what it does. 
Then change it to make it draw a different pattern. 
"""

import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup(600,600,0,0)               # Set the size of the window
window = turtle.Screen()

baseSize = 50 # the size of the black part of the star
flameSize = 50  # the length of the flaming arms

t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0) 

for i in range(360):
    t.pencolor(getNextColor(i))

    t.fillcolor(getNextColor(i))

    t.goto(0, 0) 
   
    t.begin_fill()

    t.forward(20) 

    t.left(360/360) 

    t.forward(flameSize) 

    t.right(0) 

    t.forward(flameSize) 

    t.right(0) 

    t.forward(baseSize) 

    t.end_fill()

t.hideturtle() 

turtle.done() 