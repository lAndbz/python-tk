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
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
#    def draw(self, x, y):
#        self.canvas.move(self.id, x, y)
#

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0: 
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1
            
window = tk.Tk()
window.title('弹球游戏')
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)
canvas = tk.Canvas(window, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
window.update()

ball = Ball(canvas, 'red')

#x_pos = 0
#y_pos = 0

while True:
    ball.draw()
    window.update_idletasks()
    window.update()
    time.sleep(0.01)

window.mainloop()


