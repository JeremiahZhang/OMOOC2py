# -*- coding: utf-8 -*-
from Tkinter import *
import sys, os, glob

master = Tk()

frame = Frame(master)
frame.master.title("Writing for Loving, Learning and Sharing")
frame.master.maxsize(500,200)  # set the size
frame.pack()

diary_name_content = StringVar()
Label(master, text="Diary Name->").pack(side=TOP)
diary_name_content_entry = Entry(master, textvariable=diary_name_content)
diary_name_content_entry.pack()

diary_content = StringVar()
Label(master, text="Write Words->").pack(side=TOP)
diary_content_entry = Entry(master, textvariable=diary_content)
diary_content_entry.pack()

def write_diary():

    diary_name = diary_name_content.get() + ".txt"
    diary_writer = open(diary_name, "w")

    diary_writer.write(diary_content.get())
    diary_writer.close()

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

quit_button = Button(master, text="Quit", fg="red", width=10, command=master.quit)
quit_button.pack(side=BOTTOM)

past_logs_button = Button(master, text="PrintLogs", fg="blue", width=10, command=read_diary)
past_logs_button.pack(side=BOTTOM)

# write_button = Button(master, text="Write", width=10, command=write_diary)
# write_button.pack(side=BOTTOM)

mainloop()