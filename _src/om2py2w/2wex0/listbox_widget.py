# -*- coding: utf-8 -*-
from Tkinter import *

master = Tk()
# use list box to print the past logs
past_logs = Listbox(master)
past_logs.pack()

past_logs.insert(END, "Here is your past logs:--->")

# 调用函数 打印过去的日志 在listbox中

"""listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

mainloop()"""