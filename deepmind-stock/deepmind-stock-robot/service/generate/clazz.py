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
from service.generate.simple import Simple
import os


class Clazz(Simple):
	def __init__(self):
		self.format = FormatUtil()
		self.properties = Properties()
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
		return os.path.join(self.properties.get('java.generate.tpl.dir'),tpl_name)
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