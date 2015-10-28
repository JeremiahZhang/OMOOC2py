# -*- coding: utf-8 -*-
from Tkinter import *
import sys, os, glob

master = Tk()

frame = Frame(master)
frame.master.title("Writing for Loving, Learning and Sharing")
frame.master.maxsize(500,200)  # set the size
frame.pack()

def read_diary():

    past_logs = Listbox(master, width=100, height=20)
    past_logs.pack()
    past_logs.insert(END, "Here is your past logs:--->")

    current_dir = os.getcwd() # 打印之前日志
    os.chdir(current_dir)
    
    for file in glob.glob("*.txt"):
        past_logs.insert(END, "Log_name:--->" + file)
        file_content = open(file, "r")
        past_logs.insert(END, "Log_content:---> " + file_content.read() + "\n")
        file_content.close()

past_logs_button = Button(master, text="PrintLogs", fg="blue", width=10, command=read_diary)
past_logs_button.pack(side=TOP)

quit_button = Button(master, text="Quit", fg="red", width=10, command=master.quit)
quit_button.pack(side=TOP)

mainloop()