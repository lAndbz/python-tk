head	1.1;
access;
symbols;
locks; strict;
comment	@# @;


1.1
date	2019.06.26.10.21.55;	author wy;	state Exp;
branches;
next	;


desc
@@


1.1
log
@Initial revision
@
text
@#!/usr/bin/python3

import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for _ in range(60):
	canvas.move(1, 5, 0)
	tk.update()
	time.sleep(0.05)


@
