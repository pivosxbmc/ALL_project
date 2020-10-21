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
#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile
def start_chrome():
	chrome_exe = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile'
	os.popen(chrome_exe)
	time.sleep(3)
start_chrome()


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
a=driver.current_url
if a=='https://yds-dzh-prod.ikandy.cn/txtechnology/login':
	print(a)
else:
	driver.get('https://yds-dzh-prod.ikandy.cn')
	#处理网页弹框
	time.sleep(3)
	driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/button').click()

print(driver.title)
#登录
def sign_in(name,passwora):
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/form/div[2]/input').send_keys(name)
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/form/div[3]/input').send_keys(passwora)
	driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/form/div[4]/button').click()
	time.sleep(2)
sign_in('ymf-admin',123456)
#处理弹框alert
try:
	alert=driver.switch_to_alert()
	time.sleep(2)
	alert.accept()
except :
	errorfile=open('erroe.txt','w+')
	errorfile.write(traceback.format_exc())
	errorfile.close()
finally:
	print(time.ctime())
	print('+++++++++++++++++')

time.sleep(2)


driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/span[1]').click()
time.sleep(2)
#driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/span[1]').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/span/span/input[1]').click()
time.sleep(2)
#创建一周日期
end_time=datetime.datetime.now()
end_times=end_time.strftime('%Y-%m-%d %H:%M:%S')
satrt_time=end_time-datetime.timedelta(days=8)
satrt_times=satrt_time.strftime('%Y-%m-%d %H:%M:%S')
#点击输入日期
time.sleep(2)
#点击时间位置开启下拉框
driver.find_element_by_css_selector('.ant-calendar-input').click()
driver.find_element_by_css_selector('.ant-calendar-input').send_keys(satrt_times)
time.sleep(2)
driver.find_element_by_css_selector('.ant-calendar-date-input-wrap').click() #利用css定位
#driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
#/html/body/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/input
#/html/body/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/input
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(end_times)
#点击时间确定按钮
driver.find_element_by_css_selector('.ant-calendar-ok-btn').click()

time.sleep(2)
#点击全部渠道
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div/div').click()
time.sleep(5)
#x坐标增是向右移动，Y坐标移动是向下移动
x,y=pyautogui.position() #获取当前鼠标的位置
#pyautogui.moveRel(0,30,duration=0.5) #移动鼠标位置向下移动
time.sleep(2)
#点击B端渠道
pyautogui.click(573,268)
#点击搜索按钮
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/span/span/button').click()


time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/span').click()
#获取B端数据
number=driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]').text
print(number)
print(type(number))
#获取C端数据
#点击B端渠道
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div').click()
time.sleep(1)
pyautogui.click(590,306)
#点击搜索按钮
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/span/span/button').click()
time.sleep(3)
numberc=driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]').text
print(numberc)


#用正则把B端已定损。已接收，转下线的数据提起出来
regexd=re.compile(r'已定损(\d+)条')
regexj=re.compile(r'已接收(\d+)条')
regexx=re.compile(r'转线下(\d+)条')
xd=regexd.search(number)
xj=regexj.search(number)
xx=regexx.search(number)
sums=int(xd.group(1))+int(xj.group(1))+int(xx.group(1))
print('B端数据：'+str(sums))
#用正则把C端数据提取
egexd=re.compile(r'已定损(\d+)条')
regexj=re.compile(r'已接通(\d+)条')
regexx=re.compile(r'转线下(\d+)条')
xdc=regexd.search(numberc)
xjc=regexj.search(numberc)
xxc=regexx.search(numberc)
sumsc=int(xdc.group(1))+int(xjc.group(1))+int(xxc.group(1))
print(str(sumsc))



#用正则把数字提取出来
regex=re.compile(r'\d+')
testnumber=regex.findall(number)
#用正则表达式把数字替换提取文字
#testnumbers=re.sub(r'\d+',r'',number) #要被替换的内容：\d+，替换者：，字符串内容
#testnumberss=testnumbers.split('，')	  #把字符串转换成列表
#numbers=number.split('，') #把字符串number换成list
#写入到表格,先读表格数据
rb=openpyxl.load_workbook('周报.xlsx')
sheetname=rb.get_active_sheet()
#sheetname.title='周报'
print(sheetname)
aa=sheetname['A2':'G2']
aaa=sheetname['A3':'F3']
print(type(aa))
AA=[]
for i in aa:
	for ii in i:
		AA.append(ii.value)
print(AA)
#读取第二行数据
BB=[]
for i in aaa:
	for ii in i:
		BB.append(ii.value)

#写入表格第一
wb=openpyxl.Workbook()
sheetnamew=wb.get_active_sheet()
vv= -1
aaA=sheetnamew['A2':'G2']
for i in aaA:
	for ii in i:
		vv+=1
		ii.value=AA[vv]
print(sheetnamew['A2'].value)
#写入第二
aaB=sheetnamew['A3':'F3']
vvb= -1
for i in aaB:
	for ii in i:
		vvb+=1
		ii.value=BB[vvb]
sheetnamew['G3']=sums
sheetnamew['F3']=sumsc
time.sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/header/nav/div/span[3]/a/div/span').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/header/div/div[2]/input[1]').click()
time.sleep(2)






'''
#登录国寿
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/form/div[2]/input').send_keys('gscx-zj-admin')
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/form/div[3]/input').send_keys('123qwe')
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/form/div[4]/button').click()
time.sleep(2)
#
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[1]/ul/a[1]').click()
#开始
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/span[1]').click()
time.sleep(2)
#driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/span[1]').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/span/span/input[1]').click()
time.sleep(2)
#创建一周日期
end_time=datetime.datetime.now()
end_times=end_time.strftime('%Y-%m-%d %H:%M:%S')
satrt_time=end_time-datetime.timedelta(days=8)
satrt_times=satrt_time.strftime('%Y-%m-%d %H:%M:%S')
#点击输入日期
time.sleep(2)
#点击时间位置开启下拉框
driver.find_element_by_css_selector('.ant-calendar-input').click()
driver.find_element_by_css_selector('.ant-calendar-input').send_keys(satrt_times)
time.sleep(2)
driver.find_element_by_css_selector('.ant-calendar-date-input-wrap').click() #利用css定位
#driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(end_times)
#点击时间确定按钮
driver.find_element_by_css_selector('.ant-calendar-ok-btn').click()
time.sleep(2)
#点击全部渠道
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div/div').click()
time.sleep(5)
pyautogui.click(590,306)
#点击搜索按钮
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/span/span/button').click()
time.sleep(3)
numbergs=driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]').text
print(numbergs)
#用正则把C端数据提取
regexj=re.compile(r'已接通(\d+)条')
xjgs=regexj.search(numbergs)
xjgs=xjgs.group(1)
print(str(xjgs))
sheetnamew['G4']=xjgs
#保存
date_time=end_time.strftime('%m%d')
xlsxname=date_time+'数据汇总.xlsx'
wb.save(xlsxname)
'''