# -*- coding: utf-8 -*-
from Tkinter import *
import sys, os, glob

reload(sys)
sys.setdefaultencoding('utf-8') # encoding Chinese 

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.readme_Tag    = False
        self.printLogs_Tag = False
        self.newLog_Tag = False

        self.pack()
        self.createMenus(master)

    def createScrollbar(self):
        self.scrollbar = Scrollbar(self, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

    def createText(self):
        self.text = Text(self, width=1000, height=400,
            yscrollcommand=self.scrollbar.set)
        self.text.focus_force() #  keybord 光标在Text上
        self.text.pack()
        self.text.delete(1.0, END)
        self.scrollbar.config(command=self.text.yview)

    def printLogs(self):

        self.printLogs_Tag = True

        if self.readme_Tag:
            self.text1.pack_forget()
        if self.newLog_Tag:
            self.text.pack_forget()
            self.scrollbar.pack_forget()

        self.createScrollbar()
        self.createText()

        self.text.insert(END, "Here is your past logs:--->" + "\n")

        current_dir = os.getcwd()       # print past logs
        os.chdir(current_dir)
    
        for file in glob.glob("*.txt"):
            self.text.insert(END, "Log_name:--->" + file + "\n")
            file_content = open(file, "r+")
            self.text.insert(END, "Log_content:---> " + file_content.read() + "\n \n")
            file_content.close()

    def newLog(self):

        self.newLog_Tag = True
        if self.readme_Tag:
            self.text1.pack_forget()

        if self.printLogs_Tag:
            self.text.pack_forget()
            self.scrollbar.pack_forget()

        self.createScrollbar()
        self.createText()

    def dialog(self):

        top = self.top = Toplevel()

        Label(top, text="Input your log name->").grid(row=0)
        
        self.log_name = Entry(top)
        self.log_name.focus_force()
        self.log_name.grid(row=0, column=1)
        
        self.log_name.bind("<Return>", self.ok)

    def ok(self, event):
        self.name = self.log_name.get().encode(sys.stdin.encoding) + ".txt"
        self.content = self.text.get("1.0", END)
        self.top.destroy()

    def save(self):

        self.dialog()
        self.wait_window(self)

        log_writer = open(self.name, "a+")

        log_writer.write(self.content)
        log_writer.close()

    def createMenus(self, master):

        self.menu = Menu(self)
        master.config(menu=self.menu)

        self.filemenu = Menu(self)
        self.menu.add_cascade(label="file", menu=self.filemenu)
        self.filemenu.add_command(label="PastLogs", command=self.printLogs)
        self.filemenu.add_command(label="New", command=self.newLog)
        self.filemenu.add_command(label="Save", command=self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.cancel)

        self.helpmenu = Menu(self)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="Guide", command=self.readme)

    def cancel(self):
        self.master.destroy()

    def readme(self):

        if self.newLog_Tag:
            self.text.pack_forget()
            self.scrollbar.pack_forget()

        self.readme_Tag = True

        self.text1= Text(self, height=1000, width=400)

        help ="""
        1-Please click PastLogs Menu in the filemenu to see the logs you have wrote.
        2-Then Click the New Menu in the filemenu to write your new log
        3-Please Click the Save Menu if Want to save your log which you have just worte
        4-Exit menu to exit
        5-Guide menu in the Help Menu to read the Diary Guide
        """
        self.text1.insert(END, help, "color")

        self.text1.pack()

def main():

    master = Tk()
    master.title("Diary App")
    master.geometry("1000x400")
    
    statement = Label(master, text="Dear Friend! Welcome!")
    statement.pack(side=TOP, fill=X)

    app = Application(master)
    app.mainloop()

if __name__ == '__main__':
    main()