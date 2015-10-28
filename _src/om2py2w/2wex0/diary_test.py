# -*- coding: utf-8 -*-
from Tkinter import *
import sys, os, glob

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def write_log(self):

        self.past_logs.pack_forget()
        self.scrollbar.pack_forget()

        self.log_name = StringVar()
        Label(self, text="Diary Name->").pack(side=TOP)
        self.name_entry = Entry(self, textvariable=self.log_name) # here input your diary name
        self.name_entry.pack()

        Label(self, text="Write Words->").pack(side=TOP)
        self.log_content = StringVar()
        self.content_entry = Entry(self, width=100, textvariable=self.log_content)                            # input your words
        self.content_entry.pack()

        # self.content_entry.bind("<Return>", self.save)
        # self.content_entry.focus_set()

    def save(self, event):
        name = self.log_name.get() + ".txt"
        log_writer = open(name, "a+")

        log_writer.write(self.log_content.get())
        log_writer.close()

    def print_log(self):
        self.scrollbar.pack()
        self.past_logs.pack()

        self.past_logs.insert(END, "Here is your past logs:--->" + "\n")

        current_dir = os.getcwd()       # print past logs
        os.chdir(current_dir)
    
        for file in glob.glob("*.txt"):
            self.past_logs.insert(END, "Log_name:--->" + file + "\n")
            file_content = open(file, "r+")
            self.past_logs.insert(END, "Log_content:---> " + file_content.read() + "\n \n")
            file_content.close()

    def createWidgets(self):

        self.scrollbar = Scrollbar(self, orient=VERTICAL) # scroll bar
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
        self.quit_button.pack()


    def cancel(self):
        self.quit()

    def readme():
        pass

def main():

    master = Tk()
    master.title("Diary App")
    
    statement = Label(master, text="Dear Friend! Welcome!")
    statement.pack(side=TOP, fill=X)

    app = Application(master)
    app.mainloop()

if __name__ == '__main__':
    main()

"""
menu = Menu(frame1)
master.config(menu=menu)

filemenu = Menu(frame1)
menu.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="PastLogs", command=read_diary)
filemenu.add_command(label="New", command=write_diary)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=cancel)

helpmenu = Menu(frame1)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Guide", command=readme)
"""