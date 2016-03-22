#!/usr/bin/env python
# coding:utf8

from one_finger import settings


def alarm_type():
    if isinstance(settings.ALARM_TYPE, basestring):
        # 它是个字符串，说明是一种报警类型
        fun = settings.ALARM_TYPE()
        return fun
    elif isinstance(settings.ALARM_TYPE, list):
        # 判断是个列表，说明不是一种报警方式
        pass


def email():
    pass


def we_chat():
    pass


def phone():
    pass




