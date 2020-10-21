#coding=utf-8
import sys
sys.path.append('D:\\jx\\fengzhuang')
from handle.register_handle import Dzh_AX_Handle,Dzh_AX_login_Handl
from handle.Dzh_handle import Dzh_Multi_Handle

#Dzh_AX_Handle
import time
class Dzh_Multi_Business(self,driver):
    def __init__(self,driver):
        self.multi_business = Dzh_Multi_Handle(driver)
    def function():
        pass
class Dzh_Ax_Business:
    def __init__(self,driver):
        self.register_h_login = Dzh_AX_login_Handle(driver)
        self.register_h = Dzh_AX_Handle(driver)
    def dzh_login_base(self,username,password):
        self.register_h_login.send_standard_reportId(username)
        self.register_h_login.send_standard_carNumber(password)

    def creat_standard_base(self,reportId,carNumber,cellPhone):
        self.register_h.click_standard_button()
        time.sleep(2)
        self.register_h.send_standard_reportId(reportId)
        self.register_h.send_standard_carNumber(carNumber)
        self.register_h.send_standard_cellPhone(cellPhone)
        self.register_h.click_standard_save_element()

    
    def register_succes(self):
        if self.register_h.get_register_text() == None:
            return True
        else:
            False
        
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
