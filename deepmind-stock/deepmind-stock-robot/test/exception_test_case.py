#!/usr/bin/env python
# -*- coding: utf-8 -*-

'module template'

__author__ = 'haipenge'


def try_exception():
	try:
		print 'try'
		r = 10/0
	except ValueError,e:
		print 'value error',e
		logging.exception(e)
	except ZeroDivisionError,e:
		print 'except',e
	finally:
		print 'finally'

class DefaultError(StandardError):
	pass

#抛出异常
def use_self_define_except():
	raise DefaultError('inlls')

if __name__ == '__main__':
	print 'Start now.'
	try_exception();
	use_self_define_except()