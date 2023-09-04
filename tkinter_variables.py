import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set("button pressed")

# window
window = tk.Tk()
window.title("Tkinter Variables")
window.geometry("500x250")

# tkinter variable StringVar, IntVar, DoubleVar, BooleanVar
string_var = tk.StringVar(value="start value")
another_string = tk.StringVar(value="test")

# widgets
label = ttk.Label(master=window, text="text", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

another_label = ttk.Label(master=window, textvariable=another_string)
another_label.pack()

second_entry = ttk.Entry(master=window, textvariable=another_string)
second_entry.pack()

third_entry = ttk.Entry(master=window, textvariable=another_string)
third_entry.pack()
# run
window.mainloop()