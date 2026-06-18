"""
FizzBuzz Grid

We're going to use a Windowing library, guizero, to create a 10x10 grid of
numbers, with each number in a separate cell, but we're also going to set the
color of the number based on the following rules:

* If the number is evenly divisible by 5, print '🦡'
* If the number is evenly divisible by 3, print '🍄'
* If the number is evenly divisible by 15, print '🐍'
* If it is divisible by neither, print the number.

Additionally, If you are displaying a number  color the numbers as follows:

* If the sum of the digits of the number is even, color the number blue
* If the sum of the digits of the number is odd, color the number red

Here is how you can display a number in your grid. Call this function in your loop
to display the number in the grid cell at the row and column you specify.

    Text(app, text=str(number), grid=[col, row], color=color)

Or to display a badger: 
    
    Text(app, text='🦡', grid=[col, row], color=color)

HINT: You can use % and // to get the first and last digit of a number, 
or you can convert the number to a string and iterate over the digits
"""

from guizero import App, Text

app = App("Numbers Grid", layout="grid")

for row in range(10):
    for col in range(10):
        number = row * 10 + col + 1

        if number % 15 == 0:
            display_text = "🐍"
            color = "black"
        elif number % 5 == 0:
            display_text = "🦡"
            color = "black"
        elif number % 3 == 0:
            display_text = "🍄"
            color = "black"
        else:
            display_text = str(number)
            digit_sum = sum(int(digit) for digit in display_text)
            color = "black" if digit_sum % 2 == 0 else "white"

        Text(app, text=display_text, grid=[col, row], color=color)

app.display()