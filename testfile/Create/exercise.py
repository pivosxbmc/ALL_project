#2019-12-03 15:33:59
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
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

#//*[@id="root"]/div/section/div[2]/div/section/section/div/div/main/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[3]/span
a=driver.find_element_by_xpath('//*[@id="root"]/div/section/div[2]/div/section/section/div/div/main/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[3]/span').text
a=int(a)
class ccc():
	def __call__(self,driver):		
		if a==0:
			print('数字是0')
		else:
			print('数字不是0')
WebDriverWait(driver,2,0.5).until(ccc())

