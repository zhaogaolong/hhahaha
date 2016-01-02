#!/usr/bin/env python
# coding:utf8

import logging
from django.conf import settings

logger = logging.getLogger('dfsdfsf')

logger.setLevel(logging.DEBUG)



# create file handler which logs even debug messages
# fh = logging.FileHandler('spam.log')
# fh.setLevel(logging.DEBUG)

# # create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


ch.setFormatter(formatter)
# fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
# logger.addHandler(fh)

# create formatter and add it to the handlers



logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
