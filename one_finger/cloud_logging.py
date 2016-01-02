#!/usr/bin/env python
# coding:utf8


import logging
from django.conf import settings


class cloud_logging():
    # def __init__(self):
    logger = logging.getLogger('one_finger')
    if settings.DEBUG:
        debug_level = logging.DEBUG
    else:
        debug_level = logging.INFO

    logger.setLevel(debug_level)

    # create file handler which logs even debug messages
    fh = logging.FileHandler(settings.LOG_DIR)
    fh.setLevel(debug_level)

    # create console handler with a higher log level
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.ERROR)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fh.setFormatter(formatter)

    logger.addHandler(fh)

    # def debug(self):
    #     return self.logger.debug
    #
    # def info(self):
    #     return self.logger.info
    #
    # def waring(self):
    #     return self.logger.waring
    #
    # def error(self):
    #     return self.logger.error
    #
    # def critical(self):
    #     return self.logger.critical
