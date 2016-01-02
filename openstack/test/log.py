#!/usr/bin/env python
# coding:utf8

import logging



# logging.basicConfig(level=logging.DEBUG,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='myapp.log',
#                 filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')


logger = logging.getLogger('one_finger')

logger.setLevel(logging.DEBUG)



# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)



# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
logger = logging.getLogger("test_user1") #写一个用户名，对应下面的formatter中的name
logger.setLevel(logging.DEBUG)  #全局日志级别

#屏幕输出
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  #屏幕输出的日志界别
#写目志
fh = logging.FileHandler("log2.log")
fh.setLevel(logging.DEBUG)  #写入日志的级别

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)  #应用屏幕格式
fh.setFormatter(formatter)  # 应用文 件格式


#把屏幕和file 句柄交给logger接口执行
logger.addHandler(ch)  #输出日志
logger.addHandler(fh) #输出日志
