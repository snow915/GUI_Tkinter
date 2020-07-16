from tkinter import *
from tkinter import ttk


class TabsNotebook:
    def __init__(self, root):
        self.notebook = ttk.Notebook(root)
        self.notebook.pack()

        self.notebook.add(self.get_frame1(), text="One")
        self.notebook.add(self.get_frame2(), text="Two")

        self.notebook.insert(1, self.get_frame3(), text="Middle")
        self.notebook.tab(1, state="disabled")

    def get_frame1(self):
        frame1 = ttk.Frame(self.notebook)
        ttk.Button(frame1, text="Click me").pack()
        return frame1

    def get_frame2(self):
        return ttk.Frame(self.notebook)

    def get_frame3(self):
        return ttk.Frame(self.notebook)


def main():
    root = Tk()
    app = TabsNotebook(root)
    root.mainloop()


if __name__ == '__main__':
    main()