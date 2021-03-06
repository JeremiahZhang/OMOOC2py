# -*- coding: utf-8 -*-
from Tkinter import *
import os
import tkSimpleDialog

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

class Dialog(Toplevel):
    
    def __init__(self, parent, title=None):
        
        Toplevel.__init__(self, parent)
        self.transient(parent)
        
        if title:
            self.title(title)
        
        self.parent = parent
        
        self.result = None
        
        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        
        self.buttonbox()
        
        self.grab_set() # 解决 主窗口与对话窗口的混乱
        
        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50, 
            parent.winfo_rooty()+50))
        
        self.initial_focus.focus_set()
        
        self.wait_window(self)

    # construciton hooks

    def body(self, master):
        pass
    
    def buttonbox(self):
        box = Frame(self)
        
        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)
        
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        
        box.pack()
    
    def ok(self, event=None):
        
        if not self.validate():
            self.initial_focus.focus_set()
            return
        
        self.withdraw()
        self.update_idletasks()
        
        self.apply()
        
        self.cancel()
    
    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()
    
    # command hooks
    
    def validate(self):
        return 1 # override
    
    def apply(self):
        pass # override

class MyDialog(tkSimpleDialog.Dialog):
    
    def body(self, master):
        
        Label(master, text="First:").grid(row=0)
        Label(master, text="Second:").grid(row=1)
        
        self.e1 = Entry(master)
        self.e2 = Entry(master)
        
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        
        return self.e1

    def apply(self):
        first = int(self.e1.get())
        second = int(self.e2.get())
        print first, second

root = Tk()
Button(root, text="Hello!").pack()
root.update()

d = MyDialog(root)

print d.result