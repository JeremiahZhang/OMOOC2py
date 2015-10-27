# -*- coding: utf-8 -*-
from Tkinter import *
# import every thing from Tkinter
root = Tk()
# to initialize Tkinter need to creat a TK root widget

w = Label(root, text="Hello, world!") # Label widget
w.pack()
""" # pack method

    This tells it to size itself to fit the given text,
    and make itself visible. """

root.mainloop() # start root widget