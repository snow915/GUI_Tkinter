from tkinter import *
from tkinter import ttk


class ScaleProgress:
    def __init__(self, root):
        self.progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
        self.progressbar1 = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
        self.value=DoubleVar()
        self.scale = ttk.Scale(root, orient=HORIZONTAL, length=400, variable=self.value, from_=0, to=100.0)
        self.scale.grid(row=2, column=0)

        self.set_determinate_progressbar()
        self.set_indeterminate_progressbar()

    def set_indeterminate_progressbar(self):
        progressbar_indeterminate = self.progressbar
        progressbar_indeterminate.grid(row=0, column=0)
        progressbar_indeterminate.config(mode="indeterminate")
        progressbar_indeterminate.start()

    def set_determinate_progressbar(self):
        progressbar_determinate = self.progressbar1
        progressbar_determinate.grid(row=1, column=0)
        progressbar_determinate.config(mode="determinate", maximum=100.0, value=0, variable=self.value)

def main():
    root = Tk()
    ScaleProgress(root)
    root.mainloop()


if __name__ == '__main__':
    main()
