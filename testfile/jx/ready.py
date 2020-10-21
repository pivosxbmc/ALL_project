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
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
while True:
	end_time=datetime.datetime.now()
	end_times=end_time.strftime('%Y-%m-%d %H:%M:%S')
	driver.find_element_by_xpath('//*[@id="root"]/div/section/div[2]/div[2]/section/section/div/div/main/div[2]/div/div/div[1]/div/div/div[2]/button').click()
	time.sleep(2)
	end_timess=end_time.strftime('%H%M%S')
	jxpng=end_timess+'.png'
	print(jxpng)
	try:
	    picture_url=driver.get_screenshot_as_file(jxpng)
	    print("%s：截图成功！！！" % picture_url)
	except BaseException as msg:
	    print(msg)


	aa=driver.find_element_by_xpath('//*[@id="root"]/div/section/div[2]/div/section/section/div/div/main/div[2]/div/div/div[3]/div[3]/div/div/div/div/div/div/div/div/table').text
	#print(aa)
	#aa='V370027 Jing LIULJ ready 12'
	aaa=driver.find_element_by_xpath('//*[@id="root"]/div/section/div[2]/div/section/section/div/div/main/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[3]').text
	print(end_times)
	aaa_regex=re.compile(r'\d')
	number=aaa_regex.findall(aaa)
	print(int(number[0]))
	regex=re.compile(r'\D\d+\s\D+ready\s\d')
	testnumber=regex.findall(aa)
	for x in testnumber:
		print(x)

	print(end_times)
	time.sleep(10)