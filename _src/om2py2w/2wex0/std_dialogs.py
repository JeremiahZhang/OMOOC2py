# -*- coding: utf-8 -*-
from Tkinter import *

# refer to http://effbot.org/tkinterbook/tkinter-standard-dialogs.htm

"""try:
    fp = open(filename)
except:
    tkMessageBox.showwarning(
        "Open file", 
        "Cannot open this file\n(%s)" % filename
        )
        return"""

# below refer to http://effbot.org/tkinterbook/tkinter-dialog-windows.htm

class MyDialog:
    
    def __init__(self, parent):
        
        top = self.top = Toplevel(parent)
        
        Label(top, text="Value").pack()
        
        self.e = Entry(top)
        self.e.pack(padx=5)
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)
    
    def ok(self):
        
        print "value is", self.e.get()
        
        self.top.destroy()

root = Tk()
Button(root, text="Hello!").pack()
root.update()

d = MyDialog(root)

root.wait_window(d.top)