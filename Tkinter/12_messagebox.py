# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:48:54 2019

@author: Administrator
"""

import tkinter as tk
import tkinter.messagebox

window = tk.Tk()

window.title('My window')
window.geometry('500x300')

def hit_me():
    #tk.messagebox.showinfo(title='Hi', message='你好')
    #tk.messagebox.showwarning(title='Hi', message='警告')
    #tk.messagebox.showerror(title='Hi', message='错误')
    #print(tk.messagebox.askquestion(title='Hi', message='你好'))
    #print(tk.messagebox.askretrycancel(title='Hi', message='你好'))
    #print(tk.messagebox.askyesno(title='Hi', message='你好'))
    #print(tk.messagebox.askyesnocancel(title='Hi', message='你好'))
    print(tk.messagebox.askokcancel(title='Hi', message='你好'))
tk.Button(window, text= 'hit me', bg='green', font=('Arial', 14), command=hit_me).pack()

window.mainloop()

