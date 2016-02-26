#!/usr/bin/env python
# coding:utf8
#####
from event import base
# from openstack import models


class Osd(base):
    def __init__(self, host_id):
        self.host_id = host_id
        self.event_models = base.Base.event_db_obj

    def osd_down(self, osd_name):
        data = self.parse_data(osd_name, 'down')
        osd_obj = self.event_models(**data)
        osd_obj.save()

    def osd_up(self, osd_name):
        data = self.parse_data(osd_name, 'up')
        osd_obj = self.event_models(**data)
        osd_obj.save()

    def parse_data(self, osd_name, status):
         data = {
            'event_models': 'Ceph',
            'event_content': 'Osd: %s, is %s' % (osd_name, status),
            'event_node_id': self.host_id
         }
         return data


