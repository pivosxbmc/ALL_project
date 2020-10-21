print('yu',end='')#结尾
print('zi')
print('yu','zi')
print('yu','zi',sep=',') #sep字符间隔用什么展示
def spam():
	global eggs
	eggs='spam'
eggs='global'
spam()
print(eggs)
#异常
print('>>>>>>><<<<<<')
def spam(div):
	try:
		return 42/div
	except ZeroDivisionError:
		print('ERROR:invaild')
print(spam(0))
import random
'''
secretNumber=random.randint(2,15)
print('i am thinking of a number between 1 and 20.')

for guesses in range(1,6):
	print('take a guess.')
	guess=int(input())

	if guess<secretNumber:
		print('you guess is too low')
	elif guess>secretNumber:
		print('you guess is too high')
	else:
		break
if guess == secretNumber:
	print('good job!')
else:
	print('no')

import pprint

spam={'name':'yu','age':18}
a=spam.setdefault('color','black')
print(a)
#计算每个字符出现多少次
test={} #空字典
phrase='Don\'t play games with me!'
for i in phrase:
	test.setdefault(i,0) #setdefault为字典键设置一个默认值，如果有值就返回存在的值
	test[i]+=1

print(test)
pprint.pprint(test)

theBoard={'top-L':' ','top-M':' ','top-R':' ','M-L':' ','m-m':' ','m-r':' ','l-l':' '
,'l-m':' ','l-r':' '}
def printBoard(board):
	print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
	print('-----')
	print(board['M-L']+'|'+board['m-m']+'|'+board['m-r'])
	print('-----')
	print(board['l-l']+'|'+board['l-m']+'|'+board['l-r'])

turn='X'
for i in range(9):
	printBoard(theBoard)
	print('Turn for'+turn+'.Move no which space?')
	move=input()
	theBoard[move]=turn
	if turn=='X':
		turn='O'
	else:
		turn='X'
printBoard(theBoard)
'''
print('正则表达式：')
import re
namess=re.compile(r'name:(\w)(\w)w*')
aa=namess.sub(r'\2##','name:AAA;name:BBB;name:CCC')
print(aa)


maybehigh=re.compile(r'(y){3,5}?')
names=maybehigh.search('my namelyyyyi')
a=names.group()
print(a)
regex=re.compile(r'(\d{3})-(\d{3}-\d{4})')
mmm=regex.search('my number is 10-123-1234;your number is 123-123-2345')
print(mmm.groups())

#adnroid  ios
nogreed=re.compile('W',re.I)
mo=nogreed.sub('1','<www the >for dinner>')
print(mo)
testverbose=re.compile(r'''( \d+ #匹配数字至少一个
\s #后面跟一个空格
\w #单次
)''',re.VERBOSE)
test=re.compile(r'\d+\s\w')
word=testverbose.findall('1 a;2 b;333')
print(word)

import time
data=time.strftime('%m%d-%H%M',time.localtime(time.time()))
#文件模式
baconfile=open('file.txt','w')
baconfile.write('hello world\n')
baconfile.close()
baconfile=open('file.txt','a')
baconfile.write('I have confirmed with the user'+str(data))
baconfile.close()
baconfile=open('file.txt')
readfile=baconfile.read()
baconfile.close()
print(readfile)
#shelve模块
import shelve
shelffile=shelve.open('mydata')
cats=['yu','zi','chen']
shelffile['cat']=cats
shelffile.close()

import os

files=open('filetest.py','w')
files.close()
