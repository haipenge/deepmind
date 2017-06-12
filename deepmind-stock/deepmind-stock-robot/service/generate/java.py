#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import shutil
import tempfile
import time
import random
import sys
#logging.basicConfig(level=logging.DEBUG)
#import env
from util.io_util import IOUtil
from util.io_util import Properties
from util.tpl_util import TplUtil
from util.format_util import FormatUtil
from service.generate.project import Project
from service.generate.component import Component
from service.generate.clazz import Clazz
from service.generate.property import Property
from service.generate.simple import Simple
import os


'Java 自动化项目工具'
__author__ = 'haipenge'

class SmartJava(object):
	def __init__(self):
		reload(sys)
		sys.setdefaultencoding('utf8')
		logging.debug('>>init Smart Java now.')
		global project
		project=Project()
		global component
		component=Component()
		global properties
		properties = Properties()
		component.project = project
		global clazz
		clazz = Clazz()
		clazz.project = project
		clazz.component = component
		
	def ask(self):
		project.name = project.name if project.name != '' else raw_input('请输入项目名称:') 
		component.name = raw_input('模块名:')
		while component.name == None or component.name == '':
			component.name = raw_input('模块名:')
		project.package_name = raw_input('顶层包名[com.faceye(default)]:')
		if project.package_name == None or project.package_name == '':
			project.package_name = 'com.faceye'
		project.repository = raw_input('请输入持久化类型[jpa(default),mongo]-->')

	#Generate a string-boot empty project
	def spring_boot(self):
		is_spring_boot_project = raw_input('是否创建spring-boot类型的工程？"Y":"N"')
		if is_spring_boot_project == 'Y':
			project.type='spring_boot'
			for x in os.listdir(os.path.join('template','spring_boot')):
				print('x is:',x)
				if os.path.isfile(os.path.join('template','spring_boot',x)):
					print('x:',x,'is a file')
					shutil.copy(os.path.join('template','spring_boot',x), project.project_dir())
				else:
					print('x ',x,'is not a file')

	def clazz(self):
		clazz.name = raw_input('请输入实体类名,[Exam:User]-->')
		while clazz.name == None or clazz.name =='':
			clazz.name = raw_input('请输入实体类名,[Exam:User]-->')
		clazz.generate()
	def property(self):
		self.is_continue = 'Y'
		while self.is_continue.lower() == 'y':
			property = Property()
			property.project = project
			property.component  = component
			property.clazz = clazz
			property.name = raw_input('请输入属性名:[ Exam:name ] -->')
			property.type = raw_input('请输入数据类型:[ Exap:string ] -->')
			property.title = raw_input('请输入名称:[ Exap:姓名 ]-->')
			while property.name == None or property.name =='':
				property.name = raw_input('请输入属性名:[ Exam:name ] -->')
				property.type = raw_input('请输入数据类型:[ Exap:string ] -->')
			property.generate()
			self.is_continue = raw_input('继续创建属性输入[ Y ],结束[ N ] -->')



    #生成项目骨架->包结构
	def generate_empty_project_struct(self):
		project.root_dir = properties.get('java.generate.dir')
		project.generate()
		component.generate()
		self.spring_boot()
		self.clazz()
		self.property()
    

	






class Xml(Simple):
	def __init__(self):
		pass
	def generate(self):
		pass
class Jsp(Simple):
	def __init__(self):
		pass
	def generate(self):
		pass
class Css(Simple):
	def __init__(self):
		pass
	def generate(self):
		pass
class Javascript(Simple):
	def __init__(self):
		pass
	def generate(Simple):
		pass

if __name__ == '__main__':
	logging.debug('Start Smart Java.')
	smart_java = SmartJava()
	smart_java.ask()
	smart_java.generate_empty_project_struct()