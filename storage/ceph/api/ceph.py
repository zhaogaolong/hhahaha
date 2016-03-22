# /usr/bin/env python
# coding:utf8
import pdb
import json
###
from openstack import models as openstack_models
from asset import models as asset_models
from storage import models as storage_models
from openstack.api.opentack_ansible import CmmAndRun


class Ceph():
    def __init__(self):
        self.ip = asset_models.Host.objects.first().ip_manager

    def osd_list(self):
        osd_dic = {}
        cm = "ceph osd dump| grep -v max_osd | grep osd | " \
             "awk '{print $1,$2,$14}'"
        # pdb.set_trace()
        ac = CmmAndRun(
            cmd=cm,
            host=self.ip,
        )
        data = ac.start()
        # pdb.set_trace()

        data = data.split('\n')
        # 这是一个列表：['osd.0 up', 'osd.1 down', 'osd.2 up', 'osd.3 up']
        for item in data:
            item = item.split()
            osd_dic[item[0]] = {
                'osd_name': item[0],
                'status': item[1],
                'host_id': asset_models.Host.objects.get(
                    ip_storage=item[2].split(':')[0]
                ).id
            }

        return osd_dic

    def mon_list(self):
        mon_dic = {}
        cm = "ceph mon_status"
        print 'ceph_cmd_ip:', self.ip

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

    def quorum_online(self):

        cmd = "ceph mon_status"
        ac = CmmAndRun(
            cmd=cmd,
            host=self.ip,
        )
        # import pdb
        # pdb.set_trace()
        data = ac.start()
        data = json.loads(data)

        if data:
            return data['quorum']
        else:
            None

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

        mon_obj = storage_models.CephMonitorStatus.objects.all()
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