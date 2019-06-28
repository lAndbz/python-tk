#!/usr/bin/python
#Program:
#	tkinter显示gif图片
#author:
#	WangYu 

import tkinter as tk
mainwindow=tk.Tk()
mainwindow.title('显示gif')
canvas=tk.Canvas(mainwindow, width=1000, height=800)
canvas.pack()
#myImage=tk.PhotoImage(file='./sun.gif')
myImage=tk.PhotoImage(file='./plane.gif')
myImageID=canvas.create_image(0, 0, anchor=tk.NW, image=myImage)
print('ImageID: %d' %(myImageID))

def move_image(event):
	if event.keysym == 'Up':
		canvas.move(myImageID, 0, -10)	
	if event.keysym == 'Down':
		canvas.move(myImageID, 0, 10)	
	if event.keysym == 'Left':
		canvas.move(myImageID, -10, 0)	
	if event.keysym == 'Right':
		canvas.move(myImageID, 10, 0)	
canvas.bind_all('<KeyPress-Up>', move_image)
canvas.bind_all('<KeyPress-Down>', move_image)
canvas.bind_all('<KeyPress-Left>', move_image)
canvas.bind_all('<KeyPress-Right>', move_image)

mainwindow.mainloop()

