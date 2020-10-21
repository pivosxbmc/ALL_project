#coding=utf-8
'下一个页面handle'
import sys
sys.path.append('D:\\jx\\fengzhuang')
from base.find_element import FindElement
import time
class H_multi_Page(object):
    """H5界面"""
    def __init__(self, driver):
        self.elements = FindElement(driver,'Multi')

    def get_multi_H5_button_element(self):
        return self.elements.get_multi_element('H_home_click')
    def get_multi_home_msgbox_button_element(self):
    	return self.elements.get_multi_element('H_home_msgbox_button')