from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    frame = ttk.Frame(root, height=100, width=200, relief=RIDGE)
    frame.pack()
    ttk.Button(frame, text="Click me").grid()
    frame.config(padding=(30, 15))
    ttk.Labelframe(root, height=100, width=200, text="My frame").pack()
    root.mainloop()


if __name__ == '__main__':
    main()
