#!/usr/bin/env python
# -*- coding: utf-8 -*-

'基础配置'

__author__='haipenge'

class Settings(object):
	def __init__(self):
		pass
	#属性类型
	def get_types(self):
		types = {}
		types['string'] = 'String'
		types['int'] = 'Integer'
		types['integer']='Integer'
		types['long'] = 'Long'
		types['double'] = 'Double'
		types['date']='java.util.Date'
		types['float'] ='Float'
		return types
	#各类型的默认初始值
	def get_default_values(self):
		default_values = {}
		default_values['String'] ='""'
		default_values['Integer'] ='0'
		default_values['Long'] = '0L'
		default_values['Double'] = '0.0D'
		default_values['java.util.Date'] = 'new java.util.Date()'
		default_values['Float'] = '0.0F'
		return default_values