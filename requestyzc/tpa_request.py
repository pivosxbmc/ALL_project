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
#get_account_id()

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
    '''报案'''
    tpa_create_data = '{"tenantCode":8,"policyNo": "ASSH1234335346655799","isHorsemanSelf":true,"idCardNum":"130635199404242411","reporterCellPhone": "18321020000","accidentDateTime":%d,"accidentAddress": {"province": "上海市","city": "上海市","county": "浦东新区","addrDetail": "出险地点详细地址"},"reportAddress": { "province": "江苏省", "city": "南京市","county": "玄武区","addrDetail": "玄武湖附近"},"accidentDetail": "无","reportEventType": {"eventType": "1","subEventType": "2"},"accidentType": {"firstType": "MULTI_CAR"},"isInjury": "1","otherCarLoss": [{"isDamage": "1","isInjury": "0","isCarLoss": "0"}]}'%i_time
    tpa_create_data = tpa_create_data.encode(encoding='UTF8')
    request = 'https://tpatest.ikandy.cn/api/txfit/v2.0/report'
    Content_Type =  'application/json'
    #User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    newReport_headers={'Content-Type':Content_Type}#,"user-agent":User_Agent}
    r=requests.post(url = request,data=(tpa_create_data),headers= newReport_headers)
    print(r.text)
for i in range(3):
  pass
  #i_time = get_millisecond(i)
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
def tap_login():
  url = 'https://tpatest.ikandy.cn/api/txtechnology/login'
  data = '''
  {
  "loginName":"yzc",
  "password":"123456"
  }
  '''
  Content_Type =  'application/json'
  newReport_headers={'Content-Type':Content_Type}
  r = requests.post(url=url,data=data,headers= newReport_headers,verify=False)
  r = json.loads(r.text)
  print(r['errCode'])
  if int(r['errCode']) == 511:
    data_input = input('账号已经被登录 是否要踢出 y/n')
    if data_input == 'y':
      tpa_kickout('yzc',1)
      r = requests.post(url=url,data=data,headers= newReport_headers,verify=False)
      r = json.loads(r.text)
    else:
      print('登录结束')
      print(r)
      return r
  print(r)
  token = r['result']['userAccessToken']
  return token
def tpa_check_accout(accout,address=1):
  '''查询账号'''
  if  address== 1:
    tap_url = 'https://tpatest.ikandy.cn/api/agent_list?pageIndex=1&pageSize=10&searchStr=%s'%accout
  else:
    tap_url =  'https://tpaprod.ikandy.cn/api/agent_list?pageIndex=1&pageSize=10&searchStr=%s&searchTenant=5e5ca352f5dc310006e2ea62'%accout
  #'https://tpaprod.ikandy.cn/api/agent_list?pageIndex=1&pageSize=10&searchStr=yzc'
  Access_Token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJ5bWYtYWRtaW4iLCJwYXNzd29yZCI6IjEyMzQ1NiIsImlhdCI6MTYwNTE2NDM5NiwiZXhwIjoxNjA1MjUwNzk2fQ.ZdCSJB6P9cKjhnQTyR9xzGl0wP0UAOKvV3ZtmYWjT-Q'
  print(tap_url)
  User_Agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
  headers = {'Accept':'application/json','Access-Token':Access_Token,"user-agent":User_Agent}
  r = requests.get(url=tap_url,headers=headers,verify=False)
  r = json.loads(r.text)
  #print(r)
  return r['result']['agents'][0]["_id"]
def tpa_kickout(accout_id,address=1):
  '''踢出'''
  accout_id = tpa_check_accout(accout_id,address)
  if address == 1:
    url = 'https://tpatest.ikandy.cn/api/agents/kickoutAgent/%s'%accout_id
  else:
    url = 'https://tpaprod.ikandy.cn/api/agents/kickoutAgent/%s'%accout_id
  r = requests.get(url = url,verify=False)
  print(r.text)
def tpa_lossAss_report(data_list=None,token=r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJ5emMiLCJwYXNzd29yZCI6IjEyMzQ1NiIsImlhdCI6MTYwNTY4ODAxOSwiZXhwIjoxNjA1Nzc0NDE5fQ.Mzo6A3Z6J_yrcRdfl9kOjwQa-LPjCNzICOENHmxg1Ns'):
  '''保存按钮'''
  url = 'https://tpatest.ikandy.cn/api/lossAss/newReport'
  User_Agent=r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
  Access_Token=str(token)
  newReport_headers2={'Content-Type':'application/json','Access-Token':Access_Token,"user-agent":User_Agent}
  with open('tpa_test_creat_case.json','r',encoding = 'UTF-8') as f:
    data = json.load(f) #字典
  if data_list:
    creat_case_id_flowid = data_list
    data['id'] = creat_case_id_flowid[0]
    data['flowId'] = creat_case_id_flowid[1]
    print('新数据:'+data['flowId'])
  else:
    print('原数据')
  data = json.dumps(data) #字符串
  r = requests.post(url=url,data=data,headers=newReport_headers2,verify=False)
  #print(r.text)
def creat_case():
  '''创建工单'''
  data = '{"idCardNum":"130635199104240001","policyNo":"ASSH1234335346655777","reporterCellPhone":"18312341234","horsemanCellPhone":"18312341234","reporter":"戚薇测试002","reporterCertCode":"1","reporterCertNum":"130635199104240001","reportEventType":{"eventType":"1","subEventType":"3"},"accidentAddress":{"province":"河北省","city":"邯郸市","county":"永年区","addrDetail":"测试"},"accidentPlace":"测试","accidentDateTime":1601534154992,"accidentDetail":"事件经过测试","agentId":"5e9d079f0ef8be00073e256b","accidentType":{"firstType":"SINGLE_CAR","secondType":"HORSEMAN_INJURY"},"isInjury":"1"}'
  tap_test_url = 'https://tpatest.ikandy.cn/api/lossAss/report/createByAgent'
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
def check_case_id(flowId):
  '''通过工单flowId获取相应的_id等信息,然后可以使用id做保存提交的动作'''
  url = 'https://tpatest.ikandy.cn/api/lossAss/getReportInfo/%s?from=agent'%flowId
  r = requests.get(url = url,verify=False)
  r = json.loads(r.text)
  print(r['errCode'])
  #print(r)
  print(r['result']['stateTrack'][0]['detail']) #+','+r['result']['stateTrack'][1]['detail'])
  return str((r['result']['_id']))
class Tpa_case_state(object):
  """docstring for Tpa_case_"""
  def state_surveied(self,flowId):
    '''提交案件为已查勘状态'''
    url = 'https://tpatest.ikandy.cn/api/lossAss/cpic/tpa/report/resetState?flowId=%s&state=surveied&subState=undefined&agentId=5e9d079f0ef8be00073e256b'%flowId
    r = requests.get(url=url,verify=False)
    r=json.loads(r.text)
    print(r['errInfo'])
  def state_case_receive(self,flowId):
    '''领取任务接口'''
    url = 'https://tpatest.ikandy.cn/api/lossAss/report/agentaccept?flowId=%s&agentId=5e9d079f0ef8be00073e256b'%flowId
    r = requests.get(url=url,verify=False)
    r = json.loads(r.text)
    print(r['errInfo'])
  def finish_case(self,flowId):
    url = 'https://tpatest.ikandy.cn/api/lossAss/cpic/tpa/report/resetState?flowId=%s&state=finished&subState=reject&agentId=5e9d079f0ef8be00073e256b'%flowId
    r = requests.get(url=url,verify=False)
    r = json.loads(r.text)
    print(r)
class Tpa_all__process_case(object):
  """docstring for ClassName"""
  def __init__(self,arg=0):
    self.arg = arg
  def all_process(self):
    token = tap_login()
    tpa_data_id_flowid_list = creat_case()
    tpa_lossAss_report(tpa_data_id_flowid_list)
    check_case_id(tpa_data_id_flowid_list[1])
    time.sleep(1)
    Tpa_case_state().state_surveied(flowId=tpa_data_id_flowid_list[1])
    check_case_id(tpa_data_id_flowid_list[1])
    time.sleep(1)
    Tpa_case_state().state_case_receive(flowId=tpa_data_id_flowid_list[1])


    

if __name__ == '__main__':
  # tap_login()
  # tpa_check_accout('yzc',1)
  tpa_kickout('yzc',2) #1默认测试环境、2是正式环境
  #Tpa_all__process_case().all_process()

  #tpa_lossAss_report(creat_case())  #保存案件信息
  #check_case_id('20201119000010')
  # creat_case()
  # Tpa_case_state().state_surveied(flowId='20200928000003')
  #Tpa_case_state().finish_case(flowId='20201015000012')

