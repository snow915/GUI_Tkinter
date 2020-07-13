from tkinter import *
from tkinter import ttk


root = Tk()
button = ttk.Button(root, text="Click me")
button.pack()

# Change the properties after create it
button["text"] = "Press me"
button.config(text="Push me")

print(button.config())  # Print all the properties available for this object

root.mainloop()
