# -*- coding: utf-8 -*-
from Tkinter import *
import sys, os, glob

master = Tk()
# use list box to print the past logs
past_logs = Listbox(master, width=100, height=20)
past_logs.pack()

past_logs.insert(END, "Here is your past logs:--->")

def read_diary():
    current_dir = os.getcwd() # 打印之前日志
    os.chdir(current_dir)
    
    for file in glob.glob("*.txt"):
        past_logs.insert(END, "Log_name: "+ file)
        file_content = open(file, "r")
        past_logs.insert(END, "Log_content: " + file_content.read() + "\n")
        file_content.close()

read_diary()

mainloop()

# 调用函数 打印过去的日志 在listbox中

"""listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

mainloop()"""