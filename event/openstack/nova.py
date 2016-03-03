#!/usr/bin/env python
# coding:utf8
from event import models as event_models
from asset import models as asset_models


def check_event_type():
    if not event_models.TopType.objects.filter(name='openstack'):
        event_models.TopType.objects.create(name='openstack')

    if not event_models.SecondType.objects.filter(name='nova'):
        event_models.SecondType.objects.create(
            name='nova',
            top_type_id=event_models.TopType.objects.get(name='openstack').id
        )


def nova_info(hostname, content):
    check_event_type()
    event_dic = {
        'event_content': content,
        'event_type_id': event_models.SecondType.objects.get(
            name='nova'
        ).id,
        'level': 'INFO',
        'event_node_id': asset_models.Host.objects.get(hostname=hostname).id
    }
    event_keystone_obj = event_models.Event(**event_dic)
    event_keystone_obj.save()





