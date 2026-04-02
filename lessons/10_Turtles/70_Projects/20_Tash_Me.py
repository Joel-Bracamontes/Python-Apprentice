""" 
Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustache
3) Move the moustache to the right spot on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""
import turtle as turtle
import turtle
from PIL import Image
from pathlib import Path

def resize_gif(image_path, scale=0.5):
    """Resize a GIF and save it as a new file."""
    img = Image.open(image_path)
    new_size = (int(img.width * scale), int(img.height * scale))
    img = img.resize(new_size, Image.LANCZOS)
    resized_path = str(image_path).replace(".gif", "_resized.gif")
    img.save(resized_path)
    return resized_path

def set_turtle_image(t, image_name, scale=0.5):
    """Set the turtle's shape to a resized custom image."""
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)
    resized_path = resize_gif(image_path, scale=scale)

    screen = t.getscreen()
    screen.addshape(resized_path)
    t.shape(resized_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()
set_turtle_image(t, "leaguebot_bolt.gif", scale=0.5)  # change scale here

turtle.exitonclick()