#coding:utf-8
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


save_date = {
	'flowId': "GD20200720170229919312",
	'id': "5f155da6ca96c2000759a6ea",
	'insurance': "5cc52f04a636b11604b8d892",
	'insuredMan': "102030",
	'insuredPhone': "18312341234",
	'poliyNo': "",
	'reportId': "10203040",
	'reporter': "测试人" ,
	}
multi_tokens='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJjdWkzNDUiLCJwYXNzd29yZCI6ImM4MGFiNzI0MDIzOWQ4NTY0ODExNjliMzkzOTk3MzA3YzViMDQ3YmM0NDFhZWJjZGFmMWFkNDZjYWUyMGFkNzciLCJjYXB0Y2hhIjoiMEExQ0YwMTBCOEM3MDU4RkUzNDg4NEEzQzc1OTY4M0M4NUQxRUI4QTQzRjRENDA3NUYxNEQxMzI3NzZFODNBNzJBREQzMEYyODQyMTlFQzZBQTFCNEY1NEQxODBGRUY1NTcwOUY3RjdBQTA3RDE3Qzg2MkQzMDEzMzg4RUI4QTQ4QTM3NUZDODc2NUJCNjNGMTI1RjU0ODk5M0MzQzM2MDo1ZjE1NWM5MjBuMXRkR0dFaVN4a3Noc0xCOElOemx1RE9XTml5ZWExIiwiaWF0IjoxNTk1MjM1NjQ0LCJleHAiOjE1OTUzMjIwNDR9.VIGyGjGWfo26ESYNtGknvgDgCF0ibgIdvAqRRoFAhSA'
multi_cookie = '_dx_uzZo5y=481e0783c78885560e9c7b1712e43358a0f1b64c08bcc474b2d594f927b08ba0d8853f5e; _ga=GA1.2.841391502.1594783400; _dx_app_6be4cdaed176efb4bbc6843f6381a56e=5f155c920n1tdGGEiSxkshsLB8INzluDOWNiyea1; _dx_captcha_vid=0A1CF010B8C7058FE34884A3C759683C85D1EB8A43F4D4075F14D132776E83A72ADD30F284219EC6AA1B4F54D180FEF55709F7F7AA07D17C862D3013388EB8A48A375FC8765BB63F125F548993C3C360; userAccessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJjdWkzNDUiLCJwYXNzd29yZCI6ImM4MGFiNzI0MDIzOWQ4NTY0ODExNjliMzkzOTk3MzA3YzViMDQ3YmM0NDFhZWJjZGFmMWFkNDZjYWUyMGFkNzciLCJjYXB0Y2hhIjoiMEExQ0YwMTBCOEM3MDU4RkUzNDg4NEEzQzc1OTY4M0M4NUQxRUI4QTQzRjRENDA3NUYxNEQxMzI3NzZFODNBNzJBREQzMEYyODQyMTlFQzZBQTFCNEY1NEQxODBGRUY1NTcwOUY3RjdBQTA3RDE3Qzg2MkQzMDEzMzg4RUI4QTQ4QTM3NUZDODc2NUJCNjNGMTI1RjU0ODk5M0MzQzM2MDo1ZjE1NWM5MjBuMXRkR0dFaVN4a3Noc0xCOElOemx1RE9XTml5ZWExIiwiaWF0IjoxNTk1MjM1NjQ0LCJleHAiOjE1OTUzMjIwNDR9.VIGyGjGWfo26ESYNtGknvgDgCF0ibgIdvAqRRoFAhSA'
newReport_headers={'Content-Type':'application/json','Access-Token':multi_tokens,'Cookie':multi_cookie}
multi_url='https://multi-insrn-test.ikandy.cn/api/lossAss/newReport'
def creat_multi_newReport():
	r = requests.post(url = multi_url,data=json.dumps(save_date),headers= newReport_headers)
	print(r.status_code)
	print(r.text)

multi_tokens2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJ5emMiLCJwYXNzd29yZCI6IjEyMzQ1NiIsImlhdCI6MTU5OTAxNjE1MCwiZXhwIjoxNTk5MTAyNTUwfQ.eFbeLIF8kKrsp7CeCzDsad0ahMWR6EoPGi3QZquzxHM'
multi_cookie2 = r'_ga=GA1.2.841391502.1594783400; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22%24device_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D'
User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
newReport_headers2={'Content-Type':'application/json','Access-Token':multi_tokens2,'Cookie':multi_cookie2,"user-agent":User_Agent}
gxrb_url = 'https://gxrb-yds-test.ikandy.cn/api/agents/869000213@gxrb-test.txtechnology.com.cn'
def gxrb_yds_test():
    '''广西人保获取核心系统APP账号'''
    r = requests.get(url=gxrb_url,headers= newReport_headers2,verify=False)
    datatext = json.loads(r.text)
    with open('njrb.txt','ab+') as f:
        #new_text = '+'.join([datatext['result']['thirdAppAccount'],datatext['result']['thirdAppAccountPass']])
        new_text = '\nAPP账号：%s\nAPP密码：%s\nid：%s\nsim卡id：%s\n时间戳：\n'%(datatext['result']['thirdAppAccount'],datatext['result']['thirdAppAccountPass'],datatext['result']['thirdAccountImeiNo'],datatext['result']['thirdAccountSimNo'])
        print(datatext['result']['thirdAppAccount'])
        f.write(bytes(new_text,'UTF-8'))
gxrb_yds_test()

njrb_url = 'https://yds-dzh-prod.ikandy.cn/api/updateAgentProfile'
njrb_cookies = r'_dx_uzZo5y=4f1b6f21ff4f33ddaefc3076cb2d77f11f9089f99c81178fd5aabee822f71ef492cb510d; _ga=GA1.2.841391502.1594783400; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22%24device_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _dx_app_6be4cdaed176efb4bbc6843f6381a56e=5f507ed6hXBYiiRrUvsk07slhAsqiVrh9rWBV9E1; _dx_captcha_vid=BBBF5941D3C91AA919D5DBEF79A0DC731A192F9230E1DAA62E05AC3B42AE347AE2F5F3073356F470597565CAB1AEE93D308B5BF61517C5D405A40285E3A1D75748F499821435FF8F4B5857D6089EA820'
njrb_token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoiNWYwM2E0YThiN2NiMWNmZTQ2ODQ4YmU2N2QwMjY1YTg2ZjY2N2Q0YjgwYTIxODY3MzViMmQwNGQ4NzZhNzIyNCIsImNhcHRjaGEiOiJCQkJGNTk0MUQzQzkxQUE5MTlENURCRUY3OUEwREM3MzFBMTkyRjkyMzBFMURBQTYyRTA1QUMzQjQyQUUzNDdBRTJGNUYzMDczMzU2RjQ3MDU5NzU2NUNBQjFBRUU5M0QzMDhCNUJGNjE1MTdDNUQ0MDVBNDAyODVFM0ExRDc1NzQ4RjQ5OTgyMTQzNUZGOEY0QjU4NTdENjA4OUVBODIwOjVmNTA3ZWQ2aFhCWWlpUnJVdnNrMDdzbGhBc3FpVnJoOXJXQlY5RTEiLCJpYXQiOjE1OTkyMTI4OTUsImV4cCI6MTU5OTI5OTI5NX0.hfjEZFF41qJC-UvcAw8b2pOovmiLKOVSc6a83tXms1M'
data_njrb_cx = {
  "fullUserId": "14173244@undefined",
  "email": "18312341311@qq.com",
  "fullName": "王胜",
  "thirdAccountTime": "1599530575036",
  "thirdAppAccountPass": "lI3Y8wBii3ab6Zs_SrZtyA..",
  "thirdAccountSimNo": "89860318240254427735",
  "thirdAccountImeiNo": "860187049612488",
  "thirdAppAccount": "14173244",
}
data_njrb_cx_old = {"fullUserId":"zq@undefined","email": "18312341311@qq.com","fullName": "zq1"}
data =json.dumps(data_njrb_cx)#,sort_keys=True, indent=4, separators=(',', ': '))
njrb_put_headers={'Content-Type':'application/json','Access-Token':njrb_token,'Cookie':njrb_cookies,"user-agent":User_Agent}

def njrb_put_phone():
    requests.adapters.DEFAULT_RETRIES = 5  
    r = requests.put(njrb_url,data =data,headers = njrb_put_headers,verify=False)
    print(r.text)
    print(r.status_code)
#njrb_put_phone()

def dzh_create_account():
    data_dzh = {
    'agentRole': "5a17f8eb84e6121f8c31e88",
    'cellphone': "18312341234",
    'companyId': "txtechnology",
    'fullName': "刘浩测试",
    'loginName': "19285925",
    'orgAccount': "5f39fdd0869ab60007d4dbab",
    'password': "a3a3447847736c573947e8617cfe32f6e2b2bc9f804c470b4c5caa4515ada51f",
    'permission':' ["video"]',
    'supervisePhone': "123",
    'tenant': "5e424c8ad487960008aa176b",
    }
    dzh_cookie = r'_dx_uzZo5y=4f1b6f21ff4f33ddaefc3076cb2d77f11f9089f99c81178fd5aabee822f71ef492cb510d; _ga=GA1.2.841391502.1594783400; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22%24device_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _dx_app_6be4cdaed176efb4bbc6843f6381a56e=5f507ed6hXBYiiRrUvsk07slhAsqiVrh9rWBV9E1; _dx_captcha_vid=BC7FB9B5FCE3742AEE7D51331C0863D90A97E7A01C60AE464C8C904AF157C9111D0C9F8CC5A09FA8309D9B68CCC251294C71EC1BED37F8BC0EE20470A18BA99B41726B7035A8A27E292885C250189BDD'
    dzh_token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoiZDA3NDBjZjVlZjk4MjU4ZTI2YmExZjQyNTVjYTBiNTQwZTRjMjNkMzE4Mzg5NjQ0YmQyZWMyZDk2NDhhYzYzOCIsImNhcHRjaGEiOiJCQzdGQjlCNUZDRTM3NDJBRUU3RDUxMzMxQzA4NjNEOTBBOTdFN0EwMUM2MEFFNDY0QzhDOTA0QUYxNTdDOTExMUQwQzlGOENDNUEwOUZBODMwOUQ5QjY4Q0NDMjUxMjk0QzcxRUMxQkVEMzdGOEJDMEVFMjA0NzBBMThCQTk5QjQxNzI2QjcwMzVBOEEyN0UyOTI4ODVDMjUwMTg5QkREOjVmNTA3ZWQ2aFhCWWlpUnJVdnNrMDdzbGhBc3FpVnJoOXJXQlY5RTEiLCJpYXQiOjE1OTkxMjEyMTQsImV4cCI6MTU5OTIwNzYxNH0.1b_HHLkBY2bJj_Gyob66IOYWhmfantqRDI4z8y4chy0'
    User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    Content_Type =  r'application/json'
    dzh_create_url = r'https://yds-dzh-prod.ikandy.cn/api/agents'
    newReport_headers={'Content-Type':Content_Type,'Access-Token':dzh_token,'Cookie':dzh_cookie,"user-agent":User_Agent}
    r = requests.post(url = dzh_create_url,data=json.dumps(data_dzh),headers= newReport_headers,verify=False)
    print(r.status_code)
    print(r.text)
#dzh_create_account()

tpa_create_data = '{"tenantCode":8,"policyNo": "ASSH1234335346655799","isHorsemanSelf":true,"idCardNum":"130635199404242411","reporterCellPhone": "18321020000","accidentDateTime":1601453103000,"accidentAddress": {"province": "上海市","city": "上海市","county": "浦东新区","addrDetail": "出险地点详细地址"},"reportAddress": { "province": "江苏省", "city": "南京市","county": "玄武区","addrDetail": "玄武湖附近"},"accidentDetail": "无","reportEventType": {"eventType": "1","subEventType": "2"},"accidentType": {"firstType": "MULTI_CAR"},"isInjury": "1","otherCarLoss": [{"isDamage": "1","isInjury": "0","isCarLoss": "0"}]}'
tpa_create_data = tpa_create_data.encode(encoding='UTF8')
tpa_create_data1 = {
    "tenantCode": 8,
    "policyNo": "ASSH1234335346655799",
    "isHorsemanSelf":"true",
    "idCardNum":"130635199404242411",
    "reporterCellPhone": "18321020000",
    "accidentDateTime":1601179200000,
    "accidentAddress": {
     "province": "上海市",
     "city": "上海市",
     "county": "浦东新区",
     "addrDetail": "出险地点详细地址"
    },
    "reportAddress": {
     "province": "江苏省",
     "city": "南京市",
     "county": "玄武区",
     "addrDetail": "玄武湖附近"
    },
    "accidentDetail": "无",
    "reportEventType": {
     "eventType": "1",
     "subEventType": "2"
    },
    "accidentType": {
     "firstType": "MULTI_CAR"
    },
    "isInjury": "1",
    "otherCarLoss": [
     {
      "isDamage": "1",
      "isInjury": "0",
      "isCarLoss": "0"
     } 
 ]
 }

def tap_creat_order():
    request = 'https://tpatest.ikandy.cn/api/txfit/v2.0/report'
    Content_Type =  'application/json' #; charset=utf-8'
    #User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    newReport_headers={'Content-Type':Content_Type}#,"user-agent":User_Agent}
    r=requests.post(url = request,data=(tpa_create_data),headers= newReport_headers)
    print(r.text)
#tap_creat_order()

claim_tenant = '5f59e971af7fa46ce33835ca'
claim_orgAccount ='5f963cf2af7fa46ce3383721'
claim_agent = '5f9914d809991312aac2ecbf'
claim_flowId = 'GD20201028145357326563'
test_tenant='5f4608236149d00007838439'
test_orgAccount = '5f471348aca231000774e39d'
test_agent = '5f603327189555000601de3b'
test_flowId = 'GD20201012105746656215'
A=[claim_tenant,claim_orgAccount,claim_agent,claim_flowId]
A=[test_tenant,test_orgAccount,test_agent,test_flowId]
data = '''{
"tenant":"%s",
"orgAccount":"%s",
"onlyForEncode": true,
"encodeData": {
"agent":"%s",
"flowId":"%s",
"type": 6,
"data": {
"surveyConclude":"1111查勘意见测试测试测试测试测试测试测试田林路200号，俩车碰撞，收集四面",
"signer":"qzrsf",
"place":"000出险地点测试测试测试测试测试测试测试田林路200号，俩车碰撞，收集四面",
"reportId":"12345666666",
"accidentDate":"2020-09-15",
"accidentTime":"03:09:00",
"reporterCellPhone":"15610190001",
"cellPhone":"18312341234",
"accidentResponse":"2",
"insuredName":"测试与",
"carOwner":"驾驶员人于",
"riskSummary":"测试测试测试测试测试测试测试田林路200号，俩车碰撞，收集四面",
"carNumber":"123456",
"frameNo":"vin02",
"ctpPolicyNo":"jqxbdh02",
"comPolicyNo":"syxbdh02",
"encodeEnv":"prod",
"damageReason":"事故原因测试测试测试测试测试测试测试田林路200号，俩车碰撞，收集四面"
}
}
}'''%(A[0],A[1],A[2],A[3])

old_url = 'https://developer.ikandy.cn:63222/api/external/report/update'
new_url = 'https://claim.cloud-ins.cn/api/external/report/update'
def tap_update():
  request = old_url
  Content_Type =  'application/json' #; charset=utf-8'
  newReport_headers={'Content-Type':Content_Type}#,"user-agent":User_Agent}
  datae = data.encode(encoding='UTF8')
  r=requests.post(url = request,data=datae,headers= newReport_headers,verify=False)
  print(r.text)
#tap_update()

date_tap = '''
{
"tenant":"5f4608236149d00007838439",
"orgAccount":"5f471348aca231000774e39d",
"encodeData":"6d7d8f478493a47c704b91c2ac376dec1f66a06b3b18f37519fb65c76d3e245408ca86108559bd02e9459e76da7191189b08b4e638307632a7e9d6f729ff3b728f727df1c7880c4f31cf1a06c3605142dbce015c441930e5bc7e41f00c7426bbb9e4c5e7a27117158625041005a3ec54990022b82ba924a440ae4ea3d586aedde9d556528feaf52a82b7703ccedd759a91e905c26137172fd08a5c3f2badef01491cae0f13ab8eb7de4cba512e377310c6a0a2ab991ca13da900e6fa7c56d9908baaa256e3a4bff9f06a230d31fbbda4e9e52253573b477c82b7b112af7e46bb7878df9eab40e4e9087e29459a8ef6457bb80866ce0b8e303157e155e0ebdd78d5f0d84bb16413019f791673168e9184836dde4dcf391ecab683143dc4021e5b8a8187d2ecb39814a2f93a15659770ff3f4c4e27db8a5e767832a4a12179be45d3a16b134f9393a7cb44bf3ab5cfdb0ad9293e3dc22a551184f74a318851840edae7d62f4f2a274876352e2df849978947038cc66357658fef9c06e2767061eb68a3d48b41d3ef44e248e2a1afe1e13286f1b71d494169912c7784e2df210ccfe62b0af182be24cd39a5d0e8cedab9de58b2810579b610fc0bfb71a528372056e43c1d716bf1056fdd3200b16d674e47bdbd85c49d322a79be5c28ca4b9ecf73fdbd6164aa47f72dfb10049e6ca36b8f199bcb9f40b22a00b41556a4fce63be1f2eca5730227601fe54568679ed41e32e21d60f30bf364a256ed4a7a6d548c741b152d321ce6708b71644e20f0c571d619b64d1ae87dfc21a3d45ee56505cc1318f6dbc3bcb4ffe781db77f25e076a6615eff64890b4bff882115197a8225e13ae686426a3b892e10dda2ef706e5cdeed58c51f16f69bc6592b5139d007e9597040df1416738026c0d54e8c8f449e6ce3c79ad49eee98aad94ae995b180ea53dc328c93211154e5ed20890de8c2f47b65f01cde6b15f468bdaca0bb9f03535aff1672ca4c07e42f0b875cb582d412c19db9971d5b810b932bec6297178ab519fe7b1bc454531cd261d8018cb6d664a70d9ed89a0b3affc839dfa876a4aed6ed41a40c83a714f0279a6a4595f0eba4743c70e49a93a4a21b96bffa6e1d5840132d0e37db65faf60b8f8fc1c49796194c520b72d312be5765f18fb7b892aea43f6c8f94af42c51d5e4c09b58796df7abbf4f9ea7b8b71a69fed664caaff3e087d616cd6db8f90e16377ef7b78326f3e8ec85405cef87e8e3556afb898c0847d832"
}
'''

def tap_update_new():
  request = 'https://dzh-tx-test.ikandy.cn/api/external/report/update'
  Content_Type =  'application/json' #; charset=utf-8'
  newReport_headers={'Content-Type':Content_Type}#,"user-agent":User_Agent}
  #datae = data.encode(encoding='UTF8')
  r=requests.post(url = request,data=date_tap,headers= newReport_headers)
  print(r.text)
tap_update_new()
