#coding=utf-8
import sys
sys.path.append('D:\\jx\\fengzhuang')
from handle.register_handle import RegisterHandle
import time
class RegisterBusiness:
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)
    def user_base(self,name,password):
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.click_register_button()
        time.sleep(2)
        print(self.register_h.get_tabs_sum_data())
        self.register_h.click_tab_button()
        self.register_h.click_exit_button()  
    def register_succes(self):
        if self.register_h.get_register_text() == None:
            return True
        else:
            False

    #执行操作
    def login_email_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)   
        if self.register_h.get_user_text('email_error',"请输入有效的电子邮件地址") == None:
            #print("邮箱检验不成功")
            return True
        else:
            return False
        
    def register_function(self,email,username,password,file_name,assertCode,assertText):
        self.user_base(email,username,password,file_name)
        if self.register_h.get_user_text(assertCode,assertText) == None:
            #print("邮箱检验不成功")
            return True
        else:
            return False
    #name错误
    def login_name_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('user_name_error',"字符长度必须大于等于4，一个中文字算2个字符") == None:
            #print("用户名检验不成功")
            return True
        else:
            return False  
    #密码错误
    def login_password_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('password_error',"最少需要输入 5 个字符") == None:
            #print("密码检验不成功")
            return True
        else:
            return False

        