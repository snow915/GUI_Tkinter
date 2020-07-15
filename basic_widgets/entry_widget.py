from tkinter import *
from tkinter import ttk


class Login:
    def __init__(self, root):
        self.label = ttk.Label(root, text="Login")
        self.label.grid(row=0, column=0)

        self.user_input = ttk.Entry(root, width=30)
        self.user_input.grid(row=1, column=0)

        self.pass_input = ttk.Entry(root, width=30)
        self.pass_input.grid(row=2, column=0)
        self.pass_input.config(show="*")

        ttk.Button(root, text="Sign in", command=self.sign_in).grid(row=3, column=0)
        ttk.Button(root, text="Reset", command=self.reset_inputs).grid(row=3, column=1)

    def clear_inputs(self):
        self.user_input.delete(0, END)
        self.pass_input.delete(0, END)

    def set_error_message(self):
        self.clear_inputs()
        self.user_input.insert(0, "Wrong user or pass")

    def disable_inputs(self):
        self.user_input.state(["disabled"])
        self.pass_input.state(["disabled"])

    def enable_inputs(self):
        self.user_input.state(["!disabled"])
        self.pass_input.state(["!disabled"])

    def sign_in(self):
        user_value = self.user_input.get()
        pass_value = self.pass_input.get()
        if user_value and pass_value != "":
            if user_value == "snow" and pass_value == "123":
                self.clear_inputs()
                self.user_input.insert(0, "SUCCESS")
                self.disable_inputs()
            else:
                self.set_error_message()

    def reset_inputs(self):
        self.enable_inputs()
        self.clear_inputs()


def main():
    root = Tk()
    login = Login(root)
    root.mainloop()


if __name__ == '__main__':
    main()
