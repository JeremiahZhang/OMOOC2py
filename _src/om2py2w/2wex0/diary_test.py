# -*- coding: utf-8 -*-
from Tkinter import *
import sys, os, glob

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
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
        self.scrollbar.config(command=self.text.yview)

    def printLogs(self):

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

        b = Button(top, text="OK", command=self.ok)
        b.grid(row=1)
    
    def ok(self):
        self.name = self.log_name.get() + ".txt"
        self.top.destroy()

    def save(self):

        self.dialog()
        self.wait_window(self)

        log_writer = open(self.name, "a+")

        self.content = self.text.get(1.0, END)
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
        self.destroy()

    def readme():
        pass

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

"""

"""

"""        self.scrollbar = Scrollbar(self, orient=VERTICAL) # scroll bar
        self.past_logs = Text(self, width=100, height=20, 
            yscrollcommand=self.scrollbar.set)              # past logs
        self.scrollbar.config(command=self.past_logs.yview)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.past_logs.pack()
        # buttons
        self.print_button = Button(self, text="PrintLogs", width=10, command=self.print_log)
        self.print_button.pack()

        self.write_button = Button(self, text="Write", width=10, command=self.write_log)
        self.write_button.pack()
        
        self.save_button = Button(self, text="Save", width=10, command=self.save)
        self.save_button.pack()

        self.quit_button = Button(self, text="Quit", fg="red", width=10, command=self.cancel)
        self.quit_button.pack()"""