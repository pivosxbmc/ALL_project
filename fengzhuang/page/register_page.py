#coding=utf-8
'下一个页面handle'
import sys
sys.path.append('D:\\jx\\fengzhuang')
from base.find_element import FindElement
import time
class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver,'tpa_common_element')
    #获取用户名元素
    def get_username_element(self):
        return self.fd.get_element("login_input")[0]
    #获取密码元素
    def get_password_element(self):
        return self.fd.get_element("login_input")[1]
    #获取登录按钮元素
    def get_button_element(self):
        return self.fd.get_element("login_button")
    #工作台tab页所有元素
    def get_tabs_data_element(self):
        return self.fd.get_element('tabs_sum_data')
    #工作台tab页所有状态标签 
    def get_tabs_button_element(self):
        return self.fd.get_element('tabs_sum_button')

    #退出按钮    
    def get_exit_button_element(self):
        return self.fd.get_element('exit_button')



class Dzh_login_Page(object):
    def __init__(self,driver):
        self.fd = FindElement(driver,'ax_elements')
    #创建验标任务
    def get_login_username_elements(self):
        return self.fd.get_element('login-input')[0]
    #输入验标信息
    def get_login_password_elements(self):
        return self.fd.get_element('login-input')[1]

class Dzh_AX_Page(object):
    def __init__(self,driver):
        self.fd = FindElement(driver,'ax_elements')
    #创建验标任务
    def get_creat_standard_elements(self):
        return self.fd.get_element('creat_standard_button')
    time.sleep(2)
    #输入验标信息
    def get_input_standard_reportId(self):
        return self.fd.get_element('creat_standard_buttons')[0]
    def get_input_standard_carNumber(self):
        return self.fd.get_element('creat_standard_buttons')[1]
    def get_input_standard_cellPhone(self):
        return self.fd.get_element('creat_standard_buttons')[4]
    def get_standard_save_element(self):
        return self.fd.get_element('save_standard_button')

        

