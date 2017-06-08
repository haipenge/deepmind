#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import shutil
import tempfile
#logging.basicConfig(level=logging.DEBUG)
#import env
from util.io_util import IOUtil
from util.io_util import Properties
import os

'Java 自动化项目工具'
__author__ = 'haipenge'

class SmartJava(object):
	def __init__(self):
		logging.debug('>>init Smart Java now.')
		global project
		project=Project()
		global component
		component=Component()
		global properties
		properties = Properties()
		
	def ask(self):
		project.name = raw_input('请输入项目名称:')
		component.name = raw_input('模块名:')
		while component.name == None or component.name == '':
			component.name = raw_input('模块名:')
		project.package_name = raw_input('顶层包名:')
		if project.package_name == None or project.package_name == '':
			project.package_name = 'com.faceye'
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



    #生成项目骨架->包结构
	def generate_empty_project_struct(self):
		project.root_dir = properties.get('java.generate.dir')
		project.generate()
		component.generate()
		self.spring_boot()
    


#项目
class Project(object):
	def __init__(self):
		logging.debug('>>>Init projet now')
		self._name = None
	#项目名称
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,name):
		self._name=name

	#顶层包名
	@property
	def package_name(self):
		return self._package_name
	@package_name.setter
	def package_name(self,package_name):
		if package_name == None:
			self.package_name = 'com.faceye'
		else:
			self._package_name=package_name

	#项目类型，如Spring-boot类型
	@property
	def type(self):
		return self._type
	@type.setter
	def type(self,type):
		self._type = type

    #项目根目录
	@property
	def root_dir(self):
		return self._root_dir
	@root_dir.setter
	def root_dir(self,root_dir):
		self._root_dir=root_dir
	#获取基础目录
	def project_dir(self):
		return os.path.join(self.root_dir,self.name)
	def java_dir(self):
		return os.path.join(self.root_dir,self.name,'src','main','java')
	def test_dir(self):
		return os.path.join(self.root_dir,self.name,'src','main','test','java')
	def resources_dir(self):
		return os.path.join(self.root_dir,self.name,'src','main','resources')
	def filters_dir(self):
		return os.path.join(self.root_dir,self.name,'src','main','filters')
	#获取项目包路径 exam:root/src/main/java/com/faceye
	def java_package_dir(self):
		packages = self.package_name.split('.')
		java_package_dir = self.java_dir()
		for p in packages:
			java_package_dir = os.path.join(java_package_dir,p)
		return java_package_dir
	#获取测试包路径,exam:root/src/main/test/java/com/faceye/test
	def test_package_dir(self):
		packages = self.package_name.split('.')
		test_package_dir = self.test_dir()
		for p in packages:
			test_package_dir = os.path.join(test_package_dir,p)
		test_package_dir = os.path.join(test_package_dir,'test')
		return test_package_dir



	#生成基础源码目录
	def __make_source_dirs(self):
		xdirs = [self.java_dir(),self.test_dir(),self.resources_dir(),self.filters_dir()]
		logging.debug(xdirs)
		for dir in xdirs:
			if os.path.exists(dir) is False:
				os.makedirs(dir)

	#创建包结构
	def __create_packages(self):
		java_package_dir = self.java_package_dir()
		test_package_dir = self.test_package_dir()
		if os.path.exists(java_package_dir) is False:
			os.makedirs(java_package_dir)
		if os.path.exists(test_package_dir) is False:
			os.makedirs(test_package_dir)


    #生成项目结构及基础配置
	def generate(self):
		self.__make_source_dirs()
		self.__create_packages()
		


#组件、模块
class Component(object):
	def __init__(self):
		logging.debug('>>Init component.')

	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,name):
		self._name=name
	#项目依赖关系
	@property
	def project(self):
		return self._project
	@project.setter
	def project(self,project):
		self._project=project
	#生成组件、模块
	def generate(self):
		java_package_dir = project.java_package_dir()
		test_package_dir = project.test_package_dir()
		component_java_service_package_dir = os.path.join(java_package_dir,'component',self.name,'service','impl')
		component_test_service_package_dir = os.path.join(test_package_dir,'component',self.name,'service')
		component_java_repository_package_dir = os.path.join(java_package_dir,'component',self.name,'repository','impl')
		component_test_repository_package_dir = os.path.join(test_package_dir,'component',self.name,'repository')
		xdirs = [component_java_service_package_dir,component_test_service_package_dir,component_test_service_package_dir,component_test_repository_package_dir]
		for dir in xdirs:
			if os.path.exists(dir) is False:
				os.makedirs(dir)





if __name__ == '__main__':
	logging.debug('Start Smart Java.')
	smart_java = SmartJava()
	smart_java.ask()
	smart_java.generate_empty_project_struct()