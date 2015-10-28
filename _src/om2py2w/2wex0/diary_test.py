# -*- coding: utf-8 -*-
from Tkinter import *
import sys, os, glob

def write_diary():
    # 输入文字部分 
    diary_name_content = StringVar()
    Label(master, text="Diary Name->").pack(side=TOP)
    diary_name_content_entry = Entry(master, textvariable=diary_name_content)
    diary_name_content_entry.pack()

    diary_content = StringVar()
    Label(master, text="Write Words->").pack(side=TOP)
    diary_content_text = Text(master)
    diary_content_text.pack()

    diary_name = diary_name_content.get() + ".txt"
    diary_writer = open(diary_name, "w")

    diary_writer.write(diary_content.get())
    diary_writer.close()

def read_diary():
    # 打印先前的日志 使用 Text widget
    scrollbar = Scrollbar(master, orient=VERTICAL)
    past_logs = Text(master, width=100, height=20, 
        yscrollcommand=scrollbar.set)
    scrollbar.config(command=past_logs.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    past_logs.pack()
    past_logs.insert(END, "Here is your past logs:--->" + "\n")

    current_dir = os.getcwd() # 打印之前日志
    os.chdir(current_dir)
    
    for file in glob.glob("*.txt"):
        past_logs.insert(END, "Log_name:--->" + file + "\n")
        file_content = open(file, "r")
        past_logs.insert(END, "Log_content:---> " + file_content.read() + "\n \n")
        file_content.close()

def cancel():
    master.quit()

def readme():
    pass

master = Tk()

master.geometry("1000x400")

frame1 = Frame(master)
frame1.master.title("Writing for Loving, Learning and Sharing")
# frame.master.maxsize(1000,400)  # set the size
frame1.pack()

statement = Label(frame1, text="Dear Friend! Welcome!")
statement.pack(side=TOP, fill=X)

"""quit_button = Button(master, text="Quit", fg="red", width=10, command=master.quit)
quit_button.pack()

past_logs_button = Button(master, text="PrintLogs", fg="blue", width=10, command=read_diary)
past_logs_button.pack()

write_button = Button(master, text="Write", width=10, command=write_diary)
write_button.pack()"""

mainloop()

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