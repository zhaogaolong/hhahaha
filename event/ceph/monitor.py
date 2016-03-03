#!/usr/bin/env python
# coding:utf8
#####
# from event import base
# from asset import models


# class Monitor(base):
#     def __init__(self, host_id):
#         self.host_id = host_id
#         self.event_models = base.Base.event_db_obj
#
#     def monitor_down(self, ):
#         data = self.parse_data('down')
#         osd_obj = self.event_models(**data)
#         osd_obj.save()
#
#     def monitor_up(self):
#         data = self.parse_data('up')
#         osd_obj = self.event_models(**data)
#         osd_obj.save()
#
#     def parse_data(self, status):
#         host_name = models.Host.objects.get(id=self.host_id).hostname
#         data = {
#            'event_models': 'Ceph',
#            'event_content': 'Ceph Monitor: %s, is %s' % (host_name, status),
#            'event_node_id': self.host_id
#         }
#         return data

from event import models as event_models
from asset import models as asset_models


def check_event_type():
    if not event_models.TopType.objects.filter(name='ceph'):
        event_models.TopType.objects.create(name='ceph')

    if not event_models.SecondType.objects.filter(name='ceph_mon'):
        event_models.SecondType.objects.create(
            name='ceph_mon',
            top_type_id=event_models.TopType.objects.get(name='ceph').id
        )


def ceph_mon_info(hostname, content):
    check_event_type()
    event_dic = {
        'event_content': content,
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph_mon').id,
        'level': 'INFO',
        'event_node_id': asset_models.Host.objects.get(hostname=hostname).id
    }
    event_keystone_obj = event_models.Event(**event_dic)
    event_keystone_obj.save()


def down(hostname=None):

    event_dic = {
        'event_content': 'ceph monitor status: down',
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph_mon').id,
        'level': 'ERROR',
    }

    if hostname:
        event_dic['event_node_id'] = \
            asset_models.Host.objects.get(hostname=hostname).id
        event_dic['event_content'] = '%s ceph monitor status: down' % hostname

    event_obj = event_models.Event(**event_dic)
    event_obj.save()


def up(hostname=None):
    event_dic = {
        'event_content': 'ceph monitor status: up',
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph_mon').id,
        'level': 'WARNING',
    }
    if hostname:
        event_dic['event_node_id'] = \
            asset_models.Host.objects.get(hostname=hostname).id
        event_dic['event_content'] = '%s ceph monitor status: up' % hostname
    event_obj = event_models.Event(**event_dic)
    event_obj.save()


def warning():
    event_dic = {
        'event_content': 'ceph monitor status: warning',
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph_mon').id,
        'level': 'CRITICAL',
    }
    event_obj = event_models.Event(**event_dic)
    event_obj.save()

