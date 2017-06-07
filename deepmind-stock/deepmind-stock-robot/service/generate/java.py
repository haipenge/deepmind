#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import shutil
import tempfile
#logging.basicConfig(level=logging.DEBUG)
import env
from util.io_util import IOUtil
import os

'Java 自动化项目工具'
__author__ = 'haipenge'

class SmartJava(object):
	def __init__(self):
		logging.debug('>>Start Smart Java now.')
	def ask(self):
		self.project_name = raw_input('请输入项目名称:')
		self.module_name = raw_input('模块名:')
		while self.module_name == None or self.module_name == '':
			self.module_name = raw_input('模块名:')
		self.package_name = raw_input('顶层包名:')
		if self.package_name == '':
			self.package_name = 'com.faceye'
	#Generate a string-boot empty project
	def spring_boot(self,project_name):
		is_spring_boot_project = raw_input('是否创建spring-boot类型的工程？"Y":"N"')
		if is_spring_boot_project == 'Y':
		    for x in os.listdir(os.path.join('./','template','spring_boot')):
			    if os.path.isfile(x):
				    shutil.copy (x, os.path.join("./",'tmp'))



    #生成项目骨架->包结构
	def generate_empty_project_struct(self):
		properties = properties()
		root_dir = properties.get('java.generate.dir')
		self.project_home_java = os.path.join(root_dir,self.project_name,'src','main','java')
		self.project_home_test = os.path.join(root_dir,self.project_name,'src','main','test','java')
		project_home_resources = os.path.join(root_dir,self.project_name,'src','main','resources')
		project_home_wepapp = os.path.join(root_dir,self.project_name,'src','main','webapp')
		project_home_filters = os.path.join(root_dir,self.project_name,'src','main','filters')
		self.__create_package()
		dir_structs = [self.project_home_java,project_home_resources,project_home_wepapp,project_home_filters,project_home_test]
		for path in dir_structs:
			if os.path.exists(path) is False:
				os.makedirs(path)
		self.spring_boot(self.project_name)
    
    #创建目录
	def __create_package(self):
		if self.package_name == '':
			self.package_name = 'com.faceye'
		packages = self.package_name.split('.')
		for p in packages:
			self.project_home_java = os.path.join(self.project_home_java,p)
			self.project_home_test = os.path.join(self.project_home_test,p)
		self.project_home_test = os.path.join(self.self.project_home_test,'test')



class Project(object):




if __name__ == '__main__':
	logging.debug('Start Smart Java.')
	smart_java = SmartJava()
	smart_java.ask()
	logging.debug('Project name is:'+smart_java.project_name)
	logging.debug('module :'+smart_java.module_name)
	logging.debug('package:'+smart_java.package_name)
	smart_java.generate_empty_project_struct()