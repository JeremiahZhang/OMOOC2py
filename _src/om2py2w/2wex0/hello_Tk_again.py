# -*- coding: utf-8 -*-
from Tkinter import *

class App:
    def __init__(self, master): # 构造函数 __init__ method
        # a parent widget (the master)
        # 1 frame widget
        frame = Frame(master) # local variable frame
        frame.pack() # call the pack method to make the frame visible
        
        # 2 button widget as the children of the frame widget
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            ) # command can be a methon and a function
        self.button.pack(side=LEFT)
        
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, jeremiah!"

root = Tk() #  creates a Tk root widget

app = App(root) # one instance of the App class using the root widget as its parent

root.mainloop() # start
root.destroy() # optional it explicitly destroys the main window
# when the event loop is terminated. 

"""The mainloop call enters the Tk event loop, 
in which the application will stay 
until the quit method is called 
(just click the QUIT button), 
or the window is closed."""