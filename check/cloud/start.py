#!/usr/bin/env python
# coding:utf8
import time
###
from celery import task
# from cloud import nova


@task()
class job():
    def start(self):
        while True:
            time.sleep(1)
            print "start rsync job........"



