# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:56:02 2019

@author: Administrator
"""
import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('500x300')

l = tk.Label(window, bg='green', text= '         ')
l.pack()
#创建一个菜单栏。可理解为一个容器，在窗口上方
menubar = tk.Menu(window)
#创建一个file菜单项（默认不下拉。下拉内容包括New,Open,Save,Exit）
filemenu = tk.Menu(menubar, tearoff=0)
#将定义的空菜单命名为file，
menubar.add_cascade(label='File', menu=filemenu)
#创建完菜单栏，配置让菜单栏显示出来
window.config(menu=menubar)

window.mainloop()


