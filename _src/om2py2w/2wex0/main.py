# -*- coding: utf-8 -*-
from Tkinter import *

def main():

    class App:
        """docstring for Diary_App"""
        def __init__(self, master):

            frame = Frame(master)
            frame.pack()
            
    
    my_diary_app = App()
    my_diary_app.master.title("Writing for Loving, Learning and Sharing")
    my_diary_app.master.maxsize(1000,400)

if __name__ == '__main__':
    main()