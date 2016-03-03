#!/usr/bin/env python
# coding:utf8
from django.db import models
from asset import models as asset_models
# Create your models here.

event_type_choices = (
    ('ceph', 'ceph'),
    ('openstack', "openstack"),
    ('mysql', "mysql"),
    ('pacemaker', "pacemaker"),
    ('rabbitmq', "rabbitmq"),
)


class Event(models.Model):
    event_time = models.DateTimeField(auto_now_add=True)
    event_content = models.CharField(max_length=2048)

    # 每个事件绑定主机可选
    event_node = models.ForeignKey(asset_models.Host,
                                   null=True, blank=True
                                   )
    event_type = models.ForeignKey('SecondType', null=True, blank=True)
    level = models.CharField(max_length=64)

    def __unicode__(self):
        return self.event_content


class TopType(models.Model):
    name = models.CharField(choices=event_type_choices,
                            max_length=1024)

    def __unicode__(self):
        return self.name


class SecondType(models.Model):
    top_type = models.ForeignKey('TopType', blank=True, null=True)
    name = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name

