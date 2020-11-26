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


User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
njrb_url = 'https://yds-dzh-prod.ikandy.cn/api/updateAgentProfile'
njrb_cookies = r'_dx_uzZo5y=4f1b6f21ff4f33ddaefc3076cb2d77f11f9089f99c81178fd5aabee822f71ef492cb510d; _ga=GA1.2.841391502.1594783400; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22%24device_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _dx_app_6be4cdaed176efb4bbc6843f6381a56e=5f507ed6hXBYiiRrUvsk07slhAsqiVrh9rWBV9E1; _dx_captcha_vid=BBBF5941D3C91AA919D5DBEF79A0DC731A192F9230E1DAA62E05AC3B42AE347AE2F5F3073356F470597565CAB1AEE93D308B5BF61517C5D405A40285E3A1D75748F499821435FF8F4B5857D6089EA820'
njrb_token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoiNWYwM2E0YThiN2NiMWNmZTQ2ODQ4YmU2N2QwMjY1YTg2ZjY2N2Q0YjgwYTIxODY3MzViMmQwNGQ4NzZhNzIyNCIsImNhcHRjaGEiOiJCQkJGNTk0MUQzQzkxQUE5MTlENURCRUY3OUEwREM3MzFBMTkyRjkyMzBFMURBQTYyRTA1QUMzQjQyQUUzNDdBRTJGNUYzMDczMzU2RjQ3MDU5NzU2NUNBQjFBRUU5M0QzMDhCNUJGNjE1MTdDNUQ0MDVBNDAyODVFM0ExRDc1NzQ4RjQ5OTgyMTQzNUZGOEY0QjU4NTdENjA4OUVBODIwOjVmNTA3ZWQ2aFhCWWlpUnJVdnNrMDdzbGhBc3FpVnJoOXJXQlY5RTEiLCJpYXQiOjE1OTkyMTI4OTUsImV4cCI6MTU5OTI5OTI5NX0.hfjEZFF41qJC-UvcAw8b2pOovmiLKOVSc6a83tXms1M'
data_njrb_cx = {
  "fullUserId": "zq@undefined",
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
A1=[claim_tenant,claim_orgAccount,claim_agent,claim_flowId]
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
    "surveyConclude": "ckjl02",
    "signer": "qzrsf",
    "carNumber": "1106",
    "swpfsm": "实物赔付声明",
    "adjuster": "理赔员姓名",
    "place": "出险地点地点地点地点地点88888888",
    "reportId": "test20090201",
    "accidentDate": "2020-09-15",
    "accidentTime": "03:09:00",
    "reporterCellPhone": "15610190001",
    "insuredName": "bbxr",
    "frameNo": "vin02",
    "ctpPolicyNo": "jqxbdh02",
    "comPolicyNo": "syxbdh02",
    "damageReason": "sgyy02原因原因8888888事故原因事故原因",
    "lossAmount": "000",
    "damageFees": [{
        "name": "物损物品1",
        "lossAmount": "111"
      }
    ],
    "otherCarLoss": [{
        "carNumber": "三者1106",
        "lossId": "326r",
        "accidentTime": "03:09:00",
        "insuredName": "bbxr",
        "frameNo": "vin02",
        "ctpPolicyNo": "jqxbdh02",
        "comPolicyNo": "syxbdh02",
        "damageReason": "sgyy02原因原因8888888事故原因事故原因",
        "lossAmount": "333"
      }
    ]
  }
}
}'''%(A[0],A[1],A[2],A[3])

'''
    "damageFees": [{
        "name": "物损物品1",
        "lossAmount": "111"
      }
    ],
    "otherCarLoss": [{
        "carNumber": "三者1106",
        "lossId": "326r",
        "accidentTime": "03:09:00",
        "insuredName": "bbxr",
        "frameNo": "vin02",
        "ctpPolicyNo": "jqxbdh02",
        "comPolicyNo": "syxbdh02",
        "damageReason": "sgyy02原因原因8888888事故原因事故原因",
        "lossAmount": "333"
      }
'''
old_url = 'https://dzh-tx-test.ikandy.cn/api/external/report/update'
new_url = 'https://claim.cloud-ins.cn/api/external/report/update'
def tap_update():
  request = old_url
  Content_Type =  'application/json' #; charset=utf-8'
  newReport_headers={'Content-Type':Content_Type}#,"user-agent":User_Agent}
  datae = data.encode(encoding='UTF8')
  r=requests.post(url = request,data=datae,headers= newReport_headers,verify=False)
  print(r.text)



date_tap = '''
{
"tenant":"5f4608236149d00007838439",
"orgAccount":"5f471348aca231000774e39d",
"encodeData":"6d7d8f478493a47c704b91c2ac376dec1f66a06b3b18f37519fb65c76d3e245408ca86108559bd02e9459e76da7191189b08b4e638307632a7e9d6f729ff3b728f727df1c7880c4f31cf1a06c3605142dbce015c441930e5bc7e41f00c7426bb3f34ba6ca3bf0f70f3f5f8d51cff519b9bbdb2ac9dbd7f2c9f9a6bb91c97c35852d2642c6f87bb4fed7396dd7b31600933481bc301b3cb2745f12bd33a3209e0f611e49c6481bf3c297fa1a5c0387f69607b17a5ef91b8092a7ad1d26d5fb4c94182884861482d983c8741b05b2480cc4f41be1f6319d5cffe3898fcfd88edc267e9ebc4cf554aba51fce1455f3d2b78457f2c1d281cee9b1ff85de8148390d014d860ae5cefb63f8eda999e763b730f5244fb689449ab7ddd31ededb2678f837a3765566c9c734e8d6c0f363e2e05bf21f701178a136f1d1029d9ace7ef7fe1e110bf80fcddb7bea78d85ffcca1e9cac9a49b5024560047b64100be57c6bc92a8f4a8a63c856e29975ad8b38da8157e44037c05d9e704e2419987637e8c2269cb6036fcf3c5036d4c92f9b81ee1d593a31cd1dc035665816c18f15a06d5e906bcbe3fd66e56eb89a39080a7d59a08a28a2d848c01f9833e5e7117e510ca9f85fb826cc9b76898cf31245357f5e97c23f5e6c5c99aa287e8355b38f169d62f4371b754466a225bba2b46b39efef0b7f70b606649ca58786537a420e5f828d291f45cae97dc540e944239c2853595925b652993278706e037261c1741e1f3ffce57cbff8246f0a9770172b00ce7fb352c9d81f65500c2bb80332b0bd4dad240f2ba77fb9bb0dadc2c7f59dfcee367e6eab3e79cde0b78e01a5c4856ac1cf0c1fcaf4bb74f3f652ad2bffcb924323b48ab251db341f10f002e3457e8f47a97411f6badf0aea3583ceb2d15c50fab25fa3211bf9e4de8da08f7c034e4f82a411e1aeeb11475b6804e260a8b7c4e22e07285cbdb97fd4d657283e100602ff1873bfe462205c92e0972fe1452e02c647853b568586ceb23f5424c8400be95070c02c48dd74d9d656c2c745c06bd069c3913b34c50ea13658179da02c492cf96ba13082a851ae80b5b2381f9051a10b43ef34a135b4ce79ffe6e355bf1118fede853d0e852921c0b1a3f13f0f4ca7e6485681c9f5ec91359d50d52237ba233e3351c981423c8b557667998f4226d6d746b8e50d82862e2fdeb75f1d57688162a35869453fd14abc4d1097c162e619f05f2db40"
}
'''

date_tap_zhlh = '''
{
"tenant":"5f59e971af7fa46ce33835ca",
"orgAccount":"5f963cf2af7fa46ce3383721",
"encodeData":"229d9aa5e74a20e010674839a598ab32c77f7bfa0f50b1176842243afd50314fdd40d72fce7b747ebaf5779789449f88b064e373b0137abedc590377f4b329c0c9bceb6299f944058ddc21ba86336bacf6dc1fa743279b543f3fec36e1761e97af0c762ba48e084720bd5ebf99b23b116c9918b3f6f75cc2dc0ddef40fbd01c3dc2fb10752e85b343bc23c87e90a6ccca1f0088effc27d040a2ae0ae4748fa3325cb701b0b1963d17cc8f0a5ded87effae0f23e55a4cc12b49302664cc758a31a9fbf01665720c6aedb9989873bfd97ca6fe64a1aa479ded6180210d94bbbada00d72a9c44445df7f42c5ca7be0975643fed1b3ae308ca9df3170049de823fe493d925a006b6eea90b4d5135d48d9f99f530681f2a592d93e0c1d7ad7907c82fa0c2119516d48fa2de676ff361b6a99655c004ab9b729a9d6cd97113dbcf1c3619bc09ae6339ec6dc67dfe222984fcd894b0b9c43252be3d9ad7cf14c5366bfeea2c20af7e0e8f8ff235ca517a2c62580da4e2b92af8fb50f455fcbde7422044d5971f3da2400c0e3dd68b0fc79b274b3b8d45b9033463e9c65bae0505cb6d24"
}
'''
def tap_update_old():
  request = 'https://dzh-tx-test.ikandy.cn/api/external/report/update'
  Content_Type =  'application/json' #; charset=utf-8'
  newReport_headers={'Content-Type':Content_Type}#,"user-agent":User_Agent}
  #datae = data.encode(encoding='UTF8')
  r=requests.post(url = request,data=date_tap,headers= newReport_headers,verify=False)
  print(r.text)
def tap_update_new():
  request = 'https://claim.cloud-ins.cn/api/external/report/update'
  Content_Type =  'application/json' #; charset=utf-8'
  newReport_headers={'Content-Type':Content_Type}#,"user-agent":User_Agent}
  #datae = data.encode(encoding='UTF8')
  r=requests.post(url = request,data=date_tap_zhlh,headers= newReport_headers,verify=False)
  print(r.text)
#tap_update()
tap_update_old()
#tap_update_new()