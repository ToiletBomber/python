# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:24:23 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('500x300')
var1 = tk.StringVar() #var1接收鼠标点击的具体内容
l = tk.Label(window, bg = 'green', 
             fg = 'yellow', font = ('Arial',12),
             width = 10, textvariable = var1)

l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)
    
b1 = tk.Button(window, text = 'print selection',
               width = 15, height = 2, 
               command=print_selection)
b1.pack()

var2 = tk.StringVar()#在图形界面创建一个标签用于显示
var2.set((1,2,3,4))
lb = tk.Listbox(window, listvariable = var2)

list_items = [11, 22, 33, 44]
for item in list_items:
    lb.insert('end', item)

lb.insert(1,'first')
lb.insert(2,'second')
  
lb.pack()
    

window.mainloop()
