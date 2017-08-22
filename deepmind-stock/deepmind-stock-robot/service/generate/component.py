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

'模块组件类'
__author__='haipenge'

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
		java_package_dir = self.project.java_package_dir()
		entity_package_dir=self.project.entity_package_dir()
		test_package_dir = self.project.test_package_dir()
		component_java_service_package_dir = os.path.join(java_package_dir,'component',self.name,'service','impl')
		component_test_service_package_dir = os.path.join(test_package_dir,'component',self.name,'service')
		component_java_repository_package_dir = os.path.join(java_package_dir,'component',self.name,'repository',self.project.repository,'impl')
		component_test_repository_package_dir = os.path.join(test_package_dir,'component',self.name,'repository',self.project.repository)
		component_java_entity_package_dir = os.path.join(entity_package_dir,'component',self.name,'entity')
		component_java_controller_package_dir = os.path.join(java_package_dir,'component',self.name,'controller')
		component_test_controller_package_dir = os.path.join(test_package_dir,'component',self.name,'controller')
		xdirs = [component_java_service_package_dir,component_test_service_package_dir,component_java_repository_package_dir,component_test_repository_package_dir,component_java_entity_package_dir,component_java_controller_package_dir,component_test_controller_package_dir]
		for dir in xdirs:
			if os.path.exists(dir) is False:
				os.makedirs(dir)
