#coding=utf-8
'下一个页面business'
import sys
sys.path.append('D:\\jx\\fengzhuang')
from page.register_page import Dzh_AX_Page,Dzh_login_Page


class RegisterHandle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)   
    #输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)

    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)
    
    #输入验证码
    def send_user_code(self,file_name):
        get_code_text = GetCode(self.driver)
        code = get_code_text.code_online(file_name)
        self.register_p.get_code_element().send_keys(code)
    
    #获取文字信息
    def get_user_text(self,info,user_info):
        try:
            if info == 'user_email_error':
                text = self.register_p.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.register_p.get_name_error_element().text
            elif info == 'password_error':
                text = self.register_p.get_password_element().text
            else:
                text = self.register_p.get_code_element().text
        except:
            text = None     
        return text
    #点击登录按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    #获取工作台tab标签所有数据
    def get_tabs_sum_data(self):
        text = self.register_p.get_tabs_data_element().text
        return text
    #点击工作台的tab工单状态标签0~8
    def click_tab_button(self,sum=10):
        self.register_p.get_tabs_button_element()[sum].click()
    #退出
    def click_exit_button(self):
        self.register_p.get_exit_button_element().click()
class Dzh_AX_login_Handle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_p = Dzh_login_Page(self.driver)
    #输入账号和密码
    def send_standard_reportId(self,username):
        self.register_p.get_login_username_elements().send_keys(username)
    def send_standard_carNumber(self,password):
        self.register_p.get_login_password_elements().send_keys(password)    
class Dzh_AX_Handle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_p = Dzh_AX_Page(self.driver)
    #创建
    def click_standard_button(self):
        self.register_p.get_creat_standard_elements().click()
    #输入用户名
    def send_standard_reportId(self,reportId):
        self.register_p.get_input_standard_reportId().send_keys(reportId)
    def send_standard_carNumber(self,carNumber):
        self.register_p.get_input_standard_carNumber().send_keys(carNumber)
    def send_standard_cellPhone(self,cellPhone):
        self.register_p.get_input_standard_cellPhone().send_keys(cellPhone)

    def click_standard_save_element(self):
        self.register_p.get_standard_save_element().click()



        