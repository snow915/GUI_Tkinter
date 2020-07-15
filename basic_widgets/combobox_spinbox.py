from tkinter import *
from tkinter import ttk


class ComboSpin:
    def __init__(self, root):
        self.months_list = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        self.months = StringVar()
        self.combobox = ""

        self.year = StringVar()
        self.spinbox = ""

        self.set_combobox(root)
        self.set_spinbox(root)
        ttk.Button(root, text="Get values", command=self.get_values).grid(row=1, column=1)

    def set_combobox(self, root):
        self.combobox = ttk.Combobox(root, textvariable=self.months)
        self.combobox.grid(row=0, column=0)
        self.combobox.config(values=self.months_list)

    def set_spinbox(self, root):
        self.spinbox = ttk.Spinbox(root, from_=1990, to=2020, textvariable=self.year)
        self.spinbox.grid(row=0, column=3)

    def get_values(self):
        print(self.year.get())
        print(self.months.get())



def main():
    root = Tk()
    ComboSpin(root)
    root.mainloop()


if __name__ == '__main__':
    main()
