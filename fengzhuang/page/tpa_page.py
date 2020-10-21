#coding=utf-8
'下一个页面handle'
import sys
sys.path.append('D:\\jx\\fengzhuang')
from base.find_element import FindElement
import time

class Creat_Case_Page(object):
    """新疆工单"""
    def __init__(self, driver):
        self.fd = FindElement(driver,'tpa_common_element')
    #
    def get_creat_case_button_element(self):
        return self.fd.get_element('creat_case_button')[3]
    def get_idcard_input_element(self):
        return self.fd.get_element('idcard_input')
    #输入时间
    def get_creat_case_data_input_element(self):
        return self.fd.get_element('creat_case_data_input')
    def get_creat_case_ok_button_element(self):
        return self.fd.get_element('creat_case_data_OK_button')
    def get_creat_case_check_button_elements(self):
        return self.fd.get_element('creat_case_check_button')[1]
    
    def get_creat_case_check_buttons_elements(self):
        return self.fd.get_element('creat_case_check_button')

    def get_choice_case_button_element(self):
        return self.fd.get_element('choice_case_button')[0]
    def get_choice_case_ok_elements(self):
        return self.fd.get_element('choice_case_ok_button')[2]

    def get_creat_case_choice_buttons(self):
        return self.fd.get_element('creat_case_choice_buttons')
    def get_creat_case_choice_address_button(self):
        return self.fd.get_element('creat_case_choice_address_button')
    #创建案子时输入的各种信息 姓名 手机号 详细地址 出险经过
    def get_ceeat_case_reporter_element(self):
        return self.fd.get_element('creat_case_reporter_input')
    def get_creat_case_phone_element(self):
        return self.fd.get_element('creat_case_phone_input')
    def get_creat_case_place_element(self):
        return self.fd.get_element('creat_case_place_input')
    def get_creat_case_detail_element(self):
        return self.fd.get_element('creat_case_detail_input')

    def get_creat_new_case_click_element(self):
        return self.fd.get_element('creat_case_OK_button')
class TpaPage(object):
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
    def get_login_error_element(self):
        return self.fd.get_element('login_error')
    #工作台tab页所有元素
    def get_tabs_data_element(self):
        return self.fd.get_element('tabs_sum_data')
    #工作台tab页所有状态标签 
    def get_tabs_button_element(self):
        return self.fd.get_element('tabs_sum_button')
    #搜索
    def get_gzt_search_send_element(self):
        return self.fd.get_element('gzt_search_input')
    def get_gzt_search_click_element(self):
        return self.fd.get_element('gzt_search_button')
    #工作台所有案件状态
    def get_all_case_status(self):
        pass
    #查看
    def get_gzt_look_clikc_elements(self):
        return self.fd.get_element('gzt_look_button')
    #》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》详情页各种输入内容
    def get_case_detail_input_element(self):
        return self.fd.get_element('accidentDetail')
    def get_case_conclusion_input_element(self):
        return self.fd.get_element('case_conclusion_input')
    #报案地区、报案详细地址、索赔金额
    def get_report_city_select_element(self):
        return self.fd.get_element('report_city')
    def get_report_place_input_element(self):
        return self.fd.get_element('report_place')
    def get_reportLossSum_input_element(self):
        return self.fd.get_element('reportLossSum')
    #出现原因、状态多个选项
    def get_accident_reason_select_element(self):
        return self.fd.get_element('case_select_buttons')
    # 违规项目、支付宝识别码、支付宝账户、例外原因、收款人姓名
    def get_case_detail_senkey_element1(self):
        return self.fd.get_element('case_detail_wgxm')
    def get_case_detail_senkey_element2(self):
        return self.fd.get_element('alipayId')
    def get_case_detail_senkey_element3(self):
        return self.fd.get_element('alipayAccount')
    def get_case_detail_senkey_element4(self):
        return self.fd.get_element('payeename')
    #银行卡号
    def get_case_detail_bankcard_num(self):
        return self.fd.get_element('bankcard_num')
    #医院地区、开户支行
    def get_case_detail_hospital_element(self):
        return self.fd.get_element('hosptial_address')
    def get_case_detail_three_level_menu(self):
        return self.fd.get_element('three_level_menu')


    #必填信息没填时的展示提示
    def get_case_message_must_explain(self):
        return self.fd.get_element('message_must_explain')
    #出现经过,估损金额,理赔结论,保存按钮
    def get_case_detail_input_element(self):
        return self.fd.get_element('case_detail_input')
    def get_case_detail_lossAssessmentAmount_input_element(self):
        return self.fd.get_element('lossAssessmentAmount')
    def get_case_conclusion_input_element(self):
        return self.fd.get_element('case_conclusion_input')
    def get_case_save_button_element(self):
        return self.fd.get_element('case_save_button')

    #三者信息
    def get_case_add_other_button_element(self):
        return self.fd.get_element('case_detail_add_other')
    def get_case_other_name_input_element(self):
        return self.fd.get_element('case_other_name')
    def get_case_other_input_phone(self):
        return self.fd.get_element('case_other_phone')
    def get_case_other_input_idcard_element(self):
        return self.fd.get_element('case_other_idcard')
    def get_case_other_select_common_element(self): #三者筛选项14,15,16 
        return self.fd.get_element('case_other_select')
    def get_case_other_car_name_element(self):  #三者车损的信息
        return self.fd.get_element('case_other_car_number')
    def get_case_other_car_vin_element(self):
        return self.fd.get_element('case_other_car_vin')
    def get_case_other_car_money_element(self):
        return self.fd.get_element('case_other_car_money')
    def get_case_other_goods_name_element(self):  #三者物损的信息
        return self.fd.get_element('case_other_goods_name')
    def get_case_other_goods_detail_element(self):
        return self.fd.get_element('case_other_goods_damagedetail')
    def get_case_other_goods_money_element(self):
        return self.fd.get_element('case_other_goods_money')
    #工单列表的tab页
    def get_case_detail_tabs(self):
        return self.fd.get_element('details_tabs')
    #新建协作任务
    def crete_xiezuo_ant_btn_sm(self):
        return self.fd.get_element('create_xiezuo_case')[4]
    #定损中的底部按钮
    def get_case_foot_button_elements(self):
        return self.fd.get_element('case_foot_button')
    def get_creat_case_check_buttons_elements(self):
        return self.fd.get_element('creat_case_check_button')
    #已查勘按钮
    def get_case_foot_ck_element(self):
        return self.fd.get_element('case_foot_ck_button')
    #详情界面底部按钮
    def get_case_detail_buttons_elements(self):
        return self.fd.get_element('details_buttons')
    #备注内容
    def get_case_detail_message_common_elements(self):
        return self.fd.get_element('leave_message_input')        
    def get_case_detail_message_common_add_elements(self):
        return self.fd.get_element('leave_meaaage_add_input')
    def get_case_detail_message_common_leave_elements(self):
        return self.fd.get_element('details_comment_close')[1]
    #照片取证界面 照片数量
    def case_detail_tabs_photo_text(self):
        return self.fd.get_element('case_detail_tabs_photo')[1]
    #照片取证界面 公共按钮
    
    #返回工作台
    def get_case_detail_back_workbench_element(self):
        return self.fd.get_element('details_back_button')       
    #退出按钮    
    def get_exit_button_element(self):
        return self.fd.get_element('tpa_exit_buttons')[1]
    def get_quit_button_element(self):
        return self.fd.get_element('tpa_exit_buttonss')
#一些按钮触发新弹框或界面
class TpaPage_button(object):
    def __init__(self,driver):
        self.fd = FindElement(driver,'tpa_common_element')
    #资料退回
    def get_back_return_button_element(self):
        return self.fd.get_element("details_buttons")[1]
    #自定义说明
    def get_back_return_leavemsg_element(self):
        return self.fd.get_element('back_return_leavemsg')
    #确定退回、关闭按钮
    def get_back_return_confirm_element(self):
        return self.fd.get_element('leave_meaaage_add_input')
    def get_case_detail_message_common_leave_elements(self):
        return self.fd.get_element('details_comment_close')[0]



        

