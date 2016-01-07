#!/usr/bin/env python
# coding:utf8

#import pdb
import json
###
from openstack import models as openstack_models
from opentack_ansible import CmmAndRun


class Ceph():
    def __init__(self,):
        self.ip = openstack_models.Host.objects.first().ip_manager

    def osd_list(self):
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

    def mon_list(self):
        mon_dic = {}
        cm = "ceph mon_status"
        ac = CmmAndRun(
            cmd=cm,
            host=self.ip,
        )
        data = json.loads(ac.start())
        # print data
        if data:
            for mon in data['monmap']['mons']:
                # print mon

                mon_id = mon['rank']
                mon_ip = mon['addr'].split(':')[0]

                mon_dic[mon_ip] = {'id': mon_id}

        return mon_dic

    def check_mon(self):
        # 使用ceph -s 中有一个选项是 quorum, 着就是提示有多少个mon up的
        # 通过ceph mon dump 查看mon的ID

        # 获取ceph quorum 的ID
        cm = "ceph -s |grep quorum |awk '{print $11}'"
        ac = CmmAndRun(
            cmd=cm,
            host=self.ip,
        )
        quorum = ac.start()
        if len(quorum)>1:
            quorum = quorum.split(',')

        mon_obj = openstack_models.CephMonitorStatus.objects.all()
        for mon in mon_obj:
            if mon.id in quorum:
                mon.status = 'up'
            else:
                mon.status = 'down'

    def check_osd(self):
        cm = "ceph osd dump| grep osd | awk '{print $1" "$2}' |\
         grep -v max |grep down"
        ac = CmmAndRun(
            cmd=cm,
            host=self.ip,
        )

        data = ac.start()
        if 'down' in data:
            pass

