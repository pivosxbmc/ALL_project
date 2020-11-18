#coding:utf-8
import requests,json,time,datetime,traceback,os,openpyxl,traceback,re,ast,difflib

def gxrb_yds_test():
    '''广西人保账号获取信息'''
    multi_tokens2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJ5emMiLCJwYXNzd29yZCI6IjEyMzQ1NiIsImlhdCI6MTU5OTAxNjE1MCwiZXhwIjoxNTk5MTAyNTUwfQ.eFbeLIF8kKrsp7CeCzDsad0ahMWR6EoPGi3QZquzxHM'
    multi_cookie2 = r'_ga=GA1.2.841391502.1594783400; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22%24device_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D'
    User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    newReport_headers2={'Content-Type':'application/json','Access-Token':multi_tokens2,'Cookie':multi_cookie2,"user-agent":User_Agent}
    gxrb_url = 'https://gxrb-yds-test.ikandy.cn/api/agents/869000213@gxrb-test.txtechnology.com.cn'
    '''广西人保获取核心系统APP账号'''
    r = requests.get(url=gxrb_url,headers= newReport_headers2,verify=False)
    print(type(r))
    datatext = json.loads(r.text)
    #print(datatext)
    with open('njrb.txt','ab+') as f:
        #new_text = '+'.join([datatext['result']['thirdAppAccount'],datatext['result']['thirdAppAccountPass']])
        new_text = '\nAPP账号：%s\nAPP密码：%s\nid：%s\nsim卡id：%s\n时间戳：\n'%(datatext['result']['thirdAppAccount'],datatext['result']['thirdAppAccountPass'],datatext['result']['thirdAccountImeiNo'],datatext['result']['thirdAccountSimNo'])
        print(datatext['result']['thirdAppAccount'])
        f.write(bytes(new_text,'UTF-8'))
def njrb_put_phone(fullUserId,app,apppassword,appid,appsimid,apptime):
    '''南京人保自动填入核心账号信息，参数：fullUserId 确定需要update的人'''
    njrb_url = 'https://yds-dzh-prod.ikandy.cn/api/updateAgentProfile'
    njrb_cookies = r'_dx_uzZo5y=4f1b6f21ff4f33ddaefc3076cb2d77f11f9089f99c81178fd5aabee822f71ef492cb510d; _ga=GA1.2.841391502.1594783400; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22%24device_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _dx_app_6be4cdaed176efb4bbc6843f6381a56e=5f507ed6hXBYiiRrUvsk07slhAsqiVrh9rWBV9E1; _dx_captcha_vid=BBBF5941D3C91AA919D5DBEF79A0DC731A192F9230E1DAA62E05AC3B42AE347AE2F5F3073356F470597565CAB1AEE93D308B5BF61517C5D405A40285E3A1D75748F499821435FF8F4B5857D6089EA820'
    njrb_token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoiNWYwM2E0YThiN2NiMWNmZTQ2ODQ4YmU2N2QwMjY1YTg2ZjY2N2Q0YjgwYTIxODY3MzViMmQwNGQ4NzZhNzIyNCIsImNhcHRjaGEiOiJCQkJGNTk0MUQzQzkxQUE5MTlENURCRUY3OUEwREM3MzFBMTkyRjkyMzBFMURBQTYyRTA1QUMzQjQyQUUzNDdBRTJGNUYzMDczMzU2RjQ3MDU5NzU2NUNBQjFBRUU5M0QzMDhCNUJGNjE1MTdDNUQ0MDVBNDAyODVFM0ExRDc1NzQ4RjQ5OTgyMTQzNUZGOEY0QjU4NTdENjA4OUVBODIwOjVmNTA3ZWQ2aFhCWWlpUnJVdnNrMDdzbGhBc3FpVnJoOXJXQlY5RTEiLCJpYXQiOjE1OTkyMTI4OTUsImV4cCI6MTU5OTI5OTI5NX0.hfjEZFF41qJC-UvcAw8b2pOovmiLKOVSc6a83tXms1M'
    data_njrb_cx = {
      "fullUserId": ''.join((fullUserId+"@undefined")),
      "fullName":fullUserId,
      "email": "18312341311@qq.com",
      "thirdAccountTime": apptime,
      "thirdAppAccountPass": apppassword,
      "thirdAccountSimNo": appsimid,
      "thirdAccountImeiNo": appid,
      "thirdAppAccount": app,
    }
    User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    data =json.dumps(data_njrb_cx)
    njrb_put_headers={'Content-Type':'application/json','Access-Token':njrb_token,'Cookie':njrb_cookies,"user-agent":User_Agent}
    requests.adapters.DEFAULT_RETRIES = 5  
    r = requests.put(njrb_url,data =data,headers = njrb_put_headers,verify=False)
    print(r.text)
    print(r.status_code)
def dzh_create_account(phone,name,loginName):
    data_dzh = {
    "agentRole": "5a17f8eb84e6121f8c31e88e",
    "cellphone":phone,
    "companyId": "txtechnology",
    "fullName":name,
    "loginName": loginName,
    "orgAccount": "5f39fdd0869ab60007d4dbab",
    "password": "99ae7724746b8ff6ddba07996e8df89736d832503d7a4aac240fa1a2df21b44b",
    "permission":'[]',
    "supervisePhone": "123",
    "tenant": "5e424c8ad487960008aa176b",
    }#%(phone,name,loginName)
    dzh_cookie = r'_dx_uzZo5y=4f1b6f21ff4f33ddaefc3076cb2d77f11f9089f99c81178fd5aabee822f71ef492cb510d; _ga=GA1.2.841391502.1594783400; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22%24device_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _dx_app_6be4cdaed176efb4bbc6843f6381a56e=5f507ed6hXBYiiRrUvsk07slhAsqiVrh9rWBV9E1; _dx_captcha_vid=BC7FB9B5FCE3742AEE7D51331C0863D90A97E7A01C60AE464C8C904AF157C9111D0C9F8CC5A09FA8309D9B68CCC251294C71EC1BED37F8BC0EE20470A18BA99B41726B7035A8A27E292885C250189BDD'
    dzh_token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoiMWRkY2JmMDIxYTlhZTEwYjZjYzFhN2M1MGNmYmI1NjVkYTZiZWJiYTE2NmUxNzk5ZGY3NzFlYzhlNTg2ZTdiZiIsImNhcHRjaGEiOiI4RDVFMUJFNkYyMzMzNzk2ODM2QTNGRkJGNTMyMkNBMDczMDZFRTk0NEMyNzcwN0RFQ0YwMDc3RDc0NTRDQTk3RDRGNEZBRjJBRDVDQUYwRTNGQTI5NUM2OTlGQzMxODhGMkEzNEJEMTEwMzZBQzA1RjM3NDY0NzUyQ0IzQUYwQUE2NEJENjM0QzYzNUE4REFBQ0M4QTRCMUVDNzhERjZEOjVmYTI1YWJib0F0MGNWbnB1VWQ4Q0dubEhoajJ3SHJvclp2NjRrMjEiLCJpYXQiOjE2MDQ0ODEyODYsImV4cCI6MTYwNDU2NzY4Nn0._eKYQZwoAvym6HM_DZz_dfReyU6_Jb1Dkf_Tf8Eh1Vs'
    #r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoiMWRkY2JmMDIxYTlhZTEwYjZjYzFhN2M1MGNmYmI1NjVkYTZiZWJiYTE2NmUxNzk5ZGY3NzFlYzhlNTg2ZTdiZiIsImNhcHRjaGEiOiI4RDVFMUJFNkYyMzMzNzk2ODM2QTNGRkJGNTMyMkNBMDczMDZFRTk0NEMyNzcwN0RFQ0YwMDc3RDc0NTRDQTk3RDRGNEZBRjJBRDVDQUYwRTNGQTI5NUM2OTlGQzMxODhGMkEzNEJEMTEwMzZBQzA1RjM3NDY0NzUyQ0IzQUYwQUE2NEJENjM0QzYzNUE4REFBQ0M4QTRCMUVDNzhERjZEOjVmYTI1YWJib0F0MGNWbnB1VWQ4Q0dubEhoajJ3SHJvclp2NjRrMjEiLCJpYXQiOjE2MDQ0ODEyODYsImV4cCI6MTYwNDU2NzY4Nn0._eKYQZwoAvym6HM_DZz_dfReyU6_Jb1Dkf_Tf8Eh1Vs'

    User_Agent =  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    Content_Type =  r'application/json; charset=utf-8'
    dzh_create_url = r'https://yds-dzh-prod.ikandy.cn/api/agents'
    newReport_headers={'Content-Type':Content_Type,'Access-Token':dzh_token,'Cookie':dzh_cookie,"user-agent":User_Agent}
    #data_dzh = data_dzh.encode(encoding='UTF8')
    r = requests.post(url = dzh_create_url,data=json.dumps(data_dzh),headers= newReport_headers,verify=False) #headers= newReport_headers
    #print(r.status_code) #json.dumps(data_dzh)
    print(r.text)
def read_xlsx_zuoxi(filename):
  '''读取表格内容 然后创建账号'''
  wb = openpyxl.load_workbook(filename)
  sheet = wb.get_active_sheet()
  for currt_id_raw in range(2,sheet.max_row+1):
    #sheet.max_row+1
    #账号、姓名、手机号，密码
    user_loginname = sheet.cell(row=currt_id_raw,column=2).value
    user_name = sheet.cell(row=currt_id_raw,column=1).value 
    user_phone = sheet.cell(row=currt_id_raw,column=4).value
    user_phone = str(user_phone)
    user_password = sheet.cell(row=currt_id_raw,column=3).value
    dzh_create_account(user_phone,user_name,user_loginname)
    time.sleep(1)
def get_dzh_agent(agent):
  '''查询账号列表'''
  #dzh_agent = {"pageIndex":"1","pageSize":"10","searchStr":agent}
  dzh_url = 'https://yds-dzh-prod.ikandy.cn/api/agent_list?pageIndex=1&pageSize=10&searchStr=%s'%agent
  dzh_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoiMDRlYmFiODVhMDJkNzc4YjU0NzI0ZDQ2OWZkMmViM2RmMzAzMTU1OWVkNTFhNTM4MWI0NjMyY2Y1MDI0ZTUwYiIsImNhcHRjaGEiOiI5RDk1NzM1RjY1RjQ5ODc5N0E0ODg5Mzk0QjhDNUExNUMxNTc5MzYxNjk5RkM4QkJGN0Q4RUE5RjU5NzFGMzhDMzk4QUNEQjg1RUIzQjJENjdGODgxQkQ5M0UzQTMxNzEyN0Y4RTAwRkIwQ0UzMEFCRTY3QzRCOUY3RDk1RDUxRkUwQ0Y2MUY0NUM3Njk1MDk1RjdCNzdENzExREE4OEM1OjVmYThlN2YwUHhXd0xBakV1UEtwMnVEanFCRkZlMmM0eDllY3BrajEiLCJpYXQiOjE2MDQ5MDYxNzMsImV4cCI6MTYwNDk5MjU3M30.EiNihk4UMdlEth_6yNcAM5k20gYkOJg_5ILi1hjOpEM'
  dzh_cookie = '_dx_uzZo5y=4f1b6f21ff4f33ddaefc3076cb2d77f11f9089f99c81178fd5aabee822f71ef492cb510d; _dx_app_6be4cdaed176efb4bbc6843f6381a56e=5fa8e7f0PxWwLAjEuPKp2uDjqBFFe2c4x9ecpkj1; _dx_captcha_vid=9D95735F65F498797A4889394B8C5A15C1579361699FC8BBF7D8EA9F5971F38C398ACDB85EB3B2D67F881BD93E3A317127F8E00FB0CE30ABE67C4B9F7D95D51FE0CF61F45C7695095F7B77D711DA88C5'
  headers={'Access-Token':dzh_token,'Cookie':dzh_cookie} #,"user-agent":User_Agent}
  
  r = requests.get(url=dzh_url,headers=headers,verify=False)
  print(r.text)

  dict_text = json.loads(r.text)
  print(len(dict_text['result']['agents']))
  print((dict_text['result']['agents'][0]))



if __name__ == '__main__':
  #get_dzh_agent('1111')
  gxrb_yds_test()
  #njrb_put_phone('zqqqq',1,2,3,4,5)
  #dzh_create_account('18312341234','崔腾','109449449')
  #read_xlsx_zuoxi(r'D:\jx\DZH\大案外出智能平台开通账号汇总(1).xlsx')
