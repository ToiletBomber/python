# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:33:05 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('500x300')

#在图形界面上创建一个标签label用以显示并放置
var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

#选项触发函数
def print_selection():
    l.config(text='您选择了' + var.get())
    
#创建radiobutton选型,其中variable=var, value ='A'意思是
#当鼠标选中了其中一项，把value的值A放到变量var中，然后赋值
#给variable
r1 = tk.Radiobutton(window, text='Option A', variable=var, 
                    value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, 
                    value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, 
                    value='C', command=print_selection)
r3.pack()


window.mainloop()