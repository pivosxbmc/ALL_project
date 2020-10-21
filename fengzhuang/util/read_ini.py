#coding=utf-8
import configparser
class ReadIni(object):
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "D:/jx/fengzhuang/config/elements.ini"
        if node == None:
            self.node = "tpa_common_element"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding="utf-8")
        return cf

    #获取value得值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data


class ReadMultiIni(object):
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "D:/jx/fengzhuang/config/MultiMcu.ini"
        if node == None:
            self.node = "Multi]"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding="utf-8")
        return cf

    #获取value得值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data