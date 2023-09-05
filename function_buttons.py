import tkinter as tk
from tkinter import ttk


def button_function(entry_str):
    print('button was pressed')
    print(entry_str.get())

def outer_function(parameter):
    def inner_function():
        print('button was pressed')
        print(parameter.get())
    return inner_function


# window
window = tk.Tk()
window.title("Buttons with functions and arguments")
window.geometry("400x250")


# widgets
entry_var = tk.StringVar(value = "test")
entry = ttk.Entry(window, textvariable = entry_var)
entry.pack()


# button = ttk.Button(window, text = "Button", command = lambda: button_function(entry_var))
button = ttk.Button(window, text = "Button", command = outer_function(entry_var))
button.pack()


# run
window.mainloop()