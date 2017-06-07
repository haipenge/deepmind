#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import logging
import os
from util.io_util import IOUtil
from util.io_util import Properties
logging.basicConfig(level=logging.DEBUG)

'IO操作测试用例'

__author__ = 'haipenge'

class TestIO(unittest.TestCase):
	def setUp(self):
		logging.debug('...................Set up now............................')
	def tearDown(self):
		logging.debug('...................Tear Down now.........................')
	def test_read(self):
		io = IOUtil()
		result = io.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'resources','env.properties'),'r',1024)
		logging.debug(">>File Content is:"+result)
		self.assertTrue(result)
	'''
	def test_get_properties_files(self):
		propertiesUtil = PropertiesUtil()
		properties_files=propertiesUtil.__get_properties_files()
		for file in properties_files:
			logging.debug('>>file is :'+file)
		self.assertTrue(len(properties_files)>0)
	def test_read_lines(self):
		propertiesUtil = PropertiesUtil()
		properties_files=propertiesUtil.__get_properties_files()
		lines = propertiesUtil.readlines(properties_files[0])
		logging.debug('>> Line count of file '+properties_files[0]+ " is:")
		self.assertTrue(len(lines) > 0)
    '''
	def test_get_exist(self):
		propertiesUtil = Properties()
		value=propertiesUtil.get('resource.dir')
		logging.debug('Read properties file success:resource.dir='+value)
		self.assertTrue(value!='')
	def test_get_not_exist(self):
		properties = Properties()
		value = properties.get('not.exist')
		self.assertTrue(value == '')
	def test_add_file(self):
		properties = Properties()
		properties.add_file(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'resources','add.properties'))
		value = properties.get('add.file')
		self.assertTrue(value == '1')
	def test_write(self):
		io = IOUtil()
		content = "Test Write with python"
		file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'temp','test.py')
		io.write(file,content)
		readContent = io.read(file)
		self.assertTrue(readContent!=None)

	def test_singlon(self):
		properties =  Properties()
		logging.debug(properties.get('resources.dir'))
		properties =  Properties()
		self.assertTrue(properties)




if __name__ == '__main__':
	print 'Start now.'
	unittest.main()