#/usr/bin/env python
# -*- coding: utf-8 -*-
from mako.template import Template
from mako.runtime import Context
from mako.lookup import TemplateLookup
from StringIO import StringIO
from util.io_util import IOUtil
from util.io_util import Properties

'模板工具类'
__author__='haipenge'

class TplUtil(object):
	def __init__(self):
		pass
	def render(self,tpl_file,obj):
		tpl = Template(filename=tpl_file,output_encoding='utf-8',input_encoding='utf-8', encoding_errors='replace')
		res = tpl.render(obj=obj)
		return res




if __name__ == '__main__':
	tpl_util=TplUtil()
