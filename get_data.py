import tkinter as tk
from tkinter import ttk

def get_entry():
    entry_text = entry.get()
    # update label
    # label.config(text = "some other text")
    label["text"] = entry_text
    entry["state"] = "disabled"

def change_text():
    label["text"] = "some text"
    entry["state"] = "enabled"

# window
window = tk.Tk()
window.title("Getting and setting widgets")
window.geometry("500x250")

# widgets
label = ttk.Label(master=window, text="Some text")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="Button", command=get_entry)
button.pack()

another_button = ttk.Button(master=window, text="Anoter Button", command=change_text)
another_button.pack()

# run
window.mainloop()