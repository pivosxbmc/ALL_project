#coding=utf-8
import sys
sys.path.append('D:\\jx\\fengzhuang')
from business.dzh_ax_business import Dzh_Ax_Business
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
import random

def start_chrome():
    chrome_exe = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile'
    os.popen(chrome_exe)
    time.sleep(3)



def dr():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    return driver

def current_url():
    a = driver.current_url
    if a=='https://yds-dzh-test.ikandy.cn/txtechnology/login':
        pass
    else:
        driver.get('https://yds-dzh-test.ikandy.cn')
        #处理网页弹框
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button').click()

    
def dzh_login(username,password):
    creat_standard.dzh_login_base(username,password)



def creat_standard_success():
    creat_standard.creat_standard_base('RDZA201844190000063679','沪A1234','18312341234')






if __name__ == '__main__':
    start_chrome()
    driver = dr()
    creat_standard = Dzh_Ax_Business(driver)
    current_url()
    driver.
    '''
    dzh_login('yzc-ax',123456)
    time.sleep(20)
    creat_standard_success()
    '''