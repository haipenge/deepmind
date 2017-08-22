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
import os

'工程类'
__author__='haipenge'

#项目
class Project(object):
	def __init__(self):
		logging.debug('>>>Init projet now')
		self._name = None
		self._repository = None
		#项目的基本配置信息
		self._configs={}
		properties = Properties()
		self.properties=properties
		self.name = properties.get('project.name') if properties.get('project.name') != '' else ''
		self.package_name = properties.get('project.package.name') if properties.get('project.package.name') != '' else ''
		self.type = properties.get('project.repository') if properties.get('project.repository') != '' else ''
		self.root_dir = properties.get('project.root.dir') if properties.get('project.root.dir') != '' else ''
	#项目名称
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,name):
		self._name=name
		self._configs['project.name']=self._name

	#顶层包名
	@property
	def package_name(self):
		return self._package_name
	@package_name.setter
	def package_name(self,package_name):
		if package_name == None:
			self.package_name = 'com.faceye'
		else:
			self._package_name=package_name.lower()
		self._configs['project.package.name'] = self._package_name
	#获取测试包名
	def get_test_package_name(self):
		return self.package_name+'.test'
	#项目类型，如Spring-boot类型
	@property
	def type(self):
		return self._type
	@type.setter
	def type(self,type):
		self._type = type
		self._configs['project.type'] = self._type

    #项目根目录
	@property
	def root_dir(self):
		return self._root_dir
	@root_dir.setter
	def root_dir(self,root_dir):
		self._root_dir=root_dir
		self._configs['project.root.dir']=self._root_dir
	#项目的持久化类型
	@property
	def repository(self):
		return self._repository.lower()
	@repository.setter
	def repository(self,repository):
		self._repository = repository if repository is not None and repository !='' else 'jpa'
		self._configs['project.repository'] = self._repository
	#获取基础目录
	def project_dir(self):
		return os.path.join(self.root_dir,self.name + '-api')
	def java_dir(self):
		return os.path.join(self.project_dir(),'src','main','java')
	def test_dir(self):
		return os.path.join(self.project_dir(),'src','main','test','java')
	def resources_dir(self):
		return os.path.join(self.project_dir(),'src','main','resources')
	def filters_dir(self):
		return os.path.join(self.project_dir(),'src','main','filters')
	###################实体项目类#############################################
	#实体类项目路径，分离实体类与具体服务类
	def entity_project_dir(self):
		return os.path.join(self.root_dir,self.name + '-entity')
	def entity_project_java_dir(self):
		return os.path.join(self.entity_project_dir(),'src','main','java')
	
	
	#获取项目包路径 exam:root/src/main/java/com/faceye
	def java_package_dir(self):
		packages = self.package_name.split('.')
		java_package_dir = self.java_dir()
		for p in packages:
			java_package_dir = os.path.join(java_package_dir,p)
		return java_package_dir
	#返回entity java 包路径
	def entity_package_dir(self):
		packages = self.package_name.split(".")
		entity_java_package_dir=self.entity_project_java_dir()
		for p in packages:
			entity_package_dir = os.path.join(entity_java_package_dir,p)
		return entity_java_package_dir
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
		xdirs = [self.java_dir(),self.test_dir(),self.resources_dir(),self.filters_dir(),self.entity_project_dir(),self.entity_project_java_dir()]
		logging.debug(xdirs)
		for dir in xdirs:
			if os.path.exists(dir) is False:
				os.makedirs(dir)

	#创建包结构
	def __create_packages(self):
		java_package_dir = self.java_package_dir()
		test_package_dir = self.test_package_dir()
		entity_package_dir = self.entity_package_dir()
		if os.path.exists(java_package_dir) is False:
			os.makedirs(java_package_dir)
		if os.path.exists(test_package_dir) is False:
			os.makedirs(test_package_dir)
		if os.path.exists(entity_package_dir) is False:
			os.makedirs(entity_package_dir)
	#编写properties文件
	def __create_properties(self):
		properties_file = os.path.join(self.project_dir(),'project.properties')
		properties = Properties()
		lines = ''
		for k,v in self._configs.items():
			value = properties.get(k)
			if value == None or v != value:
				lines += k
				lines += '='
				lines += v
				lines += '\n'
		if lines != '':
			io = IOUtil()
			io.write(properties_file,lines)
	#生成pom文件
	def __generate_pom(self):
		pom_entity_file=os.path.join(self.entity_project_dir(),'pom.xml')
		pom_api_file=os.path.join(self.project_dir(),'pom.xml')
		if not os.path.exists(pom_entity_file):
			shutil.copy(os.path.join(self.properties.get('java.generate.tpl.dir'),'pom-entity-jpa.xml'), pom_entity_file)
		if not os.path.exists(pom_api_file):
			shutil.copy(os.path.join(self.properties.get('java.generate.tpl.dir'),'pom-api.xml'),pom_api_file)
    #生成项目结构及基础配置
	def generate(self):
		self.__make_source_dirs()
		self.__create_packages()
		self.__generate_pom()
		self.__create_properties()