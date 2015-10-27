# -*- coding: utf-8 -*-
from Tkinter import *

def print_contents(self, event):
     print "hi. contents of entry is now ---->", \
              self.contents.get()

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()
        # app variable
        self.contents = StringVar()
        # set is to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this var
        self.entrythingy["textvariable"] = self.contents
        # add here we get a callback when the user hits return. 
        # well have the program prtin out the values of the 
        # app variable whnen the user hits return
        self.entrythingy.bind('<Key-Return>', self.print_contents)

# 24.1.6.4. Coupling Widget Variables
# - get()
# - set()
# StringVar
# IntVar
# DoubleVar
# BooleanVar
# variable 
# textvariable