# -*- coding: utf-8 -*-
import Tkinter as tk

root = tk.Tk()

root.geometry("300x300")

frame1 = tk.Frame(root)
frame2 = tk.Frame(frame1)
frame1.pack()
frame2.pack()

menubar = tk.Menu(frame1)
menubar.add_command(label="bring back!", command=frame2.pack)
menubar.add_command(label="Quit", command=root.destroy)

tk.Button(frame2, text="Forget only frame2", command=frame2.pack_forget).pack()
tk.Label(frame2, text="Label on frame2").pack()

root.config(menu=menubar)

root.mainloop()