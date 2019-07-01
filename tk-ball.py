#!/usr/bin/python
#Program:
#   Tkinter教学示例，Ball Game弹球游戏
#author:
#   WangYu 2019/06/30


import tkinter as tk
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
    def draw(self, x, y):
        self.canvas.move(self.id, x, y)

window = tk.Tk()
window.title('Ball Game')
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)
canvas = tk.Canvas(window, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
window.update()

ball = Ball(canvas, 'red')

x_pos = 0
y_pos = 0

while True:
    y_pos -= 1
    if y_pos < -50:
        y_pos += 1
    elif y_pos > 200:
        y_pos -= 1
    ball.draw(x_pos, y_pos)
    window.update_idletasks()
    window.update()
    time.sleep(0.01)

window.mainloop()


