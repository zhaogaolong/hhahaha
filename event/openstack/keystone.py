#!/usr/bin/env python
# coding:utf8
from event import models as event_models


def add_keystone_info(content_type, content, level):
    check_event_type()
    event_dic = {
        'event_content': content,
        'event_type_id': event_models.SecondType.objects.get(
            name=content_type
        ).id,
        'level': level
    }
    event_keystone_obj = event_models.Event(**event_dic)
    event_keystone_obj.save()


def check_event_type():
    if not event_models.TopType.objects.filter(name='openstack'):
        event_models.TopType.objects.create(name='openstack')

    if not event_models.SecondType.objects.filter(name='keystone'):
        event_models.SecondType.objects.create(
            name='keystone',
            top_type_id=event_models.TopType.objects.get(name='openstack').id
        )




