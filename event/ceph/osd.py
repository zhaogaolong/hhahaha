#!/usr/bin/env python
# coding:utf8
from event import models as event_models
from asset import models as asset_models
from alarm import engine


def check_event_type():
    if not event_models.TopType.objects.filter(name='ceph'):
        event_models.TopType.objects.create(name='ceph')

    if not event_models.SecondType.objects.filter(name='ceph_osd'):
        event_models.SecondType.objects.create(
            name='ceph_osd',
            top_type_id=event_models.TopType.objects.get(name='ceph').id
        )


def osd_info(hostname, content):
    check_event_type()
    event_dic = {
        'event_content': content,
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph_osd').id,
        'level': 'INFO',
        'event_node_id': asset_models.Host.objects.get(hostname=hostname).id
    }
    event_keystone_obj = event_models.Event(**event_dic)
    event_keystone_obj.save()


def down(hostname=None):
    event_dic = {
        'event_content': 'ceph osd status: down',
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph_osd').id,
        'level': 'ERROR',
    }

    if hostname:
        event_dic['event_node_id'] = \
            asset_models.Host.objects.get(hostname=hostname).id
        event_dic['event_content'] = '%s ceph osd status: down' % hostname

    event_obj = event_models.Event(**event_dic)
    event_obj.save()
    al = engine.alarm_type()
    al(event_obj.id, 'down')


def up(hostname=None):
    event_dic = {
        'event_content': 'ceph osd status: up',
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph_osd').id,
        'level': 'WARNING',
    }
    if hostname:
        event_dic['event_node_id'] = \
            asset_models.Host.objects.get(hostname=hostname).id
        event_dic['event_content'] = '%s ceph osd status: up' % hostname

    event_obj = event_models.Event(**event_dic)
    event_obj.save()
    al = engine.alarm_type()
    al(event_obj.id, 'up')
