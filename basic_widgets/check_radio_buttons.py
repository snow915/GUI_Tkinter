from tkinter import *
from tkinter import ttk


def main():
    root = Tk()

    # CHECK BUTTON
    check_button = ttk.Checkbutton(root, text="Enabled?")
    check_button.pack()
    enabled_message = StringVar()
    enabled_message.set("No use")
    check_button.config(variable=enabled_message, onvalue="Enabled", offvalue="Disabled")

    # RADIO BUTTON
    breakfast = StringVar()
    ttk.Radiobutton(root, text="Python", variable=breakfast, value="python").pack()
    ttk.Radiobutton(root, text="Java", variable=breakfast, value="java").pack()
    ttk.Radiobutton(root, text="Javascript", variable=breakfast, value="javascript").pack()
    ttk.Radiobutton(root, text="PHP", variable=breakfast, value="php").pack()

    # NORMAL BUTTON
    button = ttk.Button(root, text="Get message check button")
    button.pack()

    def get_message():
        print("CHECKBUTTON MESSAGE:", enabled_message.get())
        print("RADIOBUTTON MESSAGE:", breakfast.get())

    button.config(command=get_message)
    root.mainloop()


if __name__ == '__main__':
    main()
