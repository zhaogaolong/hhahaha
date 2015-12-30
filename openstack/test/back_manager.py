#!/usr/bin/env python
# coding:utf8


import sys
import commands

import sys
import os
import commands
import datetime

dt = datetime.datetime.now()
now = dt.strftime('%Y-%m-%d--%X')


class Back():
    def __init__(self):
        if not os.path.exists('/var/back'):
            os.makedirs('/var/back/db')
            os.makedirs('/var/back/etc')
            os.makedirs('/var/back/opt')

    def back_mysql(self):
        db_list = ['nova', 'cinder', 'glance', 'neutron', 'ceilometer', 'boss', 'heat', 'mysql']
        for name in db_list:
            cmd = 'mysqldump %s >/var/back/db/%s.sql' % (name, name)
            status, out = commands.getstatusoutput(cmd)
            if status:
                print '\033[31m command mysqldump error:%s\033[0m' % out

            cmd = 'tar czf /var/back/db/%s-%s.tar.gz /var/back/db/%s.sql' % (name, now, name)
            print cmd
            status, out = commands.getstatusoutput(cmd)
            if status:
                print '\033[31m command tar error:%s\033[0m' % out

    def back_opt(self):
        dir_list = ['boss_bill', 'boss_api', 'tomcat6_api', 'tomcat6_bill', 'horizon']
        for name in dir_list:
            cmd = 'tar czf /var/back/opt/%s-%s.tar.gz /opt/%s' % (name, now, name)
            status, out = commands.getstatusoutput(cmd)
            if status:
                print '\033[31m command tar error:%s\033[0m' % out

    def back_etc(self):
        cmd = 'tar czf /var/back/etc/etc-%s.tar.gz /etc' % now
        status, out = commands.getstatusoutput(cmd)
        if status:
            print '\033[31m command tar error:%s\033[0m' % out

    def clear_up(self):
        cmd = 'find /var/back -mtime +15 -name "*.*" -exec rm -rf {} \;'
        status, out = commands.getstatusoutput(cmd)
        if status:
            print '\033[31m command find error:%s\033[0m' % out


if __name__ == '__main__':
    arg = sys.argv[1]
    ob = Back()
    b = getattr(ob, arg)
    b()
