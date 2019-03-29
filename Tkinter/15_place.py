# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:14:00 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('500x300')

tk.Label(window, text='P1', font=('Arial', 20)).place(x=50, y=100, anchor='nw')
tk.Label(window, text='P1', font=('Arial', 20)).place(x=50, y=100, anchor='sw')

window.mainloop()
