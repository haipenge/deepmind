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