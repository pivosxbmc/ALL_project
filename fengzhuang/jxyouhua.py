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
import os
from base.find_element import Findelement

#启动Chrome;运行cmd的命令
def start_chrome():
	chrome_exe = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile'
	os.popen(chrome_exe)
	time.sleep(3)

def dr():
	chrome_options = Options()
	chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
	chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
	return driver

def message_jx(user_card):
	fd = Findelement(driver)
	driver.get('https://jx-h5-test.ikandy.cn:4002/?biType=11&groupId=2')
	time.sleep(2)
	fd.get_element('name').send_keys('圆先生')
	fd.get_element('phone_number').send_keys('18321021111')
	fd.get_element('id_card').send_keys(user_card)
	fd.get_element('store').send_keys('TXT110')
	time.sleep(1)

def login_jx():
	driver.find_element_by_class_name('txt-mobile-btn-color').click()

def screen_TX_POSL():
	skill_number = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[13]/div/div[1]/div[2]')
	skill_number.click()
	time.sleep(1)
	#driver=dr()
	#鼠标点击事件
	actions = ActionChains(driver)
	actions.click_and_hold()
	print('左键点击不松开')
	total_element = driver.find_elements_by_class_name('am-picker-col-item')
	source = total_element[8]
	target = total_element[6]
	actions = ActionChains(driver)
	actions.drag_and_drop(source, target)
	time.sleep(1)
	actions.drag_and_drop(total_element[10],total_element[7])
	a = -1
	for i in total_element:
		a = a+1
		print(str(a),i.text)
	actions.perform()
	driver.find_element_by_class_name('am-picker-popup-header-right').click()

def personal_information():
	driver=dr()
	time.sleep(2)
	aaa = driver.find_elements_by_class_name('txt-radio-buttons-normal')
	print(len(aaa))
	aaa[1].click()
	aaa[3].click()


if __name__ == '__main__':
#	start_chrome()
	driver=dr()
	message_jx('130930198405160911')
	#screen_TX_POSL()
	#登录
#	login_jx()
	time.sleep(15)
	driver.close()
'''
	driver.get('https://jx-h5-test.ikandy.cn:4002/?biType=11&groupId=2')
	a=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[3]/div/div[2]/input')
	a.click()
	time.sleep(1)
	a.send_keys('测试李')
'''