#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

from util.env import show_env
'测试用例使用示例'

__author__ = 'haipenge'

class TestModule(unittest.TestCase):
	def setUp(self):
		logging.debug('Set up now.')
	def tearDown(self):
		logging.debug('Tear Down now.')
	def test_env(self):
		env = show_env()
		logging.debug(env)
		self.assertTrue(env != '')





if __name__ == '__main__':
	print 'Start now.'
	unittest.main()