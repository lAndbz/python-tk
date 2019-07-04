#!/usr/bin/python


import tkinter as tk
import random
import time

class Ball:
    def __init__(self, canvas, color, paddle): #初始化
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.move(self.id, self.canvas_height/2, self.canvas_width/2)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x_step = starts[0]
        self.y_step = -1
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x_step, self.y_step)

        pos = self.canvas.coords(self.id)
        if pos[1] <= 0: #y1
            self.y_step = 1
        if pos[3] > self.canvas_height: #y2
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x_step = 1
        if pos[2] > self.canvas_width:
            self.x_step = -1

        if self.hit_paddle(pos):
            self.y_step = -1
        if self.hit_bottom:
            w = tk.Message(window, text="GAME OVER!")
            w.pack()
        else:
            self.canvas.after(10, self.draw)

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] < paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] < paddle_pos[3]:
                # print("hitted!")
                return True
        # print("not hitted!")
        return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.move(self.id, 230, 350)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.x_step = 0
    def draw(self):
        self.canvas.move(self.id, self.x_step, 0)
        pos = self.canvas.coords(self.id)
        #左上角x坐标,右下角x坐标超过画布宽度,增量设置为0
        if pos[0] < 0 or pos[2] >= self.canvas_width:
            self.x_step = 0
        self.canvas.after(10, self.draw)

    def turn_left(self, event):
        self.x_step = -2        
    def turn_right(self, event):
        self.x_step = 2

window = tk.Tk()
window.title("弹球示例01")
window.resizable(width=False, height=False)
window.wm_attributes("-topmost", 1)

canvas = tk.Canvas(window, width=500, height=400, bd=0)
canvas.pack()
window.update()

paddle = Paddle(canvas, 'green')
ball = Ball(canvas, 'red', paddle)
paddle.draw()
ball.draw()

window.mainloop()






        
