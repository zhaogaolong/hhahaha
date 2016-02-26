#!/usr/bin/env python
# coding:utf8
#####
from event import base
from openstack import models


class Monitor(base):
    def __init__(self, host_id):
        self.host_id = host_id
        self.event_models = base.Base.event_db_obj

    def monitor_down(self, ):
        data = self.parse_data('down')
        osd_obj = self.event_models(**data)
        osd_obj.save()

    def monitor_up(self):
        data = self.parse_data('up')
        osd_obj = self.event_models(**data)
        osd_obj.save()

    def parse_data(self, status):
        host_name = models.Host.objects.get(id=self.host_id).hostname
        data = {
           'event_models': 'Ceph',
           'event_content': 'Ceph Monitor: %s, is %s' % (host_name, status),
           'event_node_id': self.host_id
        }
        return data

