# -*- coding: utf-8 -*-
# @Author: WangYu
# @Date:   2019-07-04 10:56:42
# @Last Modified by:   lAndbz
# @Last Modified time: 2019-07-04 12:44:28
# @FileName:	       tk-ball02-new.py
# @FilePath:	       /home/wy/myPython/python-tk/tk-ball02-new.py
# @brief:		       	
# @detail:
#!/usr/bin/python


import tkinter as tk
import random
import time

class Ball:
    def __init__(self, canvas, color, paddle):    	
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
    def draw(self):
        self.canvas.move(self.id, self.x_step, self.y_step)
        # print("self.x: %d , self.y: %d" %(self.x, self.y))
        pos = self.canvas.coords(self.id)
        #debug
        # print("x1: %d , y1: %d , x2: %d , y2: %d" % (pos[0], pos[1], pos[2], pos[3]))
        #time.sleep(0.05)
        #end de
        if pos[0] <= 0:
        	self.x_step = 1
        if pos[2] >= self.canvas_width:
        	self.x_step = -1
        if pos[1] <= 0: #y1
            self.y_step = 1
        if pos[3] > self.canvas_height: #y2
            self.y_step = -1
        if self.hit_paddle(pos):
        	self.y_step = -1
        self.canvas.after(10, self.draw)

    def hit_paddle(self, pos):
    	paddle_pos = self.canvas.coords(self.paddle.id)
    	if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]: # ball_x2 >= paddle_x1 and ball_x2 <= paddle_x2
    		if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]: # ball_y2 >= paddle_y1 and ball_y2 <= paddle_y2
    			return True
    	return False

class Paddle:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
		self.canvas.move(self.id, 200, 300)
		self.canvas_width = self.canvas.winfo_width()
		self.x_step = 0

		self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
		self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
	def draw(self):
		self.canvas.move(self.id, self.x_step, 0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x_step = 0
		elif pos[2] >= self.canvas_width:
			self.x_step = 0

		self.canvas.after(10, self.draw)

	#消息绑定函数，注意接口参数！
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
ball.draw()
paddle.draw()

window.mainloop()


# while True:
#     ball.draw()
#     window.update_idletasks()
#     window.update()
#     time.sleep(0.01)




        
