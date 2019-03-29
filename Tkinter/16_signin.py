# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:17:12 2019

@author: Administrator
"""
import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()
window.title('Welcome to my website!')
window.geometry('500x300')

#图标画布
canvas = tk.Canvas(window, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='pic.gif')
image = canvas.create_image(200, 10, anchor='n', image=image_file)
canvas.pack(side='top')
#登陆界面
tk.Label(window, text='User name:', font=('Arial', 14)).place(x=10, y=170)
tk.Label(window, text='Password:', font=('Arial', 14)).place(x=10, y=210)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')#默认显示
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=175)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14),
                         show='*')
entry_usr_pwd.place(x=120, y=215)

window.mainloop()

