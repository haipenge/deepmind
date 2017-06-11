#!/usr/bin/env python
# -*- coding: utf-8 -*-
'格式转化工具'
__author__='haipenge'

class FormatUtil(object):
    #驼峰命名格式转下划线命名格式
	def camel_to_underline(self,camel_format):
		underline_format=''
		if isinstance(camel_format, str):
			for _s_ in camel_format:
				underline_format += _s_ if _s_.islower() else '_'+_s_.lower()
			while underline_format[0] == '_':
				underline_format = underline_format[1:]
		return underline_format
	#将下划线命名转化为驼峰命名
	def underline_to_camel(self,underline_format):
		camel_format = ''
		if isinstance(underline_format, str):
			for _s_ in underline_format.split('_'):
				camel_format += _s_.capitalize()
		return camel_format
	#首字母小写
	def lower_start(self,str):
		res = ''
		if str is not None:
			res = str[0].lower() + str[1:]
		return res
	#首字母大写
	def upper_start(self,str):
		res = ''
		if str is not None:
			res = str[0].upper() + str[1:]
		return res

    

if __name__ == "__main__":
	print 'start format util...'