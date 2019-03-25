#!usr/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('200x100')#长x宽
l = tk.Label(window, text = 'this is tk!',
             bg = 'green', font=('Arial', 12),
             width=15,height =2)
l.pack()
window.mainloop()