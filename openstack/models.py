#!/usr/bin/env python
# coding:utf8
from django.db import models


status_level = (
    ("up", "up"),
    ("warning", "warning"),
    ("down", "down"),
)


mode_status_level = (
        ("up", "up"),
        ("warning", "warning"),
        ("critical", "critical"),
        ("down", "down"),
    )


class CloudStatus(models.Model):
    # 整个openstack状态的总汇状态
    status = models.CharField(choices=mode_status_level, max_length=64)
    available_proportion = models.IntegerField(default=100)

    def __unicode__(self):
        return 'cloud_status:%s ' % self.status


# ####cinder service##########
class CinderStatus(models.Model):
    # 这是cinder全局的状态
    status = models.CharField(choices=mode_status_level,
                              max_length=64,
                              blank=True,
                              null=True)
    cinder_api_status = models.CharField(choices=status_level,
                                         max_length=64,
                                         blank=True,
                                         null=True)
    cinder_volume_status = models.CharField(choices=status_level,
                                            max_length=64,
                                            blank=True,
                                            null=True)
    cinder_scheduler = models.CharField(choices=status_level,
                                        max_length=64,
                                        blank=True,
                                        null=True)

    def __unicode__(self):
        return self.cinder_api_status


class CinderManagerStatus(models.Model):
    host = models.ForeignKey('Host')
    status_level = (
        ('up', "up"),
        ("waring", "waring"),
        ('down ', "down"),
    )
    status = models.CharField(choices=status_level,
                              max_length=64,
                              blank=True,
                              null=True)
    cinder_api_status = models.CharField(choices=status_level,
                                         max_length=64,
                                         blank=True,
                                         null=True )
    cinder_volume = models.CharField(choices=status_level,
                                     max_length=64)
    cinder_scheduler = models.CharField(choices=status_level,
                                        max_length=64)

    def __unicode__(self):
        return self.host.hostname


# ####ceph##########
class CephStatus(models.Model):
    # this is a ceph service tables
    status = models.CharField(choices=mode_status_level, max_length=64)
    monitor_status = models.CharField(choices=status_level, max_length=64)
    osd_status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status


class CephMonitorStatus(models.Model):
    # this is a ceph monitor service tables
    host = models.ForeignKey('Host')
    mon_id = models.IntegerField()
    status = models.CharField(choices=status_level,
                              max_length=64,
                              blank=True,
                              null=True)

    def __unicode__(self):
        return self.host.hostname


class CephOsdStatus(models.Model):
    # this is a ceph osd service tables
    osd_name = models.CharField(max_length=64)
    host = models.ForeignKey('Host')
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.osd_name


# ####nova##########
class NovaStatus(models.Model):
    status = models.CharField(choices=mode_status_level, max_length=64)
    nova_api_status = models.CharField(choices=status_level,
                                       max_length=64,
                                       blank=True,
                                       null=True)
    nova_no_vnc_proxy_status = models.CharField(choices=status_level,
                                                max_length=64,
                                                blank=True, null=True)
    nova_license_status = models.CharField(choices=status_level,
                                           max_length=64,
                                           blank=True, null=True)

    nova_consoleauth_status = models.CharField(choices=status_level,
                                               max_length=64,
                                               blank=True,
                                               null=True)
    nova_scheduler_status = models.CharField(choices=status_level,
                                             max_length=64,
                                             blank=True,
                                             null=True
                                             )
    nova_conductor_status = models.CharField(choices=status_level,
                                             max_length=64,
                                             blank=True,
                                             null=True
                                             )
    nova_cert_status = models.CharField(choices=status_level,
                                        max_length=64,
                                        blank=True,
                                        null=True)

    nova_compute_status = models.CharField(choices=status_level,
                                           max_length=64,
                                           blank=True,
                                           null=True)


    def __unicode__(self):
        return self.status


class NovaManagerServiceStatus(models.Model):
    host = models.ForeignKey('Host')
    status = models.CharField(choices=status_level, max_length=64)
    nova_api_status = models.CharField(choices=status_level,
                                       max_length=64,
                                       blank=True, null=True)
    nova_no_vnc_proxy_status = models.CharField(choices=status_level,
                                                max_length=64,
                                                blank=True, null=True)
    nova_license_status = models.CharField(choices=status_level, max_length=64,
                                           blank=True, null=True)

    nova_consoleauth_status = models.CharField(choices=status_level,
                                               max_length=64)
    enabled_nova_consoleauth = models.BooleanField()

    nova_scheduler_status = models.CharField(choices=status_level,
                                             max_length=64)
    enabled_nova_scheduler = models.BooleanField()

    nova_conductor_status = models.CharField(choices=status_level,
                                             max_length=64)
    enabled_nova_conductor = models.BooleanField()

    nova_cert_status = models.CharField(choices=status_level,
                                        max_length=64)
    enabled_nova_cert = models.BooleanField()

    def __unicode__(self):
        return self.host.hostname


class NovaComputeServiceStatus(models.Model):
    # compute node nova status
    host = models.ForeignKey('Host')
    nova_compute_status = models.CharField(choices=status_level, max_length=64)
    enabled_nova_compute = models.BooleanField()

    def __unicode__(self):
        return self.host.hostname


# ####openstack_mode: rabbitmq##########
class RabbitMqStatus(models.Model):
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.name


class RabbitmqServiceStatus(models.Model):
    host = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.host.name


# ####openstack_mode: Pacemaker##########
class PacemakerStatus(models.Model):
    host = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.host.name


class PacemakerServiceStatus(models.Model):
    host = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.host.name


# ####openstack_mode: redis##########
class RedisStatus(models.Model):
    host = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.host.name


class RedisServiceStatus(models.Model):
    host = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.host.name


# ####openstack_mode: Mysql Service##########
class MysqlStatus(models.Model):
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status


class MysqlServiceStatus(models.Model):
    host = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.mysql_group.name


# ####openstack Neutron##########
class NeutronStatus(models.Model):

    system_river_type_choices = (
        ('Open_vSwitch', "Open_vSwitch"),
        ('Linux_bridge ', "Linux_bridge"),
    )
    status = models.CharField(choices=mode_status_level,
                              max_length=64,
                              blank=True,
                              null=True)

    neutron_compute = models.CharField(choices=status_level,
                                       max_length=64,
                                       blank=True, null=True)

    neutron_river_type = models.CharField(choices=system_river_type_choices,
                                          max_length=64)
    neutron_metadata_agent = models.CharField(choices=status_level,
                                              max_length=64,)
    neutron_lbaas_agent = models.CharField(choices=status_level,
                                           max_length=64)
    neutron_l3_agent = models.CharField(choices=status_level,
                                        max_length=64,
                                        blank=True,
                                        null=True)
    neutron_dhcp_agent = models.CharField(choices=status_level,
                                          max_length=64,
                                          blank=True,
                                          null=True)
    neutron_api_status = models.CharField(choices=status_level,
                                          max_length=64,
                                          blank=True,
                                          null=True,)

    def __unicode__(self):
        return self.status


class NeutronManagerServiceStatus(models.Model):
    host = models.ForeignKey('Host')
    status = models.CharField(choices=status_level,
                              max_length=64,
                              blank=True,
                              null=True,
                              )
    neutron_openvswitch_agent = models.CharField(choices=status_level,
                                                 max_length=64)
    system_river_type_choices = (
        ('Open_vSwitch', "Open_vSwitch"),
        ('Linux_bridge ', "Linux_bridge"),
    )
    neutron_river_type = models.CharField(choices=system_river_type_choices,
                                          max_length=64)
    neutron_metadata_agent = models.CharField(choices=status_level,
                                              max_length=64,)
    neutron_lbaas_agent = models.CharField(choices=status_level,
                                           max_length=64)
    neutron_l3_agent = models.CharField(choices=status_level,
                                        max_length=64,
                                        blank=True,
                                        null=True)
    neutron_dhcp_agent = models.CharField(choices=status_level,
                                          max_length=64,
                                          blank=True,
                                          null=True)
    neutron_api_status = models.CharField(choices=status_level,
                                          max_length=64,
                                          blank=True,
                                          null=True,)
    def __unicode__(self):
        return self.host.hostname


class NeutronComputeServiceStatus(models.Model):
    host = models.ForeignKey('Host')
    neutron_openvswitch_agent = models.CharField(choices=status_level,
                                                 max_length=64)
    # river 是底层模式 ： ovs linux-bridge 等
    # river 的存储模式
    system_river_type_choices = (
        ('Open_vSwitch', "Open_vSwitch"),
        ('Linux_bridge ', "Linux_bridge"),
    )
    neutron_river_type = models.CharField(choices=system_river_type_choices,
                                          max_length=64)

    def __unicode__(self):
        return self.host.hostname


class Host(models.Model):
    hostname = models.CharField(max_length=64)
    host_group = models.ForeignKey('Group', blank=True, null=True)
    ip_manager = models.GenericIPAddressField(max_length=64, blank=True, null=True)
    ip_storage = models.GenericIPAddressField(max_length=64, blank=True, null=True)
    ip_public = models.GenericIPAddressField(max_length=64, blank=True, null=True)
    ip_pxe = models.GenericIPAddressField(max_length=64, blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    # password = models.CharField(max_length=64, blank=True, null=True)

    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64, blank=True, null=True)

    def __unicode__(self):
        return self.hostname


class Group(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name










