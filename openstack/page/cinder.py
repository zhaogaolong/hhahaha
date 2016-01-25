#!/usr/bin/env python
# coding:utf8

from openstack import models


class Cinder():
    def __init__(self):
        self.cinder_obj = models.CinderStatus.objects.first()
        self.cinder_mg_obj = models.CinderManagerStatus.objects.all()

    def status(self):
        status_dic = {
            'status': {
                'status': self.cinder_obj.status,
                'api': self.cinder_obj.cinder_api_status,
                'volume': self.cinder_obj.cinder_volume,
                'scheduler': self.cinder_obj.cinder_scheduler
            },
            'manager_node': {},
        }
        for mg in self.cinder_mg_obj:
            manager_hostname = mg.host.hostname.split('.')[0]
            # status_dic['manager_node'][manager_hostname] = mg.status
            status_dic['manager_node'][manager_hostname] = 'up'
        return status_dic
