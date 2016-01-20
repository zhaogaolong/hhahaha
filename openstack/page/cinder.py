#!/usr/bin/env python
# coding:utf8

from openstack import models


class Cinder():
    def __init__(self):
        self.cinder_obj = models.CinderStatus.objects.first()

    def status(self):
        status_dic = {
            'status': self.cinder_obj.status,
            'api': self.cinder_obj.cinder_api_status,
            'volume': self.cinder_obj.cinder_volume,
            'scheduler': self.cinder_obj.cinder_scheduler
        }
        return status_dic
