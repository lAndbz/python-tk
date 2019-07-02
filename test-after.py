#!/usr/bin/python3

import tkinter as tk


root = tk.Tk()

def task():
    print("hello")
    root.after(2000, task)

root.after(2000, task)
root.mainloop()


