# -*- coding: utf-8 -*-
from Tkinter import *
import sys, os, glob

master = Tk()

frame = Frame(master)
frame.master.title("Writing for Loving, Learning and Sharing")
# frame.master.maxsize(1000,400)  # set the size
frame.pack()

statement = Label(master, text="Dear Friend! Welcome!")
statement.pack(side=TOP, fill=X)

# 打印先前的日志 使用 Text widget
scrollbar = Scrollbar(master, orient=VERTICAL)
past_logs = Text(master, width=100, height=20, 
    yscrollcommand=scrollbar.set)
scrollbar.config(command=past_logs.yview)
scrollbar.pack(side=RIGHT, fill=Y)

past_logs.pack()

def write_diary():
    # 输入文字部分 使用entry
    diary_name_content = StringVar()
    Label(master, text="Diary Name->").pack(side=TOP)
    diary_name_content_entry = Entry(master, textvariable=diary_name_content)
    diary_name_content_entry.pack()

    diary_content = StringVar()
    Label(master, text="Write Words->").pack(side=TOP)
    diary_content_entry = Entry(master, textvariable=diary_content)
    diary_content_entry.pack()

    diary_name = diary_name_content.get() + ".txt"
    diary_writer = open(diary_name, "w")

    diary_writer.write(diary_content.get())
    diary_content_entry.delete(0,END)
    diary_writer.close()

def read_diary():

    past_logs.insert(END, "Here is your past logs:--->" + "\n")

    current_dir = os.getcwd() # 打印之前日志
    os.chdir(current_dir)
    
    for file in glob.glob("*.txt"):
        past_logs.insert(END, "Log_name:--->" + file + "\n")
        file_content = open(file, "r")
        past_logs.insert(END, "Log_content:---> " + file_content.read() + "\n \n")
        file_content.close()

quit_button = Button(master, text="Quit", fg="red", width=10, command=master.quit)
quit_button.pack()

past_logs_button = Button(master, text="PrintLogs", fg="blue", width=10, command=read_diary)
past_logs_button.pack()

write_button = Button(master, text="Write", width=10, command=write_diary)
write_button.pack()

mainloop()