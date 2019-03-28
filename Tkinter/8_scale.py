# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:39:48 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('500x300')

l = tk.Label(bg='green', fg='yellow', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have select ' + v)
    
s = tk.Scale(window, label='try me',
             from_=0, to=10, orient=tk.VERTICAL,
             length=400, showvalue=5, tickinterval=2,
             resolution=0.1, command=print_selection)
s.pack()

window.mainloop()
