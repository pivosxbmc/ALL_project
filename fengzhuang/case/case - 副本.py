#coding=utf-8
import sys
sys.path.append('D:\\jx\\fengzhuang')
from business.tpa_business import Tpa_Business
from business.Tkinter_business import Tk_messgae_alone
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
import HTMLTestRunner
import unittest
class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        
        cls.chrome_exe = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile'
        os.popen(cls.chrome_exe)
        cls.chrome_options = Options()
        cls.chrome_options.add_argument('--start-maximized')
        cls.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        cls.chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        cls.driver = webdriver.Chrome(cls.chrome_driver, chrome_options=cls.chrome_options)

        #cls.driver = webdriver.Chrome()
        cls.driver.get('https://tpatest.ikandy.cn/')
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
    def setUp(self):           
        self.Tpa = Tpa_Business(self.driver)

    def tearDown(self):
        time.sleep(2)
        #if sys.exc_info()[0]:
        print('结束')

        #print("这个是case的后置调键1")
    def test_loging_success(self):
        success = self.Tpa.tpa_login_base('testyzc','123456')
        self.assertFalse(success)
    def test_creat_case(self):
        self.Tpa.tpa_creat_case_base('130635199104240000','2020-05-01 00:00:00')

    def test_exit_quit_case(self):
        self.Tpa.tap_exit_base()

def start_chrome():
    chrome_exe = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile'
    os.popen(chrome_exe)
def dr():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    return driver
def current_url():
    a = driver.current_url
    if a=='https://tpatest.ikandy.cn/txtechnology/login':
        pass
    else:
        driver.get('https://tpatest.ikandy.cn/')
        #处理网页弹框
        time.sleep(3)
        #driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button').click()



if __name__ == '__main__':
    #start_chrome()
    driver = dr()
    #current_url()
    login = Tpa_Business(driver)
    #login.tpa_login_base('testyzc','123456')
    #login.tpa_creat_case_base('130635199104240000','2020-05-01 00:00:00','18312341234','田林路200号','前车受损请赔付')
    driver.find_element_by_id('accidentPlace').send_keys('1111')
