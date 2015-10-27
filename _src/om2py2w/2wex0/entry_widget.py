# -*- coding: utf-8 -*-
from Tkinter import *

master = Tk()

# user and password
"""def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(master, "User Name:", 10)
password = makeentry(master, "password:", 10, show="*")

mainloop()"""

"""e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print e.get()

b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()"""

"""
your_words = StringVar()
your_diary_text = Entry(master, textvariable=your_words)
your_diary_text.pack()

your_words.set("Welcome! Please write!")
s = your_words.get()

mainloop()
"""