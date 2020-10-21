#2019-11-05 14:25:51
"""
L=[]
for x in range(1,11):
	L.append(x*x)

#列表生成器
[x*x for x in range(1,11)]

#闭包
def fu():
	def inner():
		print('in fun')
	return inner
r = fu()
print(r)
r()

def fu():
	a = 10
	def inner():
		print('In fu()')
		print(a)
	return inner

print('举例：')
nums = []
def averages(n):
	nums.append(n)
	return sum(nums)/len(nums)
print(averages(10))
print(averages(20))
print('闭包')

def op_avg():
	nums = []
	def average(n):
		nums.append(n)
		return sum(nums)/len(nums)
	return average
avg = op_avg()
print(avg(10))
print(avg(20))

#装饰器
def add(a,b):
	print('Start...')
	r = a + b
	print('End...')
	return r
def multiply(a,b):
	#求任意俩个数的积
	print('Start...')
	r = a * b
	print('End...')
	return r

def fn():
	print('In fu()')
#无参数函数的情况
def start_end(func):
	#创建一个函数
	def new_func():
		print('Start...')
		func()
		print('End...')
	return new_func
#有参数函数的情况
def add(a,b):
	r = a+b
	return r
bb = add(1,5)
print(bb)
def start_end(func):
	#对其他函数进行拓展，在执行前打印开始和结束
	def new_func(a,b):
		print('Start...')
		result = func(a,b)
		print(result)
		print('End..')
		return result
	return new_func
f = start_end(add)
f(1,5)
print('*'*10)
#完整的装饰器
def start_end(func):
	def new_func(*args,**kwargs):
		print('Start....')
		result = func(*args,**kwargs)
		print('End.....')
		return result
	return new_func

#偏函数
import functools
def int2(x,base=2):
	return int(x,base)
int2('555')
int3 = functools.partial(int,base=2)
"""

'''
import logging

def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s)*2

def main():
	try:
		bar('5')
	except Exception as e:
		logging.exception(e)
main()
print('end')


import logging
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %a"
logging.basicConfig(level=logging.WARNING,
	format=LOG_FORMAT,
	datefmt=DATE_FORMAT,
	filename = r'test.log')
logging.warning('cw')

#单元测试
class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r'错误')

	def __setattr__(self,key,value):
		self[key] = value


def txt1():
	if inputa==testa:
		print('wwww')

from multiprocessing import Process
from multiprocessing import Pool #多子进程,进程池
import os,time,random
import subprocess #启动一个子进程，然后控制其输入和输出
#子进程要执行的代码
def long_time_task(name):
	print('Run task %s(%s)...'%(name,os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('task %s runs %0.2f seconds.'%(name,(end-start)))

def run_porc(name):
	print('Run child process %s(%s)...'%(name,os.getpid()))

if __name__=="__main__":

	print('Parent process %s.' %os.getpid())
	p = Pool(4) #对Pool对象调用join方法之前必须先调用close,参数：设置最多运行几个子进程
	for i in range(5):
		p.apply_async(long_time_task,args=(i,)) #参数：调用函数，函数参数
	print('Waiting for all..')
	p.close()
	p.join()
	print('All subprocesses done')

	p = Process(target=run_proc, args=('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')		


print('测试开始')
r=subprocess.call(['nslookup','www.python.org'])
print('code:',r)
'''
from collections import Counter
c=Counter()
print(c['a'])
for ch in 'program':
	c[ch]=c[ch]+1
print(c)
c=Counter(a=3,b=1,c=2,d=-1)
print(list(c.elements()))
print(c['a'])

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hsahlib?'.encode('utf-8'))
print(md5.hexdigest())
import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns))

import socket
