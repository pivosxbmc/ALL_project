import configparser

#输出ini文件所有头文件
print(cfg.sections())
#利用get方法找到 Search下面属性search_button对应的值
search_button = cfg.get('Search','search_button') 
#找到Serrch下面所有键值对
a=cfg.items('Search')


class Readini(object):
	"""读取ini文件"""
	def __init__(self,file_name=None,node=None):
		if file_name == None:
			file_name = 'D:/jx/fengzhuang/config/elements.ini'
		if node == None:
			self.node = 'jx_elements'
		else:
			self.node = node
		#疑惑1：
		self.cf = self.load_ini(file_name)
	#加载文件
	def load_ini(self,file_name):
		cf = configparser.ConfigParser()
		cf.read(file_name)
		return cf
	#获取value的值
	def  get_value(self,key):
		data = self.cf.get(self.node,key)
		return data

		







