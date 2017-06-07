#!/usr/bin/env python
# -*- coding: utf-8 -*-
' a test module '
__author__ = 'haipenge'

import sys
try:
	import cStringIO as StringIO  #import c StringIO as Default
except ImportError:
	import StringIO
try:
	import json #python >2.6
except:
	import simplejson as json #python <2.5
def test():
	args = sys.argv
	if len(args) ==1:
		print 'Hello world!'
	elif len(args) == 2:
		print 'Hellow,%s' % args[1]
	else:
		print 'Too many arguments!'

if __name__ == '__main__':
	test()