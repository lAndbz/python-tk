#!/usr/bin/python

import tkinter as tk
import random as rd
import time

class Ball:
    def __init__(self, canvas, color): #初始化
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.move(self.id, self.canvas_height/2, self.canvas_width/2)

        #增加随机方向        
        self.x = rd.randint(-5, 5)
        self.y = -3
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0: #y1
            self.y = 3
        if pos[3] > self.canvas_height: #y2
            self.y = -3
        
        if pos[0] <= 0:
            self.x = 3
        if pos[2] > self.canvas_width:
            self.x = -3
        self.canvas.after(10, self.draw)

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
        self.canvas.after(10, self.draw)

    def turn_left(self, event):
        self.x = -2
    def turn_right(self, event):
        self.x = 2
        
window = tk.Tk()
window.title("弹球示例01")
window.resizable(width=False, height=False)
window.wm_attributes("-topmost", 1)

canvas = tk.Canvas(window, width=500, height=400, bd=0)
canvas.pack()
window.update()

ball = Ball(canvas, 'red')
paddle = Paddle(canvas, 'green')

ball.draw()
paddle.draw()

window.mainloop()





        
