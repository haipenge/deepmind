#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.config
import threading
import os

'IO 工具'
__author__ = 'haipenge'
#cwd = os.getcwd()
#logging.config.fileConfig(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'resources',"logging.conf")) 
#logging = logging.getLogger("default")

##################
#IO 操作工具
##################
class IOUtil(object):
	def __init__(self):
		logging.debug('>>IOUtil init ')
    #读取文件
	def read(self,path,operate='r',size=1024):
		logging.debug('>>Operate is:'+operate)
		try:
		    f = open(path, operate)
		    result = f.read(size)
		    if f:
		    	f.close()
		    return result
		except IOError,e:
			logging.exception(e)
		finally:
			logging.debug('Finally of open file')
	#按行读数据，返回 []
	def readlines(self,path):
		logging.debug('>>Read path is:' + path)
		lines = []
		origin_lines= []
		with open(path,'r') as f:
			origin_lines = f.readlines()
		if len(origin_lines)>0:
			lines = [line.strip('\n') for line in origin_lines]
		return lines
	#写文件
	def write(self,file,content):
		dirs = os.path.split(file)
		if os.path.exists(dirs[0]) is False:
		    os.makedirs(dirs)
		with open(file, 'w') as f:
			f.write(content)

##############################
#property 文件操作工具类
##############################
class Properties(object):
	__default_properties_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'resources')
	__instance = None
	__properties_files = []
	__properties_kvs = []
	__lock = threading.RLock()
	#干预对像创建过程,实现单例
	def __new__(cls, *args, **kwargs):
		cls.__lock.acquire()
		if cls.__instance is None:
			logging.debug('>>...Properties is not instance ,create new instance.')
			try:
				if cls.__instance == None:
					logging.debug('>>Property instance is none,now ,2 create Properties instance.')
					cls.__instance = super(Properties, cls).__new__(cls, *args, **kwargs)
			finally:
				cls.__lock.release()
		return cls.__instance

    #类初始化调用方法
	def __init__(self,file=None):
		super(Properties,self).__init__()
		#加载默认配置，位于resources下的properties
		if len(self.__properties_kvs) == 0:
			self.__properties_kvs = self.__read_properties()
			logging.debug('>>Init default properties ')
		if file:
			if file not in self.__properties_files:
				self.__properties_files.append(file)
				self.__properties_kvs.extend(self.__read_single_file(file))
			logging.debug('>>..Read properties files add by user when instance Properties.')
		logging.debug('>>...Properties call __int__method,to inin values.')

	#根据指定的key取得value
	def get(self,key):
		for kv in self.__properties_kvs:
			if key in kv:
				return kv[key]
		logging.debug('>>property key is:'+key)
		return ''
	#动态添加新的资源文件
	def add_file(self,file):
		if os.path.isfile(file):
			kvs = self.__read_single_file(file)
			self.__properties_kvs.extend(kvs)
			self.__properties_files.append(file)
		logging.debug(self.__properties_kvs)

	def __get_resources_dir(self):
		return self.__default_properties_dir

	#列出指定目录下的所有资源文件
	def __get_properties_files(self):
		dir = self.__get_resources_dir()
		for dirpath, dirnames, filenames in os.walk(dir):
			for filename in filenames:
				full_file_path = os.path.join(dirpath,filename)
				files = os.path.splitext(full_file_path)
				if len(files)>=2 and files[len(files)-1] == '.properties':
					self.__properties_files.append(full_file_path)
		return self.__properties_files

	#读出properties 的所有配置，返回[{k:v},{k:v}]
	def __read_properties(self):
		result = []
		for file in self.__get_properties_files():
			kvs = self.__read_single_file(file)
			result.extend(kvs)
		#logging.debug(result)
		return result

	def __read_single_file(self,file):
		io = IOUtil()
		result = []
		for line in io.readlines(file):
			kv = self.__parse_line(line)
			if kv:
				result.append(kv)	
		return result
	
	#解析每行数据，返回{k,v}
	def __parse_line(self,line):
		result = {}
		if line and line.startswith('#') is False:
			after_line_split = line.split('=')
			if(len(after_line_split)==2):
				if not self.__is_key_exist(after_line_split[0]):
					result[after_line_split[0]] = after_line_split[1]
					return result
		else:
			logging.debug('>>Line is null or start with #')
		return None
    #K:V是否已存在？
	def __is_key_exist(self,key):
		is_exist = False
		for ikv in self.__properties_kvs:
			if key in ikv:
				is_exist = True
				return is_exist
		return is_exist



if __name__ == '__main__':
	print 'Start now.'
	io = IOUtil()
	logging.debug('start debug now.')