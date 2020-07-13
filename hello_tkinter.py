from tkinter import *
from tkinter import ttk


class Hello:

    def __init__(self, root):

        self.label = ttk.Label(root, text="Hello Tkinter!")
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(root, text="Spanish", command=self.spanish_hello).grid(row=1, column=0)
        ttk.Button(root, text="German", command=self.german_hello).grid(row=1, column=1)

    def spanish_hello(self):
        self.label.config(text="Hola Tkinter!")

    def german_hello(self):
        self.label.config(text="Hallo Tkinter!")


def main():

    root = Tk()
    app = Hello(root)
    root.mainloop()


if __name__ == "__main__": main()
