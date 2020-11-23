#coding=utf-8
import sys
sys.path.append('D:\\jx\\fengzhuang')
from business.tpa_business import Tpa_Business
#from business.Tkinter_business
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl
import traceback
import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import pyautogui #鼠标点击
import datetime,os
import HTMLTestRunner_cn
from util.MyLogger import My_Log
from util.information_data import New_Data
import unittest
class Tpa_Simple_Case(unittest.TestCase):
    '''Tpa 测试报告'''
    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(str('https://www.baidu.com'))
        #self.driver.get(str('https://tpatest.ikandy.cn/'))
        time.sleep(2)
        self.messges = New_Data()
        self.Tpa = Tpa_Business(self.driver)
    @classmethod
    def tearDownClass(cls):
        pass
    def test_1loging_success(self):
        '''Tpa 登录验证'''
        success = self.Tpa.tpa_login_base('yzc','123456')
        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main()