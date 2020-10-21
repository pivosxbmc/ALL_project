# -*- coding: utf-8 -*-
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
import sys
from selenium.webdriver.common.keys import Keys
sys.path.append('D:\\jx\\fengzhuang')
import os
from base.find_element import FindElement
#启动Chrome;运行cmd的命令
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
	driver.get('https://tpatest.ikandy.cn/')
	#处理网页弹框
	#driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button').click()


def login():
	login_elements=fd.get_element('login-input')
	login_elements[0].send_keys('yzc')
	login_elements[1].send_keys('123456')
	fd.get_element('login_button').click()
def tap_gzt():
	time.sleep(2)
	data = fd.get_element('tap_sum')
#	data = dr().find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/span/span/button')
	print(data.text)

def fapiao():
	driver.get('https://tpainvce-test.ikandy.cn/')
	
	fd  = Findelement(dr(),'tap_fapiao')
#tab详情界面
def test_tpa_details():
	time.sleep(2)

	ddd=driver.find_element_by_id('reportProvinceAndCity')
	#ddd.send_keys(Keys.DOWN)
	#driver.find_elements_by_class_name('ant-cascader-picker-label')[0].click()
	#driver.execute_script("arguments[0].click();", testddd)

	#fd.get_element('report_city').send_keys(Keys.ENTER)
	driver.switch_to.active_element.send_keys(Keys.DOWN)
	#driver.switch_to.active_element.send_keys(Keys.ENTER)
	driver.switch_to.active_element.send_keys(Keys.RIGHT)
	#driver.switch_to.active_element.send_keys(Keys.ENTER)
	driver.switch_to.active_element.send_keys(Keys.RIGHT)
	driver.switch_to.active_element.send_keys(Keys.ENTER)
	time.sleep(1)

	data_text = driver.find_element_by_id('place')
	print(data_text.get_attribute('value'))
	if data_text.get_attribute('value'):
		print('有值')
	else:
		data_text.send_keys('附近')

	driver.find_elements_by_class_name('ant-select-selection__rendered')[2].click()
	driver.switch_to.active_element.send_keys(Keys.ENTER)

	driver.find_elements_by_class_name('ant-select-selection__rendered')[3].click()
	driver.switch_to.active_element.send_keys(Keys.ENTER)

	driver.find_element_by_id('accidentDetail').send_keys('文章测试')





if __name__ == '__main__':
	start_chrome()
	driver=dr()
	fd = FindElement(dr(),'tpa_elements')
	current_url()
	login()
	#tap_gzt()
	time.sleep(15)
	test_tpa_details()

	#driver.close()

