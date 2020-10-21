# -*- coding: utf-8 -*-
#表示模块的文档注释；任何模块代码的第一个字符串都被视为模块的文档注释
'a test module'
#__author__会把作者写进入
__author__ = 'yu zi chen'

import sys
sys.path.append('D:\\jx\\fengzhuang')
from PIL import Image
import tkinter as tk
import tkinter.messagebox
from tkinter import simpledialog
from util.emailtest import Run_Send_Mail 

class Login_TK(object):
	"""docstring for login_TK"""
	def login_TK(self):	
		text_data=[]

		# 第1步，实例化object，建立窗口window
		window = tk.Tk()
		 
		# 第2步，给窗口的可视化起名字
		window.title('Wellcome to Hongwei Website')
		 
		# 第3步，设定窗口的大小(长 * 宽)
		window.geometry('400x300')  # 这里的乘是小x
		 
		# 第4步，加载 wellcome image
		canvas = tk.Canvas(window, width=400, height=135, bg='green')
		#image_file = tk.PhotoImage(file='ins.gif')
		#image = canvas.create_image(200, 0, anchor='n', image=image_file)
		canvas.pack(side='top')
		tk.Label(window, text='Tpa系统',font=('Arial', 16)).pack()
		 
		# 第5步，用户信息
		tk.Label(window, text='账号:', font=('Arial', 14)).place(x=10, y=170)
		tk.Label(window, text='密码:', font=('Arial', 14)).place(x=10, y=210)
		# 第6步，用户登录输入框entry
		# 用户名
		var_usr_name = tk.StringVar()
		var_usr_name.set('example@python.com')
		entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
		entry_usr_name.place(x=120,y=175)
		# 用户密码
		var_usr_pwd = tk.StringVar()
		entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
		entry_usr_pwd.place(x=120,y=215)
		 
		# 第8步，定义用户登录功能
		def usr_login():
		    # 这两行代码就是获取用户输入的usr_name和usr_pwd
		    usr_name = var_usr_name.get()
		    usr_pwd = var_usr_pwd.get()
		    text_data.append(usr_name)
		    text_data.append(usr_pwd)
		    window.quit()
		# 第7步，login and sign up 按钮
		btn_login = tk.Button(window, text='点击登录并退出', command=usr_login)
		btn_login.place(x=120, y=240)
		# 第10步，主窗口循环显示
		window.mainloop()
		print(text_data)
		return text_data







		