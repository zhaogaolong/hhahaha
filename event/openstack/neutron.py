#!/usr/bin/env python
# coding:utf8
from event import models as event_models
from asset import models as asset_models


def neutron_info(hostname, content):
    check_event_type()
    event_dic = {
        'event_content': content,
        'event_type_id': event_models.SecondType.objects.get(
            name='neutron'
        ).id,
        'level': 'INFO',
        'event_node_id': asset_models.Host.objects.get(hostname=hostname).id
    }
    event_keystone_obj = event_models.Event(**event_dic)
    event_keystone_obj.save()


def check_event_type():
    if not event_models.TopType.objects.filter(name='openstack'):
        event_models.TopType.objects.create(name='openstack')

    if not event_models.SecondType.objects.filter(name='neutron'):
        event_models.SecondType.objects.create(
            name='neutron',
            top_type_id=event_models.TopType.objects.get(name='openstack').id
        )




