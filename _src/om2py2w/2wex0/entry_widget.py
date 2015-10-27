# -*- coding: utf-8 -*-
from Tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.delete(0, END)
e.insert(0, "a default value")

mainloop()

e.focus_set()

def callback():
    print e.get()

b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()

e = Entry(master, width=50)
e.pack()

text = e.get()