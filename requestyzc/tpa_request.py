import requests
import json
from selenium import webdriver
import time,datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import traceback
import os
from selenium.webdriver.chrome.options import Options
import openpyxl
import traceback
import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import pyautogui #鼠标点击
import datetime
from selenium.webdriver.common.keys import Keys
import ast
import difflib

new_list = []
with open(r'C:\Users\DELL\Documents\WeChat Files\sixin2010123\FileStorage\File\2020-09\南京车险账号','r',encoding = 'UTF-8') as f:
    datatext = f.read()
    new_data_list = re.split('},',datatext)
    #datatext = datatext.replace('},','}')
    for i in new_data_list:
        ii = i+'}'
        new_list.append(ii)
#print(new_list[0])
def serch_str_list(loginName_full):
    for i in new_list:
        if i.find(loginName_full) > 0 :
            data_text_dict = json.loads(i)
            print(data_text_dict['fullUserId'])
            return data_text_dict
        else:
            continue       
#new_serch_str_list('16221587')
def get_account_id():
  r = requests.get('https://tpaprod.ikandy.cn/api/agent_list?pageIndex=1&pageSize=1000&searchTenant=5e5ca352f5dc310006e2ea62')
  print(type(r.text))
get_account_id()

def get_millisecond(i):
    #print(time.localtime(time.time()))
    """
    :return: 获取精确毫秒时间戳,13位
    """
    get_time = time.time()-86400*i
    millis = int(get_time)* 1000
    return millis
case_time = get_millisecond(1)*1000


def tap_creat_order(i_time):
    tpa_create_data = '{"tenantCode":8,"policyNo": "ASSH1234335346655799","isHorsemanSelf":true,"idCardNum":"130635199404242411","reporterCellPhone": "18321020000","accidentDateTime":%d,"accidentAddress": {"province": "上海市","city": "上海市","county": "浦东新区","addrDetail": "出险地点详细地址"},"reportAddress": { "province": "江苏省", "city": "南京市","county": "玄武区","addrDetail": "玄武湖附近"},"accidentDetail": "无","reportEventType": {"eventType": "1","subEventType": "2"},"accidentType": {"firstType": "MULTI_CAR"},"isInjury": "1","otherCarLoss": [{"isDamage": "1","isInjury": "0","isCarLoss": "0"}]}'%i_time
    tpa_create_data = tpa_create_data.encode(encoding='UTF8')
    request = 'https://tpatest.ikandy.cn/api/txfit/v2.0/report'
    Content_Type =  'application/json'
    #User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    newReport_headers={'Content-Type':Content_Type}#,"user-agent":User_Agent}
    r=requests.post(url = request,data=(tpa_create_data),headers= newReport_headers)
    print(r.text)
for i in range(3):
  i_time = get_millisecond(i)
  #tap_creat_order(i_time)
def tap_kick_out_account():
  '''踢出账号'''
  url = 'https://tpaprod.ikandy.cn/api/agents/kickoutAgent/5e943b66e1dc070005ef09e8'
  cookie = r'_ga=GA1.2.841391502.1594783400; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22%24device_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D'
  token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJseWgtYWRtaW4iLCJwYXNzd29yZCI6IjEyM0Bxd2UiLCJpYXQiOjE2MDI1NTA1NjcsImV4cCI6MTYwMjYzNjk2N30.KklyLe41Q8mVuWF21ZbcuOakeiYFc6qXK0A6dhdvFgA'
  newReport_headers2={'Content-Type':'application/json','Access-Token':token,'Cookie':cookie,}
  r = requests.get(url=url,headers= newReport_headers2,verify=False)
  print(r.text)
#tap_kick_out_account()
