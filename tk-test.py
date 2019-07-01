#!/usr/bin/python

import tkinter as tk
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 499, 399)


window = tk.Tk()
window.title('Test')
#window.resizable(0, 0)
canvas = tk.Canvas(window, width=500, height=400, bd=0)
canvas.pack()
window.update()

ball = Ball(canvas, 'red')

while True:
    window.update_idletasks()
    window.update()
    time.sleep(0.01)

window.mainloop()


