#!/usr/bin/env python
# coding:utf8
from event import models as event_models


def check_event_type():
    if not event_models.TopType.objects.filter(name='ceph'):
        event_models.TopType.objects.create(name='ceph')

    if not event_models.SecondType.objects.filter(name='ceph'):
        event_models.SecondType.objects.create(
            name='ceph',
            top_type_id=event_models.TopType.objects.get(name='ceph').id
        )


def info(content):
    check_event_type()
    event_dic = {
        'event_content': content,
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph').id,
        'level': 'INFO',
    }
    event_keystone_obj = event_models.Event(**event_dic)
    event_keystone_obj.save()


def down():
    check_event_type()
    event_dic = {
        'event_content': 'ceph cluster status: down',
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph').id,
        'level': 'ERROR',
    }

    event_obj = event_models.Event(**event_dic)
    event_obj.save()


def up():
    check_event_type()
    event_dic = {
        'event_content': 'ceph cluster status: up',
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph').id,
        'level': 'WARNING',
    }
    event_obj = event_models.Event(**event_dic)
    event_obj.save()


def warning():
    check_event_type()
    event_dic = {
        'event_content': 'ceph cluster status: warning',
        'event_type_id': event_models.SecondType.objects.get(
            name='ceph').id,
        'level': 'CRITICAL',
    }
    event_obj = event_models.Event(**event_dic)
    event_obj.save()
