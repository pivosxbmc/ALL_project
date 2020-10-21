print('输入信息：')
first=input()
print('enter the second number to add:')
second=input()
print('the sum is'+first+second) 
import requests #引入下载模板

files=requests.get('https://www.baidu.com')
files.raise_for_status() #如果下载文件出差，会报异常
playfile=open('wa.txt','wb') #下载的文档是二进制的，所以要用二进制的方式写入

for document in files.iter_content(500): #iter_content()方法在循环的每次迭代都返回一段内容，参数是返回一段的字节数
	playfile.write(document)
playfile.close()

import bs4
#files.text：files是网站的主页，然后files有一个text的属性；bs4.BeautifulSoup也可以直接加载一个HTML文件
files.encoding='utf-8' #解决中文乱码问题，极为重要
downloadfile=bs4.BeautifulSoup(files.text,features="html.parser")#第二个参数是加载HTML文件需要的

print(downloadfile.title)
print(downloadfile.find_all('a'))

import re
datafile=downloadfile.find_all('a')
print(type(datafile))
datafile=str(datafile)
a='''href="http://news.baidu.com"'''
print(a)
regex=re.compile(r'((href)(=\S*)(\"))') #正则匹配网址

dataweb=regex.findall(datafile)
print('搜索到的数据：')
print(dataweb)
'''
datafiles=open('datafiles.txt','w')
datafiles.write(str(datafile))
datafiles.close()
'''