# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:17:12 2019

@author: Administrator
"""
import tkinter as tk
import tkinter.messagebox
import pickle
#1
window = tk.Tk()
window.title('Welcome to my website!')
window.geometry('500x300')

#2图标画布
canvas = tk.Canvas(window, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='pic.gif')
image = canvas.create_image(200, 10, anchor='n', image=image_file)
canvas.pack(side='top')
#3登陆界面
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
#8user_login usr_sign_up
def usr_login():
    usr_name = var_usr_name.get()#获取账户名和密码
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usr_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usr_info = {'admin':'admin'}
            pickle.dump(usr_info, usr_file)
            usr_file.close()
    if usr_name in usr_info:
        if usr_pwd == usr_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome',
                                   message='How are you? ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error, you password is wrong, try agin!')
    else:
        is_sign_up = tk.messagebox.askyesno(message='Welcome! you have not sign up yet!')
        if is_sign_up :
            usr_sign_up()
            
def usr_sign_up():
    def sign_up_to():#10逻辑注册函数
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_comfirm.get()
        
        with open ('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)#打开记录数据的文件，将注册信息读出
            if np != npf:
                tk.messagebox.showerror(message='Password is wrong!')
            
            elif nn in exist_usr_info:
                tk.messagebox.showerror(message='User already sign up!')
                
            else:
                exist_usr_info[nn] = np
                with open ('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo(message='Successfully sign up')
                window_sign_up.destroy()
    #9注册框
    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('Sign up window')
    window_sign_up.geometry('300x200')
    
    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=130, y=10)
    
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='User password: ').place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd,
                             show = '*')
    entry_new_pwd.place(x=130, y=50)
    
    new_comfirm = tk.StringVar()
    tk.Label(window_sign_up, text='Password comfirm: ').place(x=10, y=90)
    entry_new_comfirm = tk.Entry(window_sign_up, textvariable=new_comfirm,
                             show = '*')
    entry_new_comfirm.place(x=130, y=90)
    
    new_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', 
                                    command=sign_up_to)
    new_comfirm_sign_up.place(x=180, y=120)
#4登录按钮
bt_login = tk.Button(window, text='Login', command= usr_login)
bt_login.place(x=120, y=240)
bt_sign_up = tk.Button(window, text='Sign up', command= usr_sign_up)
bt_sign_up.place(x=200, y=240)



window.mainloop()

