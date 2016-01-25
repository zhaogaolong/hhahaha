#!/usr/bin/env python
# coding:utf8

from openstack import models

class Ceph():
    def __init__(self):
        self.ceph_obj = models.CephStatus.objects.first()
        self.ceph_mon_obj = models.CephMonitorStatus.objects.all()
        self.ceph_osd_obj = models.CephOsdStatus.objects.all()

    def status(self):
        status_dic = {
            'status':{
                'status': self.ceph_obj.status,
                'monitor': self.ceph_obj.monitor_status,
                'osd': self.ceph_obj.osd_status,
            },
            'mon_node': {},
            'osd_node': {},
        }

        for mon in self.ceph_mon_obj:
            manager_hostname = mon.host.hostname.split('.')[0]
            status_dic['mon_node'][manager_hostname] = mon.status

        for osd in self.ceph_osd_obj:
            osd_hostname = osd.host.hostname.split('.')[0]
            status_dic['osd_node'][osd_hostname] = osd.status
        return status_dic