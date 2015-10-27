# -*- coding: utf-8 -*-
from Tkinter import *

master = Tk()

def makeentry(parent, caption, width=None, **options):
    Lable(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(master, "User Name:", 10)
password = makeentry(master, "password:", 10, show="*")

content = StringVar()
entry = Entry(master, text=caption, textvariable=content)

text = content.get()
content.set(text)

mainloop()