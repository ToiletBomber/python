# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:09:53 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('500x300')

tk.Label(window, text='p', fg='red').pack(side='top')
tk.Label(window, text='p', fg='red').pack(side='bottom')
tk.Label(window, text='p', fg='red').pack(side='left')
tk.Label(window, text='p', fg='red').pack(side='right')

window.mainloop()
