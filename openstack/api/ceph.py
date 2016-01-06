#!/usr/bin/env python
# coding:utf8

#import pdb
###
from openstack import models as openstack_models
from opentack_ansible import CmmAndRun


class Ceph():
    def __init__(self,):
        self.ip = openstack_models.Host.objects.first().ip_manager

    def host_osd_list(self):
        osd_dic = {}
        cm = "ceph osd dump| grep osd | awk '{print $1}' | grep -v max"
        ac = CmmAndRun(
            cmd=cm,
            host=self.ip,
        )

        data = ac.start()
        # pdb.set_trace()

        # 这是一个列表：['osd.0', 'osd.1', 'osd.2', 'osd.3']
        data = data.split('\n')
        for osd in data:
            osd_dic[osd] = {}
            osd_dic[osd]['osd_name'] = osd

            # 获取状态和主机的命令列表
            cmd_list = {
                'status': ("ceph osd dump| grep %s|awk '{print $2}'| \
                grep -v max" % osd),
                'host_ip': ("ceph osd dump| grep %s|awk '{print $14}'| \
                grep -v max |awk -F ':' '{print $1}'" % osd)
            }
            for name, cmd in cmd_list.items():
                # 生成字典
                ac = CmmAndRun(
                    cmd=cmd,
                    host=self.ip,
                )
                data = ac.start()
                if data:
                    osd_dic[osd][name] = data

        for osd, val in osd_dic.items():
            host_id = openstack_models.Host.objects.get(
                ip_storage=val['host_ip']).id
            # 移除该key
            del val['host_ip']

            # 添加foreignKey 的host_id
            osd_dic[osd]['host_id'] = host_id

        return osd_dic

