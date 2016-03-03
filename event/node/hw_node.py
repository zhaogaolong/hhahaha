#!/usr/bin/env python
# coding:utf8

from event import models as event_models
from asset import models as asset_models


def node_info(hostname, content):
    check_event_type()
    event_dic = {
       'event_content': content,
       'event_type_id': event_models.SecondType.objects.get(
          name='HW_Node'
       ).id,
       'level': 'INFO',
       'event_node_id': asset_models.Host.objects.get(hostname=hostname).id
    }

    event_node_info_obj = event_models.Event(**event_dic)
    event_node_info_obj.save()


def check_event_type():
    if not event_models.TopType.objects.filter(name='node'):
        event_models.TopType.objects.create(name='node')

    if not event_models.SecondType.objects.filter(name='HW_Node'):
        event_models.SecondType.objects.create(
            name='HW_Node',
            top_type_id=event_models.TopType.objects.get(name='node').id
        )
