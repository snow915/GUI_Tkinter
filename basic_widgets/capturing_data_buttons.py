from tkinter import *
from tkinter import ttk


def callback():
    print("Clicked!")


def main():
    root = Tk()
    button = ttk.Button(root, text="Click me")
    button.pack()
    button.config(command=callback)
    button.invoke()  # This will be execute the button
    button.state(["disabled"])
    button.state(["!disabled"])
    print("Button disabled:", button.instate(["disabled"]))

    # Put an image
    logo = PhotoImage(file="/home/snow/Pictures/logoOficial.png")
    small_logo = logo.subsample(5, 5)
    button.config(image=small_logo, compound=LEFT)
    root.mainloop()


if __name__ == '__main__':
    main()
