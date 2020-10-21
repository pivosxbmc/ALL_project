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
#启动Chrome;运行cmd的命令
def start_chrome():
	chrome_exe = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile'
	os.popen(chrome_exe)
	time.sleep(3)
#start_chrome()
def dr():
	chrome_options = Options()
	chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
	chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
	return driver
driver=dr()

#a='''//*[@id="app"]/div/main/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr['''+str(10)+''']/td[5]/span/button[2]'''
aaa='''A01 正确称呼客户姓名性别，正确清晰自我介绍 通过 播 放
A02 询问预填信息是否真实或是否携带身份证银行卡 通过 播 放
A02 确认银行卡和手机号是否符合要求 通过 播 放
B01 正确询问客户职业是否为学生/军人 通过 播 放
B01 正确询问客户工作是否满一个月 通过 播 放
'''



for aba in range(1,70):
	for i in range(1,11):
		element_result='''//*[@id="app"]/div/main/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr['''+str(i)+''']/td[5]/span/button[2]'''
		result_click = driver.find_element_by_xpath(element_result).click()		
		time.sleep(1)
		bb = driver.find_element_by_class_name('ant-row')
		bbb = driver.find_element_by_class_name('ant-card-head-title').text
		if aaa in bb.text:
			print('pass')
		else:
			print(bbb)
			with open('name.txt','a+') as f:
				f.write(bbb)
		time.sleep(1)	
		quit_click = driver.find_element_by_class_name('anticon-close').click()
		time.sleep(2)
	driver.find_element_by_class_name('ant-pagination-next').click()
	print('+++++++++')
	time.sleep(2)
