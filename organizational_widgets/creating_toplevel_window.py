from tkinter import *


def main():
    root = Tk()
    window = Toplevel(root)
    window.title("New window")
    window.iconify()
    window.geometry("640x480+50+100")  # WIDTHxHEIGHT+X+Y
    window.maxsize(640, 480)
    window.minsize(200, 200)
    window.resizable(True, True)  # True is for resize the window by the user
    root.mainloop()


if __name__ == '__main__':
    main()
