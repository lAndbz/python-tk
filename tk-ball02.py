#!/usr/bin/python


import tkinter as tk
import random
import time

class Ball:
    def __init__(self, canvas, color): #初始化
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.move(self.id, self.canvas_height/2, self.canvas_width/2)
        # self.x = 0
        # self.y = -1
        self.x_step = 0
        self.y_step = -1
    def draw(self):
        self.canvas.move(self.id, self.x_step, self.y_step)
        # print("self.x: %d , self.y: %d" %(self.x, self.y))
        pos = self.canvas.coords(self.id)
        print("x1: %d , y1: %d , x2: %d , y2: %d" % (pos[0], pos[1], pos[2], pos[3]))
        time.sleep(0.05)
        # if pos[1] <= 0: #y1
        #     self.y = 1
        # if pos[3] > self.canvas_height: #y2
        #     self.y = -1


window = tk.Tk()
window.title("弹球示例01")
window.resizable(width=False, height=False)
window.wm_attributes("-topmost", 1)

canvas = tk.Canvas(window, width=500, height=400, bd=0)
canvas.pack()
window.update()

ball = Ball(canvas, 'red')

while True:
    ball.draw()
    window.update_idletasks()
    window.update()
    time.sleep(0.01)




        
