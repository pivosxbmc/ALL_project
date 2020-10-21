#coding=utf-8
import sys
sys.path.append('D:\\jx\\fengzhuang')
from util.read_ini import ReadIni,ReadMultiIni

class FindElement(object):
	def __init__(self,driver,nodes):
		self.driver = driver
		self.nodes = nodes

	def get_element(self,key):
		read_ini = ReadIni(node=self.nodes)
		data = read_ini.get_value(key)
		by = data.split('>')[0]
		value = data.split('>')[1]

		try:
			if by == 'id':
				return self.driver.find_element_by_id(value)
			elif by == 'xpath':
				return self.driver.find_element_by_xpath(value)
			elif by == 'className':
				return self.driver.find_element_by_class_name(value)
			elif by == 'class_Name':
				return self.driver.find_elements_by_class_name(value)
			else:
				return self.driver.find_element_by_name(value)
		except :
			return None
	def get_multi_element(self,key):
		read_ini = ReadMultiIni(node=self.nodes)
		data = read_ini.get_value(key)
		by = data.split('>')[0]
		value = data.split('>')[1]

		try:
			if by == 'id':
				return self.driver.find_element_by_id(value)
			elif by == 'xpath':
				return self.driver.find_element_by_xpath(value)
			elif by == 'className':
				return self.driver.find_element_by_class_name(value)
			elif by == 'class_Name':
				return self.driver.find_elements_by_class_name(value)
			else:
				return self.driver.find_element_by_name(value)
		except :
			return None
	