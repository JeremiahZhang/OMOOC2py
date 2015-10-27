# -*- coding: utf-8 -*-
from Tkinter import *

master = Tk()

e = Entry(master)
e.pack()

# e.focus_set()

def callback():
    print e.get()

b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()

"""
your_words = StringVar()
your_diary_text = Entry(master, textvariable=your_words)
your_diary_text.pack()

your_words.set("Welcome! Please write!")
s = your_words.get()

mainloop()
"""


e = Entry(master, width=50)
e.pack()

text = e.get()