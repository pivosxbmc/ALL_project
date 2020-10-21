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
import datetime
import os
import HTMLTestRunner_cn
import unittest
from util.MyLogger import My_Log
from util.information_data import New_Data
class Tpa_Simple_Case(unittest.TestCase):
    '''Tpa 测试报告'''
    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True
    @classmethod
    def setUpClass(self):
        self.chrome_exe = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile'
        os.popen(self.chrome_exe)
        self.chrome_options = Options()
        self.chrome_options.add_argument('--start-maximized')
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome_driver, options = self.chrome_options)
        self.driver.get(str('https://tpatest.ikandy.cn/'))
        time.sleep(2)
        self.messges = New_Data()
        self.Tpa = Tpa_Business(self.driver)
    @classmethod
    def tearDownClass(cls):
        pass
    def test_1loging_success(self):
        '''Tpa 登录验证'''
        success = self.Tpa.tpa_login_base('yzc001','123456')
        self.assertFalse(success)
    #@unittest.skip('现在不需要')
    def test_2creat_case(self):
        '''创建一个新的案件'''
        for i in range(4,5):
            self.Tpa.tpa_creat_case_base('350622198301304575','2020-05-19 10:00:00',i,2)#,'18312341234',self.messges.get_address(),self.messges.get_text())
            time.sleep(1)
        #self.Tpa.tpa_creat_case_base('211103197505105905','2020-05-14 10:00:00',5,2)
    #@unittest.skip('现在不需要')
    def test_3lsearch_case(self):
        '''验证搜索案件功能'''
        self.Tpa.tap_worktop_base('') #20200420000008 20200729000002
        time.sleep(5)
        #test_data = self.Tpa.tap_case_ck_base() #验证是否有必填字段 点击已查勘返回必填字段数目
        #self.assertIsNone(test_data,msg='存在%s 个必填字段'%test_data)
    @unittest.skip('现在不需要')
    def test_5Insurance_case(self):
        '''定损处理任务'''
        #self.Tpa.tap_worktop_job_receive()
        self.Tpa.tap_wirktop_job_check()
    #@unittest.skip('现在不需要')
    def test_4case_detail_data(self):
        '''案件详情'''
        result_text = self.Tpa.tpa_case_detail_base('1234')
        self.assertIn('',result_text,msg='断言')
    @unittest.skip('现在不需要')
    def test_7case_detail_photo(self):
        '''照片详情界面'''
        self.Tpa.tap_case_detail_switch_tabs(1)
        text = self.Tpa.tap_case_detail_photo_base()
        print(text)
    @unittest.skip('现在不需要')
    def test_6case(self):
        '''定损任务处理'''
        self.Tpa.tap_case_dingsun_base()
    @unittest.skip('现在不需要退出')
    def test_9exit_quit_case(self):
        '''验证是否可以正常退出'''
        self.Tpa.tap_exit_base()



if __name__ == '__main__':
    unittest.main()



