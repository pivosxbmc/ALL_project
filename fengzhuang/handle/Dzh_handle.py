#coding=utf-8
'下一个页面business'
import sys
sys.path.append('D:\\jx\\fengzhuang')
from page.dzh_page import H_multi_Page


class Dzh_Multi_Handle(object):
	'''multi-mcu，H5页面操作'''
    def __init__(self,driver):
        self.driver = driver
        self.Dzh_page = H_multi_Page(self.driver)
    #点击下一步按钮
    def dzh_multi_home_button(self):
        self.Dzh_page.get_multi_H5_button_element().click()
    #弹框
    def dzh_multi_home_msgbox_button(self):
        self.Dzh_page.get_multi_home_msgbox_button_element().click()