from django.db import models
from asset import models as asset_models
# Create your models here.

event_type_choices = (
    ('ceph', 'ceph'),
    ('openstack', "openstack"),
    ('mysql', "mysql"),
    ('pacemaker', "openstack"),
    ('rabbitmq', "openstack"),
    ('rabbitmq', "openstack"),
)


class Event(models.Model):
    event_time = models.DateTimeField(auto_now_add=True)
    event_content = models.CharField(max_length=2048)
    event_node = models.ForeignKey(asset_models.Host,
                                   null=True, blank=True
                                   )


class TopType(models.Model):
    event = models.ForeignKey('Event')
    name = models.CharField(choices=event_type_choices,
                            max_length=1024)


class SecondType(models.Model):
    top_type = models.ForeignKey('TopType', blank=True, null=True)
    name = models.CharField(max_length=1024)




























