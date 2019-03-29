# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:27:11 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('500x300')
tk.Label(window, text='on the window', bg='red',font=('Arial', 16)).pack()

#创建一个主frame，在主window窗口上
frame = tk.Frame(window)
frame.pack()
#创建一个frame_l，在frame窗口上
frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')

tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()

tkinter.messagebox.showinfo(title='Hi', message='你好！')

window.mainloop()