"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.
"""

if __name__ == "__main__":
    # Import the required modules
    import tkinter as tk
    from tkinter import simpledialog, messagebox

    # Create a window object
    root = tk.Tk()

    # Hide the window, hint: use the withdraw method
    root.withdraw()

    # Ask the user for the first number
    num1 = simpledialog.askinteger("First Number", "Enter the first number:")

    # Ask the user for the second number
    num2 = simpledialog.askinteger("Second Number", "Enter the second number:")

    # Display the sum of the two numbers
    total = num1 + num2
    messagebox.showinfo("Sum", f"The sum of {num1} and {num2} is {total}.")

    # Keep the window open
    root.mainloop()
