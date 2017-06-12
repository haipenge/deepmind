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
from service.generate.settings import Settings
import os


#实体类属性定义
class Property(Simple):
	def __init__(self):
		self.format = FormatUtil()
		self.settings = Settings()

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
			types = self.settings.get_types()
			if lower_type.find('.') != -1:
				lower_type_array = lower_type.split('.')
				lower_type = lower_type_array[-1]
			if types.get(lower_type) == None:
				res = self._type.capitalize()
			else:
				res = types.get(lower_type)
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
		value = self.settings.get_default_values().get(self.type)
		if value is None:
			value = 'null'
		return value
	#生成属性
	def generate(self):
		properties = Properties()
		property_tpl = os.path.join(properties.get('java.generate.tpl.dir'),"EntityProperty.java")
		entity_path = self.clazz.output_path('entity')
		if os.path.exists(property_tpl):
			tplUtil = TplUtil()
			res = tplUtil.render(property_tpl,obj=self)
			io=IOUtil()
			io.replace(entity_path,'@GenerateEntityProperty',res)