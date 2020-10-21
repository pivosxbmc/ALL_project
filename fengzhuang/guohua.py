# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from base.find_element import Findelement
#设置启动时浏览器就最大化
options = Options()
'''
options.add_argument('--start-maximized')
options.add_argument('--incognito')

options.add_argument('--disable-infobars')
'''
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://yds-dzh-prod.ikandy.cn:60615/reportExcel/20200407/report.xlsx")

fd = Findelement(driver,'ty_common_elements')
def home_login():
	fd.get_element('login_loginName').send_keys('yzc')
	fd.get_element('login_password').send_keys('123456')
	fd.get_element('login-btn').click()

#home_login()





time.sleep(10)
driver.quit()