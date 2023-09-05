import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f"x: {event.x} y: {event.y}")


# window
window = tk.Tk()
window.geometry("500x500")
window.title("Event binding")

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = "Button")
button.pack()


# events
button.bind("<Alt-KeyPress-a>", lambda event: print("Event"))
window.bind("<Motion>", get_pos)
window.bind("<KeyPress>", lambda event: print("Button was pressed"))

entry.bind("<FocusIn>", lambda event: print("Entry field was selected"))
entry.bind("<FocusOut>", lambda event: print("Entry field was unselected"))


# exercise
text.bind("<Shift-MouseWheel>", lambda event: print("Mousewheel"))

# run 
window.mainloop()