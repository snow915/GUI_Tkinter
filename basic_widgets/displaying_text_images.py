from tkinter import *
from tkinter import ttk


class ImageText:
    def __init__(self, root):
        self.label = ttk.Label(root, text="This is a text", foreground="blue", font=("Inconsolata", 20, "bold"))
        self.label.grid(row=0, column=0, columnspan=2)
        self.logo = PhotoImage(file="/home/snow/Pictures/logoOficial.png")
        self.label.img = self.logo
        self.label.config(image=self.label.img)
        self.label.config(compound="center")
        self.show_buttons(root)

    def show_buttons(self, root):
        positions = {
            "left": self.set_text_left,
            "center": self.set_text_center,
            "right": self.set_text_right,
            "top": self.set_text_top,
            "bottom": self.set_text_bottom
        }

        counter = 0
        for key, function in positions.items():
            ttk.Button(root,
                       text=key.capitalize(),
                       command=function)\
                .grid(row=1, column=counter)
            counter += 1

    # What really moves is the image
    def set_text_right(self):
        self.label.config(compound="left")

    def set_text_center(self):
        self.label.config(compound="center")

    def set_text_left(self):
        self.label.config(compound="right")

    def set_text_top(self):
        self.label.config(compound="bottom")

    def set_text_bottom(self):
        self.label.config(compound="top")



def main():

    root = Tk()
    app = ImageText(root)
    root.mainloop()


if __name__ == '__main__':
    main()
