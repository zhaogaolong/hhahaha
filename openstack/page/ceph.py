#!/usr/bin/env python
# coding:utf8

from openstack import models

class Ceph():
    def __init__(self):
        self.ceph_obj = models.CephStatus.objects.first()

    def status(self):
        status_dic = {
            'status': self.ceph_obj.status,
            'monitor': self.ceph_obj.monitor_status,
            'osd': self.ceph_obj.osd_status,
        }
        return status_dic