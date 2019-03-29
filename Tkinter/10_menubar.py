# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:56:02 2019

@author: Administrator
"""
import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('500x300')

l = tk.Label(window, bg='green',fg='white' ,text= '         ')
l.pack()
counter = 0
def do_job():
    global counter
    l.config(text='do ' + str(counter))
    counter += 1
#----------------------------------------------------------------------
#创建一个菜单栏。可理解为一个容器，在窗口上方
menubar = tk.Menu(window)
#创建一个file菜单项（默认不下拉。下拉内容包括New,Open,Save,Exit）
filemenu = tk.Menu(menubar, tearoff=0)#tearoff=0菜单不能独立
#将定义的空菜单命名为file，放到菜单栏上，就是哪个容器
menubar.add_cascade(label='File', menu=filemenu)
#在filemenu上添加菜单
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()#分割线
filemenu.add_command(label='Exit',command=window.quit)

#----------------------------------------------------------------------
editmenu = tk.Menu(menubar, tearoff=0)#二级菜单
menubar.add_cascade(label='Edit', menu=editmenu, underline=0)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', command=do_job)

#----------------------------------------------------------------------
#创建完菜单栏，配置让菜单栏显示出来
window.config(menu=menubar)

window.mainloop()


