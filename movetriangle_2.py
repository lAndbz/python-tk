#!/usr/bin/python
#Program:
#	tkinter教学示例程序 第二版
#author:
#	WangYu  2019/06/25
import tkinter as tk

window=tk.Tk()
window.title('这是一个示例程序')
canvas=tk.Canvas(window, width=400, height=400)
canvas.pack()
myTriangle=canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')

def move_triangle(event):
	if event.keysym == 'Up':
		canvas.move(myTriangle, 0, -5)
	if event.keysym == 'Down':
		canvas.move(myTriangle, 0, 5)
	if event.keysym == 'Left':
		canvas.move(myTriangle, -5, 0)
	if event.keysym == 'Right':
		canvas.move(myTriangle, 5, 0)

canvas.bind_all('<KeyPress-Up>', move_triangle)
canvas.bind_all('<KeyPress-Down>', move_triangle)
canvas.bind_all('<KeyPress-Left>', move_triangle)
canvas.bind_all('<KeyPress-Right>', move_triangle)
window.mainloop()
