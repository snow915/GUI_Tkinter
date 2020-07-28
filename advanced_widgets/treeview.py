from tkinter import *
from tkinter import ttk

root = Tk()
tree_view = ttk.Treeview(root)
tree_view.pack()
tree_view.insert("", "0", "item1", text="First item")
tree_view.insert("", "1", "item2", text="Second item")
tree_view.insert("", "2", "item3", text="Third item")
logo = PhotoImage(file="/home/snow/Pictures/giphy.gif").subsample(30, 30)
tree_view.insert("item2", "end", "python", text="Python", image=logo)
tree_view.insert("item3", "end", "item31", text="Hello")
tree_view.insert("item3", "end", "item32", text="World")
tree_view.insert("item3", "end", "item33", text="Friends")
tree_view.item("item3", open=True)

tree_view.config(height=5)
root.mainloop()
