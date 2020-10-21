#coding=utf-8
import sys
sys.path.append('D:\\jx\\fengzhuang')
from handle.tpa_handle import Login,Creat_Case_Handle,Case_details_handle,Gzt_Common_handle
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from util.emailtest import Run_Send_Mail

class Tpa_Business(object):
    """docstring for tpa_business"""
    def __init__(self,driver):
        self.driver = driver
        self.Tpa_login = Login(driver)
        self.Tpa_Creat_Case = Creat_Case_Handle(driver)
        self.Tpa_case_detail = Case_details_handle(driver)
        self.Tpa_worktop = Gzt_Common_handle(driver)
    def tpa_login_base(self,username,password):
        self.Tpa_login.send_user_name(username)
        self.Tpa_login.send_user_password(password)
        self.Tpa_login.click_login_button_handle()
        #report_table_button = (By.CLASS_NAME,'login-alert')
        #WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(report_table_button),'business没有这个元素')
        time.sleep(2)
        self.Tpa_login.check_login_error()     
    def tpa_creat_case_base(self,idcard,DataTime,key_data=2,keys_data=2):  #,iphone,place,detail):
        report_table_button = (By.CLASS_NAME,'report-list-head-create-report-button')
        WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(report_table_button),'business没有这个')
        self.Tpa_Creat_Case.click_creat_case_button()
        self.Tpa_Creat_Case.send_idcard_input_handle(idcard)
        self.Tpa_Creat_Case.send_creat_data_input_handle(DataTime)
        self.Tpa_Creat_Case.click_choice_case_button_handle()
        self.Tpa_Creat_Case.creat_new_case_handle(key_data,keys_data)
        #self.Tpa_Creat_Case.creat_new_case_handle(iphone,place,detail)
    #TPA 工作台
    def tap_worktop_base(self,data_text=''):
        '''搜索、查看'''
        self.Tpa_worktop.search_input_check_handle(data_text)
        time.sleep(1)
        self.Tpa_worktop.check_case_details()
    #领取待定损任务
    def tap_worktop_job_receive(self):
        self.Tpa_worktop.choice_gzt_page(3)
        time.sleep(1)
        self.Tpa_worktop.check_case_details(2)
    def tap_wirktop_job_check(self):
        self.Tpa_worktop.choice_gzt_page(4)
        time.sleep(1)
        self.Tpa_worktop.check_case_details(1)
    #tpa详情界面内容
    def tpa_case_detail_base(self,num):
        self.Tpa_case_detail.case_detail_page()
        self.Tpa_case_detail.case_detail_reportLossSum(num)
        self.Tpa_case_detail.case_accident_reason_handle()
        detail_data_text = self.Tpa_case_detail.case_detail_input_handle()
        self.Tpa_case_detail.case_detail_input_common_handles() #违规项目、支付宝识别码、支付宝账户、例外原因、收款人姓名
        self.Tpa_case_detail.case_conclusion_input_handle()
        #self.Tpa_case_detail.case_detail_other_handle() #三者
        self.Tpa_case_detail.case_save_button_handle()
        #self.Tpa_case_detail.case_comment_button_handle() #备注按钮
        self.Tpa_case_detail.case_detail_back_workbench_handle() #退出
        return detail_data_text
    def tap_case_detail_photo_base(self):
        '''返回照片总数'''
        photo_amount = self.Tpa_case_detail.case_detail_photo_amount()
        return photo_amount
    def tap_case_detail_switch_tabs(self,i=0):
        '''切换工单列表的tab'''
        self.Tpa_case_detail.switch_case_detail_tabs(i)
    #定损处理
    def tap_case_dingsun_base(self):
        self.Tpa_case_detail.case_bottom_button_handles()
    #已查勘
    def tap_case_ck_base(self):
        '''返回必填字段数据'''
        #self.Tpa_case_detail.case_bottom_ck_handle()
        time.sleep(1)
        self.Tpa_case_detail.case_save_button_handle()
        text_data = self.Tpa_case_detail.case_message_must_explain() #必填字段
        return text_data

    #退出系统
    def tap_exit_base(self):
        self.Tpa_login.click_exit_button_handle()
        self.Tpa_login.click_quit_button_handle()

class Dzh_Ax_Business(object):
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

# 工作台详情界面
class Tpa_Case_Detail(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        self.arg = arg
