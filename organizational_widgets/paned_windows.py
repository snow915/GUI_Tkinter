from tkinter import *
from tkinter import ttk

class Paned:
    def __init__(self, root):
        self.paned_window = ttk.Panedwindow(root, orient=HORIZONTAL)
        self.paned_window.pack(fill=BOTH, expand=True)

        self.paned_window.add(self.frame_1(), weight=1)
        self.paned_window.add(self.frame_2(), weight=4)
        self.paned_window.insert(1, self.frame_3_not_resizable())

    def frame_1(self):
        return ttk.Frame(self.paned_window, width=100, height=300, relief=SUNKEN)

    def frame_2(self):
        return ttk.Frame(self.paned_window, width=400, height=400, relief=SUNKEN)

    def frame_3_not_resizable(self):
        return ttk.Frame(self.paned_window, width=50, height=400, relief=SUNKEN)


def main():
    root = Tk()
    root.minsize(500, 500)
    app = Paned(root)
    root.mainloop()


if __name__ == '__main__':
    main()
