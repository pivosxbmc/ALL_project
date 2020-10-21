import openpyxl
'''
wb=openpyxl.load_workbook('珠海.xlsx')
sheet=wb.get_sheet_by_name('Sheet3')
a=tuple(sheet['A1':'M3'])
b=sheet['A1':'A3']
print(a)
print(b)
a=0
aa=[]
for i in sheet['A2':'A4']:
	a+=1
	
	for ii in i:
		#print(ii.value)
		aa.append(ii.value)
print(aa)
#邮箱：
import smtplib
smtp = smtplib.SMTP() 
smtp.connect('smtp.exmail.qq.com',25) 
smtp.login('yu.zichen@txtechnology.com.cn', 'iTxtyzc2017') 
smtp.sendmail('yu.zichen@txtechnology.com.cn', '1094491399@qq.com', msg.as_string('hellp')) 
smtp.quit()
rowlist=[]
print(sheet.columns)
for i in sheet.columns:
	rowlist=[]
	for ii in i:
		iivalue=ii.value
		rowlist.append(iivalue)
print(rowlist)
print(len(rowlist))

'''
name='yu zi chen'
print(name.title())

def function(first_name,last_name,age=''):
	person={'first':first_name,'last':last_name}
	if age:
		person['age']=age
	return person
aa=function('yu','w',12)
print(aa)
aaa='1'
if aaa:
	print('www')

class Dog():
	"""docstring for Dog"""
	def __init__(self, name,age):
		self.name = name
		self.age = age
	def sit(self):
		print(self.name.title()+' is now sitting')
	def roll_over(self):
		print(self.name.title()+'rolled over')

my_dog=Dog('yuan',10)
print('我的狗名字是：'+my_dog.name.title())
my_dog.sit()
class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0 #初始值为0
	def get_descriptive_name(self):
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
	def read_odometer(self):
		print('Thie car has '+str(self.odometer_reading))
	def update_odometer(self,mileage):
		"""更新里程数据"""
		self.odometer_reading = mileage
	def update_max_odometer(self,mileage):
		"""将里程表读树设置为指定的值，禁止将里程表读数回调"""
		if mileage >= self.odometer_reading:
			self.odometer_reading= mileage
		else:
			print("you can't roll back an odometer!")
	def increment_odometer(self,miles):
		"""将里程表读数增加指定的量"""
		self.odometer_reading += miles

my_new_car=Car('奥迪','A4',2010)
print(my_new_car.get_descriptive_name())
my_new_car.update_max_odometer(1000)
my_new_car.read_odometer()
my_new_car.increment_odometer(2000)
my_new_car.read_odometer()

#继承
class ElectricCar(Car):
	def __init__(self,make,model,year):
		"""初始化父类的属性,添加子类的属性"""
		super().__init__(make,model,year)
		self.battery_size = 70
	def describe_battery(self):
		"""打印电瓶的信息"""
		print('This car has a '+str(self.battery_size))

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
#针对ElectrucCar类单独列一类
class Battery():
	def __inin__(self,battery_size=70):
		"""初始化电瓶的属性"""
		self.battery_size=battery_size
	def describe_battery(self):
		"""打印电瓶的信息"""
		print('This car has a '+str(self.battery_size))
#继承Car类
class ElectricCar(Car):
	def __init__(self,make,model,year):
		"""初始化父类的属性,添加子类的属性"""
		super().__init__(make,model,year)
		"""创建一个Battery()的实例"""
		self.battery=Battery()

#collections中的OrderedDict类会记录键-值对的添加顺序
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['saran'] = 'c'
favorite_languages['safai'] = 'ios'
for name,language in favorite_languages.items():
	print(name.title()+' + '+language.title())

with open('test.txt','a') as files:
	files.write('\n测试文档aa\n')
	files.write('第二行aa\n')

#异常
try:
	print(5/0)
except ZeroDivisionError:
	print('不能除0')
else:
	pass #成功是返回结果
finally:
	pass
#储存数据 json	
import json
filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)#读取json文件里面的数据
except FileNotFoundError:
	username = input('你的名字：')
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj) #加载数据到json
		print('欢迎回来'+username+'!')
else:
	print('欢迎'+username)
finally:
	pass
#重构前
def greet_user():
	"""问候用户"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		username = input('你的名字')
		with open(filename,'w') as f_obj:
			json.dump(username,f_obj)
			print('欢迎回来'+username)
	else:
		print('第二次欢迎回来'+username)
greet_user()
 #重构
def get_stored_username():
	"""这个函数负责获取用户值"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
def get_new_username():
	"""新用户获取"""
	username = input('请输入名字：')
	filename = 'username.json'
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	return username
def greet_user():
	"""先获取用户信息"""
	username = get_stored_username()
	if username:
		print('Welcome back，'+username)
	else:
		"""如果不存在就是新用户"""
		username = get_new_username()
		print("We'll remember you :"+username)
greet_user()

#要被测试的代码
def get_formatted_name(first,last,middle=''):
	full_name=first+'-'+last
	if middle:
		full_name = first+' '+ last + ' '+middle
	else:
		full_name=first+'-'+last
	return full_name.title()
#检查函数是否正常运行
import unittest
class NamesTestCase(unittest.TestCase):
	"""测试函数"""
	def test_first_last_name(self):
		"""以test_开头的方法会自动运行"""
		formatted_name = get_formatted_name('yu','zi')
		self.assertEqual(formatted_name,'Yu-Zi')#断言，验证第一个参数是不是等于第二个参数
	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name('yu','zi','chen')
		self.assertEqual(formatted_name,'Yu Zi Chen')
#unittest.main()
#如果函数报错，一般我们要修改测试的函数代码，而不是修改测试本身

print('测试类')
#测试类
#创建类
class Anon():
	def __init__(self,question):
		"""加入一个参数"""
		self.question = question
		self.responses = []
	def show_question(self):
		print(question)
	def store_response(self,new_response):
		"""储存问题"""
		self.responses.append(new_response)
	def show_results(self):
		print('显示')
		for response in self.responses:
			print('-'+response)
question = '请说出LOL喜欢的选手'
my_survey = Anon(question)
my_survey.show_question()
while True:
	response = input('选手:')
	if response == 'q':
		break
	my_survey.store_response(response)
print('感觉你参与survey！')
my_survey.show_results()
#
class TestAnon(unittest.TestCase):
	"""docstring for TestAnon"""
	def setUp(self):
		"""创建一个调查对象和一组答案"""
		question = "请说出LOL最喜欢的人们："
		self.my_survey = Anon(question)
		self.responses = ['uzi','shy','ming']
	def test_store_single_response(self):

		self.my_survey.store_response('xiaohu')
		self.assertIn('xiaohu',self.my_survey.responses)
	def test_store_three_responses(self):
		"""测试三个答案会储存"""
		responses = ['uzi','ming','shy']
		#先分别储存
		for i in self.responses:
			self.my_survey.store_response(i)
		#再分别验证
		for i in self.responses:
			self.assertIn(i,self.my_survey.responses)

#方法setUp(),python将先运行setUp(),再运行各个以test_开头的方法
unittest.main()