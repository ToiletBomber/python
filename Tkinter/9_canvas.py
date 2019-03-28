# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:30:10 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('500x300')

canvas = tk.Canvas(window, bg='green', height=200,
                   width=500)
image_file = tk.PhotoImage(file='C:\\Users\\Administrator\\Desktop\\1372069-20180808213752551-737495553.gif')
image = canvas.create_image(200, 0, anchor='n',image=image_file)
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)
canvas.pack()

def moveit():
    canvas.move(rect, 2, 2)
    canvas.move(arc , 3, 3)

b = tk.Button(window, text='move item', command=moveit).pack()

window.mainloop()
