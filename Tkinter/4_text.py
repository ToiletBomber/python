# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:36:15 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('300x200')

e1 = tk.Entry(window, show=None)
e1.pack()
#python 执行顺序从上到下，所以函数放在按钮上面
def insert_point():
    var = e1.get()
    t.insert('insert', var)
    
def insert_end():
    var = e1.get()
    t.insert('end', var)
    
b1 = tk.Button(window, text = '光标插入', width = 10,
               height = 2, command = insert_point)
b2 = tk.Button(window, text = '结尾插入', width = 10,
               height = 2, command = insert_end)

b1.pack()
b2.pack()


t =tk.Text(window, height = 3)
t.pack()

window.mainloop()

