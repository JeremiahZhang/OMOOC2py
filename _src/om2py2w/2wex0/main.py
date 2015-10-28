# -*- coding: utf-8 -*-
from Tkinter import *

def main():

    class App:
        """Dear here is your diary system! Start writing!--->"""
        def __init__(self,master=None):

            frame = Frame(master)
            frame.pack()

# GUI 标题
    diary = Tk()
    diary_app = App(master=diary)

    diary_app.master.title("Writing for Loving, Learning and Sharing")
    diary_app.master.maxsize(1000,400)

    diary_app.mainloop()
    diary.destroy()

if __name__ == '__main__':
    main()