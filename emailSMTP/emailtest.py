#2020-01-07 14:02:18
from email.mime.text import MIMEText
import smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import sys
import os

user_path = os.getcwd()
sys.path.append(user_path)

def format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))
#1创建带附件的邮件，先需要创建邮件对象
msg = MIMEMultipart()
'''
#文本主题
msgtest = MIMEText('hello,send by Python..','plain','utf-8')
#HTML类型的邮件
msg = MIMEText('<html><body><h1>Hello</h1>'+'<p>send by<a href="https://www.baidu.com"> baidu </a> 完毕</p>'
	+'</body></html>','html','utf-8')
'''
#输入email地址和口令：
from_addr = 'yu.zichen@txtechnology.com.cn'
password = 'cgdrVDXoxEHHBpME'
#输入收件人的地址：
to_addr =['1094491399@qq.com','2012129495@qq.com']
#输入SMTP服务器地址：
smtp_server = 'smtp.exmail.qq.com'
#发送人和收件人
msg['From'] = format_addr('yu.zichen<%s>'% from_addr)
msg['to'] = format_addr('收件人<%s>'% to_addr)
#标题
msg['Subject'] = Header('录屏报告','utf-8').encode()
#2邮件正文是MIMEText
msg.attach(MIMEText('最后一表：展示的是lost的工单客户身份证和坐席姓名','plain','utf-8'))
#添加附件e，从本地读取一个文件
'''
zipFile = save_filename
zipApart = MIMEApplication(open(zipFile, 'rb').read())
zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)
msg.attach(zipApart)
'''
def run_send_mail(save_filename):
	print('开始')
	zipFile = save_filename
	zipApart = MIMEApplication(open(zipFile, 'rb').read(),zipFile.split('.')[-1])
	zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)
	msg.attach(zipApart)
	server = smtplib.SMTP_SSL(smtp_server,465)
	server.set_debuglevel(1)
	server.login(from_addr,password)
	server.sendmail(from_addr,to_addr,msg.as_string())
	print('success')
	server.quit()

		