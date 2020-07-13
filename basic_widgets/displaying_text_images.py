from tkinter import *
from tkinter import ttk


def main():

    root = Tk()
    label = ttk.Label(root, text="Hello")
    label.pack()
    label.config(text="Hello, Tkinter! It's been a while since we last met. Great to see you again!")
    label.config(wraplength=150)
    label.config(justify=CENTER)
    label.config(foreground="blue", background="yellow")
    label.config(font=("Courier", 18, "bold"))

    logo = PhotoImage(file="/home/snow/Pictures/logoOficial.png")
    label.img = logo
    label.config(image=label.img)
    label.config(compound="text")  # This will set the text instead of image
    label.config(compound="center")  # This will set the text in front of image
    label.config(compound="left")  # This will put the image to the left
    root.mainloop()


if __name__ == '__main__':
    main()
