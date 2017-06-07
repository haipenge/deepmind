#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

'module template'

__author__ = 'haipenge'



def test_logging():
	logging.info('Now,Run in logging.')

if __name__ == '__main__':
	print 'Start now.'
	test_logging()