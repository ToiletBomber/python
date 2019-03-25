# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:29:12 2019

@author: Administrator
"""

import tkinter as tk

window = tk.Tk()

window.title('My window')
window.geometry('300x200')
#密文
e1 = tk.Entry(window, show='*', font=('Arial',14))
#明文
e2 = tk.Entry(window, show=None, font=('Arial',14))
e1.pack()
e2.pack()

window.mainloop()

