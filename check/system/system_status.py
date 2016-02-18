#!/usr/bin/env python
# coding:utf8
import datetime
####
from openstack.api import opentack_ansible
from openstack import models


class CheckSystemStatus():
    def __init__(self):
        self.host_list = models.Host.objects.all()

    def check(self):
        for host in self.host_list:
            if not models.SystemInfo.objects.filter():
                host_dic = {
                    'host_id': host.id,
                    'cpu_status': self.cpu(host.ip_manager),
                    'mem_status': self.memory(host.ip_manager),
                    'uptime': datetime.datetime.now().strftime("%F %X")
                }
                host_info_obj = models.SystemInfo(host_dic)
                host_info_obj.save()
            else:
                host_info_obj = models.SystemInfo.objects.get(host_id=host.id)
                host_info_obj.cpu_status = self.cpu(host.ip_manager)
                host_info_obj.mem_status = self.memory(host.ip_manager)
                host_info_obj.uptime = datetime.datetime.now().strftime("%F %X")

    def cpu(self, host_ip):
        cmd = "sar 1 3 |grep Average |awk '{print $8}'"
        b = opentack_ansible.CmmAndRun(
         host=host_ip,
         cmd=cmd)
        data = b.start()
        if data:
            return data
        else:
            return None


    def memory(self):
        pass

    def update(self):
        pass

    def save_db(self):
        pass

