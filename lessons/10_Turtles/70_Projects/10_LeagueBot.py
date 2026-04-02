""" 
LeagueBot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bot.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 
"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=300, height=300)
screen.bgcolor('white')

t = turtle.Turtle()

from pathlib import Path

def set_turtle_image(turtle, image_name):
    
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)
    turtle.turtlesize(10, 10)

screen = turtle.Screen()
screen.setup(width=600, height=600)

t = turtle.Turtle()

set_turtle_image(t, "leaguebot_bolt.gif")

t.penup()
t.speed(3)
t.turtlesize(10, 10)

for i in range(23):
    t.goto(0,0)
    t.fillcolor('blue')
    t.begin_fill()
    for _ in range(5): 
        t.forward(100) 
        t.right(75)
    t.end_fill()

turtle.exitonclick()