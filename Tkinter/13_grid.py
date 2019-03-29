# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:03:19 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('500x300')

x=0
for i in range(3):
    for j in range(3):
        tk.Label(window, text=x).grid(row=i, column=j, padx=10 , pady=10, 
                ipadx=10, ipady=10)
        x += 1

window.mainloop()
