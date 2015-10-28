# -*- coding: utf-8 -*-
from Tkinter import *

master = Tk()

"""b = Button(master, text="click me!", image=pattern, compound=CENTER)
b.pack() 
you need to define the pattern"""

"""b = Button(master, text="here is your diary button test!", 
    anchor=W, justify=LEFT, padx=2)
b.pack()"""

"""f = Frame(master, height=32, width=32)
f.pack_propagate(0) # dont shrink
f.pack()

b = Button(f, text="Sure!")
b.pack(fill=BOTH, expand=1)"""

"""def callback():
    print "click!"""

"""b = Button(master, text="OK", command=callback)
b.pack()
b = Button(master, text="Help", state=DISABLED)
b.pack()"""
mainloop()