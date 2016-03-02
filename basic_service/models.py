from django.db import models
from asset.models import Host
# Create your models here.


status_level = (
    ('Ok', "ok"),
    ('Warning ', "Warning"),
    ('Error ', "Error"),
)


# ####openstack_mode: rabbitmq##########
class RabbitMqStatus(models.Model):
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status


class RabbitmqServiceStatus(models.Model):
    host = models.ForeignKey(Host)
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status


# ####openstack_mode: Pacemaker##########
class PacemakerStatus(models.Model):
    host = models.ForeignKey(Host)
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status


class PacemakerServiceStatus(models.Model):
    host = models.ForeignKey(Host)
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status


# ####openstack_mode: redis##########
class RedisStatus(models.Model):
    host = models.ForeignKey(Host)
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status


class RedisServiceStatus(models.Model):
    host = models.ForeignKey(Host)
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status


# ####openstack_mode: Mysql Service##########
class MysqlStatus(models.Model):
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status


class MysqlServiceStatus(models.Model):
    host = models.ForeignKey(Host)
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status
