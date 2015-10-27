# -*- coding: utf-8 -*-
from Tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

# my app
myapp = App()
# here are method calls to the window manager class

myapp.master.title("My Do-Nothing Application!")
myapp.master.maxsize(1000, 400)

# start app
myapp.mainloop()