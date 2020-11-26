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

def tap_creat_order():
    '''报案'''
    url = 'https://video-sells-test.ikandy.cn/api/tenant?pageSize=&pageIndex=1'
    date = '{"agentId":"5faba00828ec055deaf2ac94"}'
    Content_Type =  'application/json'
    User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJ0ZWNlbnRscmoiLCJwYXNzd29yZCI6InRlY2VudGxyaiIsImlhdCI6MTYwNTg0OTkyNSwiZXhwIjoxNjA1OTM2MzI1fQ.P-fp-Q5pVijTA-gaavCLyH1_skiy2o8bBPG5X5B4LcU'
    newReport_headers={'Content-Type':Content_Type,'Access-Token':token,"user-agent":User_Agent}
    r=requests.get(url = url,headers= newReport_headers,verify=False) #,data=date,headers= newReport_headers)
    print(r.text)

def tap_creat_orders():
    '''报案'''
    url = 'https://video-sells-test.ikandy.cn/api/serviceRoom/request/list?beginTime=&idpath=&endTime=&agent=&pageIndex=1&pageSize=10&searchTenant=5f437b28708bd45de0d6452b&searchOrgAccount=5f437b4a708bd45de0d6452c&agentId=5faba00828ec055deaf2ac94&timestamp=1605849954'
    Content_Type =  'application/json'
    User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJ0ZWNlbnRscmoiLCJwYXNzd29yZCI6InRlY2VudGxyaiIsImlhdCI6MTYwNTg0OTkyNSwiZXhwIjoxNjA1OTM2MzI1fQ.P-fp-Q5pVijTA-gaavCLyH1_skiy2o8bBPG5X5B4LcU'
    newReport_headers={'Content-Type':Content_Type,'Access-Token':token,"user-agent":User_Agent}
    r=requests.get(url = url,headers= newReport_headers)
    print(r.text)
def creat_case():
  '''创建工单'''
  data = '{"loginName":"testyzc","password":"123456","fullName":"YZC","tenant":"18312341234","reporter":"戚薇测试002","reporterCertCode":"1","reporterCertNum":"130635199104240001","reportEventType":{"eventType":"1","subEventType":"3"},"accidentAddress":{"province":"河北省","city":"邯郸市","county":"永年区","addrDetail":"测试"},"accidentPlace":"测试","accidentDateTime":1601534154992,"accidentDetail":"事件经过测试","agentId":"5e9d079f0ef8be00073e256b","accidentType":{"firstType":"SINGLE_CAR","secondType":"HORSEMAN_INJURY"},"isInjury":"1"}'
  tap_test_url = 'https://video-sells-test.ikandy.cn//api/agents'
  Access_Token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJ5emMiLCJwYXNzd29yZCI6IjEyMzQ1NiIsImlhdCI6MTYwNTQ5MTY2OSwiZXhwIjoxNjA1NTc4MDY5fQ.iqWfY5fK34jNFQ-aUvlmIOP1QS23DnV86Ubc7-m9quI'
  User_Agent=r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
  test_url = 'https://tpatest.ikandy.cn/api/lossAss/report/createByAgent'
  newReport_headers2={'Content-Type':'application/json','Access-Token':Access_Token,"user-agent":User_Agent}
  data =data.encode(encoding='UTF8')
  r = requests.post(url=test_url,data=data,headers=newReport_headers2,verify=False)
  #print(r.text)
  r = json.loads(r.text)
  r = [r['result']['_id'],r['result']['flowId'],r['errCode']]
  #print(r)
  return r
def login():
  '''创建工单'''
  data = '{"loginName":"testyzc","password":"123456","fullName":"YZC","tenant":"18312341234","reporter":"戚薇测试002","reporterCertCode":"1","reporterCertNum":"130635199104240001","reportEventType":{"eventType":"1","subEventType":"3"},"accidentAddress":{"province":"河北省","city":"邯郸市","county":"永年区","addrDetail":"测试"},"accidentPlace":"测试","accidentDateTime":1601534154992,"accidentDetail":"事件经过测试","agentId":"5e9d079f0ef8be00073e256b","accidentType":{"firstType":"SINGLE_CAR","secondType":"HORSEMAN_INJURY"},"isInjury":"1"}'
  tap_test_url = 'https://video-sells-test.ikandy.cn/api/login'
  Access_Token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJ5emMiLCJwYXNzd29yZCI6IjEyMzQ1NiIsImlhdCI6MTYwNTQ5MTY2OSwiZXhwIjoxNjA1NTc4MDY5fQ.iqWfY5fK34jNFQ-aUvlmIOP1QS23DnV86Ubc7-m9quI'
  User_Agent=r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
  test_url = 'https://tpatest.ikandy.cn/api/lossAss/report/createByAgent'
  newReport_headers2={'Content-Type':'application/json','Access-Token':Access_Token,"user-agent":User_Agent}
  data =data.encode(encoding='UTF8')
  r = requests.post(url=test_url,data=data,headers=newReport_headers2,verify=False)
  #print(r.text)
  r = json.loads(r.text)
  r = [r['result']['_id'],r['result']['flowId'],r['errCode']]
  #print(r)
  return r
tap_creat_order()