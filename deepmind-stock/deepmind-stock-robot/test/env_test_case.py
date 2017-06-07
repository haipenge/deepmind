#!/usr/bin/env python
# -*- coding: utf-8 -*-

'module template'

__author__ = 'haipenge'

from util.env import show_env

def test_show_env():
	sys_path = show_env()
	print sys_path



if __name__ == '__main__':
	print 'Start now.'
	test_show_env()