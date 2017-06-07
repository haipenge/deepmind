#!/usr/bin/env python
# -*- coding: utf-8 -*-

' show env info'
__author = 'haipenge'

import sys
import os


def settings():
	root_dir = os.path.dirname(os.getcwd())
	log_conf_file = os.path.join(root_dir,'resources','logging.conf')
	print '--Log Conf File is:',log_conf_file
    #logging.config.fileConfig(log_conf_file)
    #logging = logging.getLogger("default")


if __name__ == '__main__':
	settings()