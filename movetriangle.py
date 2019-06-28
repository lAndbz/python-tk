#!/usr/bin/python
#Program:
#	tkinter示例程序
#History:
#	2019/06/26 王郁 First release
#from tkinter import *
import tkinter as tk

#tk = Tk()
window = tk.Tk()
#canvas = Canvas(tk, width=400, height=400)
canvas = tk.Canvas(window, width=400, height=400)
window.title('这是一个测试程序')
canvas.pack()
#canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red') #填充红色

def move_triangle(event):
	if event.keysym == 'Up':
		canvas.move(1, 0, -3)
	if event.keysym == 'Down':
		canvas.move(1, 0, 3)
	if event.keysym == 'Left':
		canvas.move(1, -3, 0)
	if event.keysym == 'Right':
		canvas.move(1, 3, 0)

canvas.bind_all('<KeyPress-Up>', move_triangle)

canvas.bind_all('<KeyPress-Down>', move_triangle)

canvas.bind_all('<KeyPress-Left>', move_triangle)

canvas.bind_all('<KeyPress-Right>', move_triangle)

tk.mainloop()
