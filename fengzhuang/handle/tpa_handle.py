#coding=utf-8
'下一个页面business'
import sys
sys.path.append('D:\\jx\\fengzhuang')
from util.information_data import New_Data
from page.tpa_page import Creat_Case_Page,TpaPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
a=datetime.datetime.now().strftime('%m-%d %H:%M:%S')
file_png =(str(a)+".png")
def messages():
    messges_data = New_Data()
    return messges_data
report_name = messages().get_name()
class Login(object):
    """tpa login handle"""
    def __init__(self,driver):
        self.driver = driver
        self.register_p = TpaPage(self.driver)
    #输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)
    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)
    def check_login_error(self):
        try:
            error_text = self.register_p.get_login_error_element().get_attribute("innerHTML")
            raise Exception(error_text)
        except Exception as e:
            pass
    def click_login_button_handle(self):
        self.register_p.get_button_element().click()
    #退出
    def click_exit_button_handle(self):
        self.register_p.get_exit_button_element().click()
    def click_quit_button_handle(self):
        self.register_p.get_quit_button_element().click()
class Creat_Case_Handle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_p = Creat_Case_Page(self.driver)
        self.messges = New_Data()
    def click_creat_case_button_element():
        self.register_p.get_creat_case_button_element()
    def click_creat_case_button(self):
        self.register_p.get_creat_case_button_element().click()
    def send_idcard_input_handle(self,idcard):
        self.register_p.get_idcard_input_element().clear()
        self.register_p.get_idcard_input_element().send_keys(idcard)
    def send_creat_data_input_handle(self,DataTime):
        self.register_p.get_creat_case_data_input_element().click()
        data_time_selement = self.driver.find_element_by_id('accidentDateTime')
        action = ActionChains(self.driver)
        action.click(data_time_selement)
        action.perform()
        time.sleep(2)
        data_time_selements = self.driver.find_element_by_class_name('ant-calendar-input')
        data_time_selements.click()
        data_time_selements.send_keys(DataTime)
        #self.register_p.get_creat_case_ok_button_element().click() #确定按钮直接输入日期不能点击
        self.register_p.get_idcard_input_element().click() #回到身份证的位置
        time.sleep(1)
        self.register_p.get_creat_case_check_button_elements().click()

    def click_choice_case_button_handle(self):
        time.sleep(1)
        try:
            self.register_p.get_choice_case_button_element().click()
            self.register_p.get_choice_case_ok_elements().click()          
        except Exception as e:
            print('就一个保单')
            pass

    def common_keys_handle(self,key_data,keys_data):
        for i in range(1,key_data):
            self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        for x in range(1,keys_data):
            self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    #装饰器
    def creat_case_common(self,key_data,keys_data):
        global report_name
        report_name = messages().get_name() #获取信息
        self.register_p.get_creat_case_choice_address_button()[0].click()
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.register_p.get_creat_case_choice_address_button()[1].click()
        self.common_keys_handle(key_data,keys_data)
        time.sleep(2)
        self.register_p.get_ceeat_case_reporter_element().clear()
        self.register_p.get_ceeat_case_reporter_element().send_keys(report_name)
        self.register_p.get_creat_case_phone_element().send_keys(messages().get_phone())
        self.register_p.get_creat_case_place_element().send_keys('田林路6000号')
        self.register_p.get_creat_case_detail_element().send_keys(messages().get_text())
        try:
            self.register_p.get_creat_new_case_click_element()[3].click()
        except Exception as e:
            print(e)
            self.register_p.get_creat_new_case_click_element()[2].click()


    #简易的创建案件
    def creat_new_case_handle(self,key_data,keys_data):
        Detail = (By.ID,'accidentDetail')
        '''效验事件经过'''
        WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(Detail),'没有这个')        
        for i in range(7,11):
            self.register_p.get_creat_case_choice_buttons()[i].click()
            #self.driver.switch_to.active_element.send_keys(Keys.DOWN)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.creat_case_common(key_data,keys_data)

    #输入信息;没有改动
    def creat_new_case_handles(self,iphone,place,detail):
        Detail = (By.ID,'accidentDetail')
        WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(Detail),'没有这个')
        time.sleep(2)
        for i in range(4,7):
            self.register_p.get_creat_case_choice_buttons()[i].click()
            #self.driver.switch_to.active_element.send_keys(Keys.DOWN)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.register_p.get_creat_case_choice_address_button()[0].click()
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.register_p.get_creat_case_choice_address_button()[1].click()
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(2)
        self.register_p.get_creat_case_phone_element().send_keys(iphone)
        self.register_p.get_creat_case_place_element().send_keys(place)
        self.register_p.get_creat_case_detail_element().send_keys(detail)
        try:
            self.driver.save_screenshot(file_png)
            self.register_p.get_creat_new_case_click_element().click()
        except Exception as e:
            self.driver.save_screenshot(file_png)
            raise e
    def creat_new_case_people(self):
        Detail = (By.ID,'accidentDetail')
        WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(Detail),'没有这个')
        self.register_p.get_creat_case_choice_buttons()[i].click()
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        for i in range(3,5):
            self.register_p.get_creat_case_choice_buttons()[i].click()
            self.driver.switch_to.active_element.send_keys(Keys.DOWN)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.register_p.get_creat_case_choice_address_button()[0].click()
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.register_p.get_creat_case_choice_address_button()[1].click()
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(2)
        self.register_p.get_creat_case_phone_element().send_keys(iphone)
        self.register_p.get_creat_case_place_element().send_keys(place)
        self.register_p.get_creat_case_detail_element().send_keys(detail)
        try:
            self.driver.save_screenshot(file_png)
            self.register_p.get_creat_new_case_click_element().click()
        except Exception as e:
            self.driver.save_screenshot(file_png)
            raise e
    def creat_case_gools(self):
        self.register_p.get_creat_case_choice_buttons()[i].click()
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        #出险类型二级
        self.register_p.get_creat_case_choice_buttons()[i].click()
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
    def creat_case_car(self):
        self.register_p.get_creat_case_choice_buttons()[i].click()
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        #出险类型二级
        self.register_p.get_creat_case_choice_buttons()[i].click()
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
class Gzt_Common_handle(object):
    '''工作台操作'''
    def __init__(self,driver):
        self.driver = driver
        self.Gzt_common = TpaPage(self.driver)
    #工作台tab页筛选
    def choice_gzt_page(self,pagedate=10):
        self.Gzt_common.get_tabs_button_element()[pagedate].click()
    #输入文字搜索
    def search_input_check_handle(self,data_text):
        self.Gzt_common.get_gzt_search_send_element().send_keys(data_text)
        self.Gzt_common.get_gzt_search_click_element().click()
    #查看或接收按钮  这个有些变化，参数被取消
    def check_case_details(self,pagedate=1,):
        self.Gzt_common.get_tabs_button_element()[pagedate].click()
        time.sleep(1)
        elements_number = len(self.Gzt_common.get_gzt_look_clikc_elements())
        new_element_number = int(elements_number/2)
        self.Gzt_common.get_gzt_look_clikc_elements()[new_element_number].click()
#工单详情界面
class Case_details_handle(object):
    """docstring for Case_details_handle"""
    def __init__(self,driver):
        self.driver = driver
        self.Tpa_detail = TpaPage(self.driver)
    def select_buttons_common(self,falg_sign=1):
        if falg_sign==3:
            self.driver.switch_to.active_element.send_keys(Keys.DOWN)
            #self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
            #self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        elif falg_sign==2:
            self.driver.switch_to.active_element.send_keys(Keys.DOWN)
            #self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            self.driver.switch_to.active_element.send_keys(Keys.RIGHT)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        elif falg_sign==4:
            self.driver.switch_to.active_element.send_keys(Keys.DOWN)
            self.driver.switch_to.active_element.send_keys(Keys.DOWN)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        else:
            self.driver.switch_to.active_element.send_keys(Keys.DOWN)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(2)
    #工单列表切换TAB页
    def switch_case_detail_tabs(self,i):
        self.Tpa_detail.get_case_detail_tabs()[i].click() 
    #案件详情
    #报案地区，详细地址
    def case_detail_page(self):
        time.sleep(1)
        report_city_element = self.Tpa_detail.get_report_city_select_element()  #send_keys(Keys.ENTER)
        #self.driver.execute_script("arguments[0].click();",report_city_element)
        #self.select_buttons_common(3)
        report_place_check = self.Tpa_detail.get_report_place_input_element()
        if report_place_check.get_attribute('value'):
            pass
        else:
            report_place_check.send_keys(messages().get_text())
    #索赔金额
    def case_detail_reportLossSum(self,num):
        reportLossSum_ckeck=self.Tpa_detail.get_reportLossSum_input_element()
        if reportLossSum_ckeck.get_attribute('value'):
            pass
        else:
            reportLossSum_ckeck.send_keys(num)
    #出现原因、状态、事故责任、有伤亡情况、
    def case_accident_reason_handle(self):        
        for i in range(4,7):
            self.Tpa_detail.get_accident_reason_select_element()[i].click()
            self.select_buttons_common(1)
        for i in range(8,13):
            self.Tpa_detail.get_accident_reason_select_element()[i].click()
            self.select_buttons_common(1)
        #开户银行
        if self.Tpa_detail.get_accident_reason_select_element()[7].text == '否':
            must_bank = self.Tpa_detail.get_accident_reason_select_element()[11]
        else:
            must_bank = self.Tpa_detail.get_accident_reason_select_element()[13]

        must_bank.click()
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys('中国建设银行')
        time.sleep(1)
        self.select_buttons_common(1)                
    # 违规项目、支付宝识别码、支付宝账户、例外原因、收款人姓名
    def case_detail_input_common_handles(self):
        elements1 = self.Tpa_detail.get_case_detail_senkey_element1()
        #self.driver.execute_script("arguments[0].click();",elements1)
        #self.select_buttons_common(2)
        self.Tpa_detail.get_case_detail_senkey_element2().send_keys('测试支付A')
        self.Tpa_detail.get_case_detail_senkey_element3().send_keys('测试支付B') #错误
        self.Tpa_detail.get_case_detail_senkey_element4().send_keys('测试支付C')
        #银行卡号
        self.Tpa_detail.get_case_detail_bankcard_num().send_keys('12345678901234')
        #医院地区、开户支行
        self.Tpa_detail.get_case_detail_hospital_element()[4].click()
        self.select_buttons_common(3)
        self.Tpa_detail.get_case_detail_three_level_menu()[5].click()
        self.select_buttons_common(3)
    #出现经过
    def case_detail_input_handle(self,data_text=messages().get_text()):
        detail_input_check = self.Tpa_detail.get_case_detail_input_element()
        if detail_input_check.get_attribute('value'):
            pass
        else:
            detail_input_check.send_keys(data_text)
        return detail_input_check.get_attribute('value')
    #三者信息
    def case_detail_other_handle(self):
        self.Tpa_detail.get_case_add_other_button_element().click()
        time.sleep(1)
        self.Tpa_detail.get_case_other_name_input_element().send_keys(report_name)
        self.Tpa_detail.get_case_other_input_phone().send_keys(messages().get_phone())
        self.Tpa_detail.get_case_other_input_idcard_element().send_keys(messages().get_id_card())
        for i in range(12,21):
            time.sleep(1)
            self.Tpa_detail.get_case_other_select_common_element()[i].click()
            self.select_buttons_common(0)
        self.Tpa_detail.get_case_other_car_name_element().send_keys('粤A6666')
        self.Tpa_detail.get_case_other_car_vin_element().send_keys('AFG10203040HHH')
        self.Tpa_detail.get_case_other_car_money_element().send_keys('2020')
        self.Tpa_detail.get_case_other_goods_name_element().send_keys('电子手机')
        self.Tpa_detail.get_case_other_goods_detail_element().send_keys('需要更换屏幕')
        self.Tpa_detail.get_case_other_goods_money_element().send_keys('2021')
    def case_conclusion_input_handle(self):
        '''估损金额、理赔结论'''
        self.Tpa_detail.get_case_detail_lossAssessmentAmount_input_element().send_keys('666')
        conclusion_input_check = self.Tpa_detail.get_case_conclusion_input_element()
        if conclusion_input_check.get_attribute('value'):
            pass
        else:
            conclusion_input_check.send_keys(messages().get_text())
    #保存按钮
    def case_save_button_handle(self):
        self.Tpa_detail.get_case_save_button_element().click()
    #备注按钮【需要分情况：资料收集】
    def case_comment_button_handle(self):
        self.Tpa_detail.get_case_detail_buttons_elements()[3].click()
        self.Tpa_detail.get_case_detail_message_common_elements().send_keys(messages().get_text())
        self.Tpa_detail.get_case_detail_message_common_add_elements().click()
        self.Tpa_detail.get_case_detail_message_common_leave_elements().click()
    #定损中处理底部按钮
    def case_bottom_button_handles(self):
        time.sleep(1)
        self.Tpa_detail.get_case_foot_button_elements()[2].send_keys(Keys.ENTER)
        elements_bottom1 =self.Tpa_detail.get_case_other_select_common_element()[-1]
        ActionChains(self.driver).move_to_element(elements_bottom1).perform()
        elements_bottom1.click()
        self.select_buttons_common(1)
        self.Tpa_detail.get_creat_case_check_buttons_elements()[-1].click()
        time.sleep(1) 
        elements_bottom2=self.Tpa_detail.get_case_other_select_common_element()[-2]
        ActionChains(self.driver).move_to_element(elements_bottom2).perform()
        elements_bottom2.click()
        self.select_buttons_common(1)
        self.Tpa_detail.get_creat_case_check_buttons_elements()[-2].click()
        #except Exception as e:
    #已查勘提交按钮
    def case_bottom_ck_handle(self):
        self.Tpa_detail.get_case_foot_ck_element().click()
    #必填信息展示提示
    def case_message_must_explain(self):
        messges_amount = self.Tpa_detail.get_case_message_must_explain()
        if len(messges_amount) == 0:
            print('没有必填的字段')
        else:
            print('存在%s 个必填的字段'%len(messges_amount))
            return len(messges_amount)
    #照片取证界面
    def case_detail_photo_amount(self):
        '''照片数量'''
        photo_amount = self.Tpa_detail.case_detail_tabs_photo_text().text
        regexx=re.compile(r'(\d+)')
        xdc=regexx.findall(photo_amount)
        photo_sum=int((xdc)[0])+int((xdc)[1])+int((xdc)[2])+int((xdc)[3])+int((xdc)[4])+int((xdc)[5])
        return photo_sum


    #返回工作台
    def case_detail_back_workbench_handle(self):
        time.sleep(1)
        self.Tpa_detail.get_case_detail_back_workbench_element().click()
        