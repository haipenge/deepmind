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
		print project.name
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
    


#项目
class Project(object):
	def __init__(self):
		logging.debug('>>>Init projet now')
		self._name = None
		self._repository = None
		#项目的基本配置信息
		self._configs={}
		properties = Properties()
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


    #生成项目结构及基础配置
	def generate(self):
		self.__make_source_dirs()
		self.__create_packages()
		self.__create_properties()
		


#组件、模块
class Component(object):
	def __init__(self):
		logging.debug('>>Init component.')
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,name):
		self._name=name.lower()
	#项目依赖关系
	@property
	def project(self):
		return self._project
	@project.setter
	def project(self,project):
		self._project=project
	#模块包名
	def package_name(self):
		return self.project.package_name+ '.component.' + self.name
	def get_test_package_name(self):
		return self.project.get_test_package_name() +'.component.' + self.name

	#生成组件、模块
	def generate(self):
		java_package_dir = project.java_package_dir()
		test_package_dir = project.test_package_dir()
		component_java_service_package_dir = os.path.join(java_package_dir,'component',self.name,'service','impl')
		component_test_service_package_dir = os.path.join(test_package_dir,'component',self.name,'service')
		component_java_repository_package_dir = os.path.join(java_package_dir,'component',self.name,'repository',self.project.repository,'impl')
		component_test_repository_package_dir = os.path.join(test_package_dir,'component',self.name,'repository',self.project.repository)
		component_java_entity_package_dir = os.path.join(java_package_dir,'component',self.name,'entity')
		component_java_controller_package_dir = os.path.join(java_package_dir,'component',self.name,'controller')
		component_test_controller_package_dir = os.path.join(test_package_dir,'component',self.name,'controller')
		xdirs = [component_java_service_package_dir,component_test_service_package_dir,component_java_repository_package_dir,component_test_repository_package_dir,component_java_entity_package_dir,component_java_controller_package_dir,component_test_controller_package_dir]
		for dir in xdirs:
			if os.path.exists(dir) is False:
				os.makedirs(dir)



class Simple(object):
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,name):
		#首字母强制大写
		self._name = name.capitalize()
	@property
	def project(self):
		return self._project
	@project.setter
	def project(self,project):
		self._project = project
	@property
	def component(self):
		return self._component
	@component.setter
	def component(self,component):
		self._component = component
	#获取当前时间
	def get_current_date(self):
		return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	#生成序列化ID
	def get_serial_version_uid(self):
		return random.randint(10000, 65535)

class Clazz(Simple):
	def __init__(self):
		self.format = FormatUtil()
	def get_table_name(self):
		return self.format.camel_to_underline(self.component.name)+'_'+self.format.camel_to_underline(self.name)
	def get_lower_start_clazz_name(self):
		return self.format.lower_start(self.name)
	def generate(self):
		tpls = ['Entity.java','Service.java','ServiceImpl.java','JpaRepository.java','Controller.java','ServiceTestCase.java','JpaRepositoryTestCase.java','ControllerTestCase.java']
		paths = ['entity','service','service.impl','jpa.repository','controller','test.service','jpa.test.repository','test.controller']
		for tpl,path in zip(tpls,paths):
			self.__generate(self.__tpl_path(tpl),self.output_path(path))
		return self.output_path('entity')
	#取得模板路径
	def __tpl_path(self,tpl_name):
		return os.path.join(properties.get('java.generate.tpl.dir'),tpl_name)
	#取得输出路径
	def output_path(self,path):
		output_paths ={
		'entity':os.path.join(self.project.java_package_dir(),'component',self.component.name,'entity',self.name+'.java'),
		'service':os.path.join(self.project.java_package_dir(),'component',self.component.name,'Service',self.name+'Service.java'),
		'service.impl':os.path.join(self.project.java_package_dir(),'component',self.component.name,'service','impl',self.name+'ServiceImpl.java'),
		'jpa.repository':os.path.join(self.project.java_package_dir(),'component',self.component.name,'repository',self.project.repository,self.name+'Repository.java'),
		'controller':os.path.join(self.project.java_package_dir(),'component',self.component.name,'controller',self.name+'Controller.java'),
		'test.service':os.path.join(self.project.test_package_dir(),'component',self.component.name,'service',self.name+'ServiceTestCase.java'),
	    'jpa.test.repository':os.path.join(self.project.test_package_dir(),'component',self.component.name,'repository',self.name+'RepositoryTestCase.java'),
	    'test.controller':os.path.join(self.project.test_package_dir(),'component',self.component.name,'controller',self.name+'ControllerTestCase.java')
		}
		return output_paths[path]
	#根据模板生成文件
	def __generate(self,tpl,output_file):
		if os.path.exists(tpl):
			tplUtil = TplUtil()
			res = tplUtil.render(tpl,obj=self)
			io_util = IOUtil()
			if not os.path.exists(output_file):
				io_util.write(output_file,res)
			else:
				print '>>Tips:',self.name,'.java 已创建,不进行二次创建' 

#实体类属性定义
class Property(Simple):
	def __init__(self):
		self.format = FormatUtil()
		#属性类型
		self.types = {}
		self.types['string'] = 'String'
		self.types['int'] = 'Integer'
		self.types['integer']='Integer'
		self.types['long'] = 'Long'
		self.types['double'] = 'Double'
		self.types['date']='java.util.Date'
		self.types['float'] ='Float'
		#各类型的默认初始值
		self.default_values = {}
		self.default_values['String'] ='""'
		self.default_values['Integer'] ='0'
		self.default_values['Long'] = '0L'
		self.default_values['Double'] = '0.0D'
		self.default_values['java.util.Date'] = 'new java.util.Date()'
		self.default_values['Float'] = '0.0F'

	@property
	def clazz(self):
		return self._clazz
	@clazz.setter
	def clazz(self,clazz):
		self._clazz = clazz
	#数据类型
	@property
	def type(self):
		res = 'String'
		if self._type != None and self._type != '':
			lower_type = self._type.lower()
			if lower_type.find('.') == -1:
				res = self.types[lower_type]
			else:
				lower_type_array = lower_type.split('.')
				res = self.types[lower_type_array[-1]]
		return res
	@type.setter
	def type(self,type):
		self._type = type
	@property
	#属性标题
	def title(self):
		return self._title
	@title.setter
	def title(self,title):
		self._title = title
	#返回数据库列名
	def get_column_name(self):
		return self.format.camel_to_underline(self.name)
	#返回属性名,马鞍命名法
	def get_property_name(self):
		return self.format.lower_start(self.name)
	#返回方法名,get/set 后半段
	def get_method_name(self):
		return self.format.upper_start(self.name)
	#返回属性默认值
	def get_default_value(self):
		value = self.default_values.get(self.type)
		if value is None:
			value = 'null'
		return value
	#生成属性
	def generate(self):
		properties = Properties()
		property_tpl = os.path.join(properties.get('java.generate.tpl.dir'),"EntityProperty.java")
		entity_path = clazz.output_path('entity')
		if os.path.exists(property_tpl):
			tplUtil = TplUtil()
			res = tplUtil.render(property_tpl,obj=self)
			print 'property res is:',res
			io=IOUtil()
			io.replace(entity_path,'@GenerateEntityProperty',res)


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