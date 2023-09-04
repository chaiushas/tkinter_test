import tkinter as tk
from tkinter import ttk


# window
window = tk.Tk()
window.title("Buttons")
window.geometry("400x250")


# button
def button_function():
    print('pressed')
    print(radio_var.get())


button_str = tk.StringVar(value = "Custom")
button = ttk.Button(window, text = "Button", command = button_function, textvariable = button_str)
button.pack()

# check button
check_var = tk.BooleanVar(value = False)
check = ttk.Checkbutton(window, text = "checkbox1", command = lambda: print(check_var.get()), variable = check_var) # onvalue=5, offvalue=10
check.pack()

check2 = ttk.Checkbutton(window, text = "Check 2", command = lambda: print("test"))
check2.pack()


# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text = "Radio button 1",
                         value = "radio 1",
                         variable = radio_var,
                         command = lambda: print(radio_var.get()))

radio2 = ttk.Radiobutton(window, text = "Radio button 2", value = 2, variable = radio_var)

radio1.pack()
radio2.pack()


# exercise
def radio_com():
    print(check_var2.get())
    check_var2.set(False)


radio_var2 = tk.StringVar()
check_var2 = tk.BooleanVar(value = False)

exe_check = ttk.Checkbutton(window, text = "Check", command = lambda: print(radio_var2.get()), variable=check_var2)

exe_radio1 = ttk.Radiobutton(window, text = "Radio1", value = 'A', variable = radio_var2, command = radio_com)

exe_radio2 = ttk.Radiobutton(window, text = "Radio2", value = 'B', variable = radio_var2, command= radio_com)


exe_check.pack()
exe_radio1.pack()
exe_radio2.pack()


# run
window.mainloop()