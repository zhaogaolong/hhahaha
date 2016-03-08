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





def down(hostname, service_name):
    check_event_type()
    event_dic = {
        'event_content': '%s host nova service %s status:down' % (
            hostname, service_name),
        'event_type_id': event_models.SecondType.objects.get(
            name='neutron'
        ).id,
        'level': 'ERROR',
        'event_node_id': asset_models.Host.objects.get(hostname=hostname).id
    }
    event_db_obj = event_models.Event(**event_dic)
    event_db_obj.save()


def up(hostname, service_name):
    check_event_type()
    event_dic = {
        'event_content': '%s host nova service %s status:up' % (
            hostname, service_name),
        'event_type_id': event_models.SecondType.objects.get(
            name='neutron'
        ).id,
        'level': 'WARNING',
        'event_node_id': asset_models.Host.objects.get(hostname=hostname).id
    }
    event_db_obj = event_models.Event(**event_dic)
    event_db_obj.save()


def warning(hostname, service_name):
    check_event_type()
    event_dic = {
        'event_content': '%s host nova service %s status:warning' % (
            hostname, service_name),
        'event_type_id': event_models.SecondType.objects.get(
            name='neutron'
        ).id,
        'level': 'WARNING',
        'event_node_id': asset_models.Host.objects.get(hostname=hostname).id
    }
    event_db_obj = event_models.Event(**event_dic)
    event_db_obj.save()


class CloudStatus():
    def __init__(self, service_name, status):
        self.service_name = service_name
        self.status = status

    def up(self):
        data = self.parse_data()
        data['level'] = 'WARNING'
        event_db_obj = event_models.Event(**data)
        event_db_obj.save()

    def down(self):
        data = self.parse_data()
        data['level'] = 'ERROR'
        event_db_obj = event_models.Event(**data)
        event_db_obj.save()

    def warning(self):
        data = self.parse_data()
        data['level'] = 'WARNING'
        event_db_obj = event_models.Event(**data)
        event_db_obj.save()

    def parse_data(self):
        data = {
            'event_content': 'CLOUD Nenutron %s status:%s' % (
                self.service_name, self.status),
            'event_type_id': event_models.SecondType.objects.get(
                name='neutron'
            ).id,
            'level': 'WARNING',
        }
        return data


def neutron_migrate(content):
    check_event_type()
    event_dic = {
        'event_content': content,
        'event_type_id': event_models.SecondType.objects.get(
            name='neutron'
        ).id,
        'level': 'CRITICAL',
    }
    event_keystone_obj = event_models.Event(**event_dic)
    event_keystone_obj.save()
