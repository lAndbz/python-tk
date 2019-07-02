#!/usr/bin/python


import tkinter as tk
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.move(self.id, self.canvas_height/2, self.canvas_width/2)
    def draw(self):
        pass


window = tk.Tk()
window.title("弹球示例01")
window.resizable(width=False, height=False)
window.wm_attributes("-topmost", 1)

canvas = tk.Canvas(window, width=500, height=400, bd=0)
canvas.pack()
window.update()

ball = Ball(canvas, 'red')


while True:
    window.update_idletasks()
    window.update()
    time.sleep(0.01)


window.mainloop()


