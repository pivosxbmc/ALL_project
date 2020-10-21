
from multiprocessing import Process
from multiprocessing import Pool
import os,time,random
import socket


def run_proc(name):
	print('run child process %s..(%s)'%(os.getppid(),os.getpid()))

def long_time_task(name):
	print('Run task %s 父：%s 子：%s '%(name,os.getppid(),os.getpid()))
	#time.sleep(2)
	print('task %s end'%os.getpid())

def main1():
	print('start.........')
	p = Pool(5)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	p.close()
	p.join()
def dance():
	print('>>>>>>>>')
	for x in range(1,10):
		print('我在跳舞')

def sing():
	print('==============')
	for x in range(1,10):
		print('我在唱歌')

def main2():
	p1 = Process(target = dance)
	p2 = Process(target = sing)
	p1.start()
	p2.start()


if __name__ == '__main__':
	#main2()
	a = 'C:\\Users\\DELL\\Pictures\\Feedback\\anxin.png'
	print(a)

