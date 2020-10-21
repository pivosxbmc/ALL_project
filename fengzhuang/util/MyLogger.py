import os
import logging
from datetime import datetime
class My_Log(object):
	"""docstring for My_Log"""
	def __init__(self):
		global resultPath,logpath
		resultPath = os.path.abspath(os.path.join(os.getcwd(), "../case/report/"))
		if not os.path.exists(resultPath):
			os.mkdir(resultPath)
		logpath = os.path.join(resultPath,str(datetime.now().strftime('%m%d_%H_%M')))
		log_file = logpath+'.log'
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.INFO)
		self.filehandler = logging.FileHandler(log_file,'a',encoding='utf-8')
		formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
		self.filehandler.setFormatter(formatter)
		self.logger.addHandler(self.filehandler)
	def get_log(self):
		return self.logger
