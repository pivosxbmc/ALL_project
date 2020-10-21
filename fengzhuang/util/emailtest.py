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
path_file=os.path.abspath(os.path.join(os.getcwd(), "../case/report/"))  # 获取上上级目录
lists = os.listdir(path_file)
lists.sort(key=lambda fn: os.path.getmtime(path_file+'\\'+fn))
path_files=os.path.join(path_file,lists[-1])
sys.path.append(user_path)

def format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))
class Run_Send_Mail(object):
	"""docstring for run_send_mail"""
	def __init__(self):
		#1创建带附件的邮件，先需要创建邮件对象
		self.msg = MIMEMultipart()
		#输入email地址和口令：
		self.from_addr = 'yu.zichen@txtechnology.com.cn'
		self.password = 'cgdrVDXoxEHHBpME'
		#输入收件人的地址：
		self.to_addr =['1094491399@qq.com','2012129495@qq.com']
		#输入SMTP服务器地址：
		self.smtp_server = 'smtp.exmail.qq.com'
		#发送人和收件人
		self.msg['From'] = format_addr('yu.zichen<%s>'% self.from_addr)
		self.msg['to'] = format_addr('收件人<%s>'% self.to_addr)
		#标题
		self.msg['Subject'] = Header('录屏报告','utf-8').encode()
		#2邮件正文是MIMEText
		self.msg.attach(MIMEText('Tpa 测试报告','plain','utf-8'))

	def send_mail(self,save_filename=path_files):
		print('开始')
		zipFile = save_filename
		zipApart = MIMEApplication(open(zipFile, 'rb').read(),zipFile.split('.')[-1])
		zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)
		self.msg.attach(zipApart)
		server = smtplib.SMTP_SSL(self.smtp_server,465)
		server.set_debuglevel(1)
		server.login(self.from_addr,self.password)
		server.sendmail(self.from_addr,self.to_addr,self.msg.as_string())
		print('success')
		server.quit()
