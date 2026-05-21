"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() )

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().
"""

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import simpledialog, messagebox

    root = tk.Tk()
    root.withdraw()

    number1 = simpledialog.askfloat("First Number", "Enter the first number:")
    if number1 is None:
        messagebox.showinfo("Info", "No first number entered.")
        root.destroy()
        raise SystemExit

    number2 = simpledialog.askfloat("Second Number", "Enter the second number:")
    if number2 is None:
        messagebox.showinfo("Info", "No second number entered.")
        root.destroy()
        raise SystemExit

    operation = simpledialog.askstring(
        "Operation",
        "Enter the math operation (add, subtract, multiply, divide, +, -, *, /):"
    )
    if operation is None:
        messagebox.showinfo("Info", "No operation entered.")
        root.destroy()
        raise SystemExit

    operation = operation.strip().lower()

    if operation in ("add", "+", "plus"):
        result = number1 + number2
        messagebox.showinfo("Result", f"{number1} + {number2} = {result}")
    elif operation in ("subtract", "-", "minus"):
        result = number1 - number2
        messagebox.showinfo("Result", f"{number1} - {number2} = {result}")
    elif operation in ("multiply", "*", "times"):
        result = number1 * number2
        messagebox.showinfo("Result", f"{number1} × {number2} = {result}")
    elif operation in ("divide", "/", "over"):
        if number2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
        else:
            result = number1 / number2
            messagebox.showinfo("Result", f"{number1} / {number2} = {result}")
    else:
        messagebox.showerror(
            "Error",
            f"Unknown operation: '{operation}'. Please enter add, subtract, multiply, divide, +, -, *, or /."
        )

    root.mainloop()
