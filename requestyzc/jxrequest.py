import requests
import http.cookiejar as cookielib
import urllib.request
import re

#session 代表某一次连接
jxsession = requests.session()
jxsession.cookies = cookielib.LWPCookieJar(filename='jxCookie.txt')


userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
header = {
	#"Origin": https://hc.ikandy.cn
	"Referer": 'https://hc.ikandy.cn/login',
	'User-Agent': userAgent,
}

def jxlogin(account,password):
	print('登录')

	posturl = 'https://hc.ikandy.cn/login'
	postdata = {
		"loginName":account,
		"password":password,
	}
	responseRes = requests.get(posturl,data = postdata,headers = header)
	print(f"statusCode = {responseRes.status_code}")
	print(f"text = {responseRes.text}")

	#登录成功之后把cookie保存到本地
	jxsession.cookies.save()

#多租户
dzhsession = requests.session()
dzhsession.cookies = cookielib.LWPCookieJar(filename='dzhCookie.txt')
dzhsession.cookies = cookielib.LWPCookieJar('myaxis.cookies')


dzhuserAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
dzhheader = {
	#"Origin": https://hc.ikandy.cn
	"Referer": 'https://yds-dzh-prod.ikandy.cn/txtechnology/login',
	'User-Agent': dzhuserAgent,
}
def dzhlogin(account,password):
	print('dzh登录')

	posturl = 'https://yds-dzh-prod.ikandy.cn/api/txtechnology/login'
	postdata = {
		"loginName":account,
		"password":password,
	}
	responseRes = requests.get(posturl,data = postdata,headers = dzhheader)
	print(f"statusCode = {responseRes.status_code}")
	#print(f"text = {responseRes.text}")

	#登录成功之后把cookie保存到本地
	#dzhsession.cookies.save(ignore_expires=True)

def dzh_data():
	url='https://yds-dzh-prod.ikandy.cn/api/lossAss/getReports/listPage?pageSize=10&pageIndex=1&searchTenant=5df1f2813475460007affb59&isVideoSurvey=1&state=holdedOn,surveied&beginTime=1596556800&endTime=1597161600'
	headers = {'Access-Token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiIxMDk0NDkiLCJwYXNzd29yZCI6ImY0NjAzMzM5NDlmMmNhMzkxZTdjOWE5MDg1N2ZkYjg5ZTk0NzQ0YzMyNmFlNGI3ZWM3MzNhOTAxZGY0NWE5NzYiLCJjYXB0Y2hhIjoiOUVDODQ2QjQ3MDY2RDNDQTAwODE3ODIzRTNEMUNFRDBGODhGNjk2MEE4RUFCREFERDBGQkM1QUJCN0Y5Q0I2QjNFODBCQzE2MzdBRUYxNzNCREQ4M0MyMkM5MDhBMzVBQjU3OEY4Q0E5NDM0OTc0REFCM0U2NTZDQUNCMjg5Q0M2QjYyRkM2MEVCRjhDNTM5MjEzMEE1QTg3Njc4MTA2Mzo1ZjMzNTIzYVo5M0NkR1NnemFQRUdORFNoYkZQUU9XT0tabGZLb0kxIiwiaWF0IjoxNTk3MjIzMDcyLCJleHAiOjE1OTczMDk0NzJ9.DN2Wpcn0qL-3qFbd4ptfIuY5NTlUiP9pFlCaiyVv7mM',
	'Cookie':r'_dx_uzZo5y=4f1b6f21ff4f33ddaefc3076cb2d77f11f9089f99c81178fd5aabee822f71ef492cb510d; _ga=GA1.2.841391502.1594783400; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22%24device_id%22%3A%221738e63e67311-08d580513c2524-67e1b3f-1049088-1738e63e674609%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _dx_app_6be4cdaed176efb4bbc6843f6381a56e=5f33523aZ93CdGSgzaPEGNDShbFPQOWOKZlfKoI1; _dx_captcha_vid=9EC846B47066D3CA00817823E3D1CED0F88F6960A8EABDADD0FBC5ABB7F9CB6B3E80BC1637AEF173BDD83C22C908A35AB578F8CA9434974DAB3E656CACB289CC6B62FC60EBF8C5392130A5A876781063'}
	res = requests.get(url=url,headers=headers)
	print(res.cookies)
	data=re.findall('count":(\d+)',res.text)
	print(data[0])
def test_url():
	data = {'loginName':"yzc",'password':"123456"}
	res = requests.post('https://tpatest.ikandy.cn/api/txtechnology/login',data=data)
	print(res.status_code)
	print(res.cookies)
	print(type(res.text))
	print(res.json())
if __name__ == "__main__":
	#jxlogin('zyyadmin1','yy880914')
	#jxsession.cookies = cookielib.LWPCookieJar('myaxis.cookies')
	dzh_data()
	test_url()
	'''
	dzhlogin('ymf-admin','123456')
	dzhsession.cookies.save()
	session.cookies = cookielib.LWPCookieJar('myaxis.cookies')
	'''