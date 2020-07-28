from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
text = Text(root, width=40, height=10)
text.pack()
text.config(wrap="word")


def get_text():
    print(text.get("1.0", "end"))


def set_image():
    image = Image.open("/home/snow/Pictures/python.jpg")
    image = ImageTk.PhotoImage(image)
    text.image_create("insert", image=image)


button = ttk.Button(root, text="Get text", command=get_text)
button.pack()

button_image = ttk.Button(root, text="Set default image", command=set_image)
button_image.pack()

text2 = Text(root, width=40, height=10)
text2.pack()
text2.config(wrap="word")


def replace_text():
    if text2.get("1.0", "end") != "":
        text.replace("1.0", "end", text2.get("1.0", "end"))
    else:
        print("Write something")


button2 = ttk.Button(root, text="Replace text", command=replace_text)
button2.pack()

root.mainloop()
