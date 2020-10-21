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

'''
日期时间
'''
end_time=datetime.datetime.now()
end_times=end_time.strftime('%Y-%m-%d %H:%M:%S')
end_time_data = end_time.strftime('%m{m}%d{d}').format(m='月',d='号')
satrt_time=end_time-datetime.timedelta(days=8)
satrt_times=satrt_time.strftime('%Y-%m-%d %H:%M:%S')
satrt_time_datas=end_time-datetime.timedelta(days=7)
satrt_time_data=satrt_time_datas.strftime('%m{m}%d{d}').format(m='月',d='号')
time_date='-'.join([satrt_time_data,end_time_data])


def dr():
	chrome_options = Options()
	chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
	chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
	return driver

def current_url():
	a=driver.current_url
	if a=='https://multi-insrn-prod.ikandy.cn/txtechnology/login':
		print(a)
		#driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button').click()
	else:
		driver.get('https://multi-insrn-prod.ikandy.cn/')
		#处理网页弹框
		time.sleep(3)
		driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button').click()

def login():
	loging_inputs=driver.find_elements_by_class_name('form-control')
	loging_inputs[0].clear()
	loging_inputs[0].send_keys('yzc-admin')
	loging_inputs[1].clear()
	loging_inputs[1].send_keys('1')
	driver.find_element_by_class_name('ant-btn').click()
	time.sleep(2)

def week_date():
	#ant-calendar-range-picker-input
	'''
	点击开始时间
	'''
	week_date_inputs = driver.find_elements_by_class_name('ant-calendar-range-picker-input')
	time.sleep(1)
	week_date_inputs[0].click()
	time.sleep(1)
	'''
	点击，再输入时间
	'''
	week_date_inputss = driver.find_elements_by_class_name('ant-calendar-input')
	week_date_inputss[0].click()
	week_date_inputss[0].send_keys(satrt_times)
	week_date_inputss[1].click()
	week_date_inputss[1].send_keys(end_times)
	#确定按钮
	driver.find_element_by_class_name('ant-calendar-ok-btn').click()
	time.sleep(1)
def cancel_button():
	time.sleep(1)
	driver.find_element_by_class_name('ant-calendar-picker-icon').click()

def c_channel():
	driver.find_elements_by_class_name('ant-select-selection__rendered').click()


def confirm_button():
	#ant-btn ant-input-search-button ant-btn-primary ant-btn-sm
	#确定按钮
	confirm = driver.find_elements_by_class_name('ant-btn-primary')
	confirm[0].click()
	time.sleep(2)
def date_number():
	dates = driver.find_element_by_class_name('Statistics_div')
	print(dates.text)
	return dates.text

def date_number_result():
	re_pending= re.compile(r'共(\d+)条')
	number_pending = re_pending.search(date_number())
	#print('待查勘：',str(number_pending.group(1)))
	return number_pending.group(1)

def xlsx_data():
	wb = openpyxl.load_workbook('周报数据汇总.xlsx')
	sheet = wb.get_sheet_by_name('韦莱')
	number_pending_xlsx = date_number_result()
	sheet['D3'] = number_pending_xlsx
	sheet['A1'] = time_date
	wb.save('测试.xlsx')
if __name__ == '__main__':
	start_chrome()
	driver=dr()
	current_url()
	login()
	print('测试开始')
	week_date() #输入日期
	#cancel_button() #清空日期
	confirm_button() #点击搜索确定
	date_number_result() #输出日期
	xlsx_data()



