#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.config

ogging.config.fileConfig("../resources/logging.conf") 
logging = logging.getLogger("default")