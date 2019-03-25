#!usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:05:13 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('500x200')
#这里往下显示一个标签
var = tk.StringVar()#将label标签内容设置为字符内容，用var接收hitme传出的内容
#textvariable 就是在button显示字符的一个参数，若是普通只需要text
l = tk.Label(window, textvariable = var,
             bg = 'green',fg = 'white', font = ('Arial', 12),
             width = 30, height = 2 )
l.pack()
#这里往下显示一个按钮
on_hit = False
#类似取反操作
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('您点击了按钮！')
    else:
        on_hit = False
        var.set('')
        
b = tk.Button(window, text = '点击', font = ('Arial',12),
              width = 30, height = 2, command = hit_me)
b.pack()

window.mainloop()