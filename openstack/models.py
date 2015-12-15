#!/usr/bin/env python
# coding:utf8

from django.db import models




class Openstack_keystone_service_list(models.Model):
    service_id = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    description = models.CharField(max_length=100)










class Openstack_status(models.Model):
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)
    available_proportion = models.IntegerField(default=100)



class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip_manager = models.GenericIPAddressField()
    ip_storage = models.GenericIPAddressField()
    ip_public = models.GenericIPAddressField(blank=True, null=True)
    ip_pxe = models.GenericIPAddressField()
    group = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.hostname

class Group(models.Model):
    name = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name

# ####ceph##########
# this is a ceph osd service tables
class Ceph_osd_service_status(models.Model):

    osd_name = models.CharField(max_length=64)
    osd_host = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.osd_name

# this is a ceph monitor service tables
class Ceph_monitor_service_status(models.Model):

    monitor_host = models.ForeignKey('Group')
    status = models.IntegerField()
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.monitor_host.name

class Ceph_monitor_node_service_status(models.Model):
    monitor_host = models.ForeignKey('Host')
    status = models.IntegerField()
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.monitor_host.name

# ####openstack_mode: rabbitmq##########
class Rabbitmq_service_status(models.Model):
    rabbitmq_group = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)


    def __unicode__(self):
        return self.rabbitmq_group.name
class Rabbitmq_node_service_status(models.Model):
    rabbitmq_group = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.rabbitmq_group.name

# ####openstack_mode: pa##########
class Pacemaker_service_status(models.Model):
    rabbitmq_group = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.rabbitmq_group.name

class Pacemaker_node_service_status(models.Model):
    rabbitmq_group = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.rabbitmq_group.name

# ####openstack_mode: redis##########
class Redis_service_status(models.Model):
    redis_group = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.redis_group.name

class Redis_node_service_status(models.Model):
    redis_group = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.redis_group.name

class Mysql_service_status(models.Model):
    # version = models.CharField(max_length=64)
    mysql_group = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.mysql_group.name


class Mysql_node_service_status(models.Model):
    # version = models.CharField(max_length=64)
    mysql_group = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.mysql_group.name

# ####openstack_nova_manager##########
class Nova_manager_service_status(models.Model):
    group_name = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)
    nova_api_status = models.CharField(choices=status_level, max_length=64)
    nova_novncproxy_status = models.CharField(choices=status_level, max_length=64)
    nova_consoleauth_status = models.CharField(choices=status_level, max_length=64)
    nova_scheduler_status = models.CharField(choices=status_level, max_length=64)
    nova_conductor_status = models.CharField(choices=status_level, max_length=64)
    nova_license_status = models.CharField(choices=status_level, max_length=64)
    def __unicode__(self):
        return self.status

#
class Nova_manager_node_service_status(models.Model):
    group_name = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)
    nova_api_status = models.CharField(choices=status_level, max_length=64)
    nova_novncproxy_status = models.CharField(choices=status_level, max_length=64)
    nova_consoleauth_status = models.CharField(choices=status_level, max_length=64)
    nova_scheduler_status = models.CharField(choices=status_level, max_length=64)
    nova_conductor_status = models.CharField(choices=status_level, max_length=64)
    nova_license_status = models.CharField(choices=status_level, max_length=64)
    def __unicode__(self):
        return self.status

# ####openstack_nova_compute##########
class Nova_compute_service_status(models.Model):
    group_name = models.ForeignKey('Group')
    group_name = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)
    libvirtd_staus = models.CharField(choices=status_level, max_length=64)
    def __unicode__(self):
        return self.status



# ####openstack_cinder_manange # 整个组的状态##########
class cinder_minager_service_status(models.Model):
    group_name = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)
    cinder_api_status = models.CharField(choices=status_level, max_length=64)
    cinder_volume_status = models.CharField(choices=status_level, max_length=64)
    cinder_scheduler_status = models.CharField(choices=status_level, max_length=64)
    def __unicode__(self):
        return self.status

# 每一台的状态
class cinder_node_service_status(models.Model):
    group_name = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)
    cinder_api_status = models.CharField(choices=status_level, max_length=64)
    cinder_volume_status = models.CharField(choices=status_level, max_length=64)
    cinder_scheduler_status = models.CharField(choices=status_level, max_length=64)
    def __unicode__(self):
        return self.status

# ####openstack_cinder_manange##########
#
class Neutron_manager_service_status(models.Model):
    group_name = models.ForeignKey('Group')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)
    neutron_api_status = models.CharField(choices=status_level, max_length=64)
    neutron_network_status = models.CharField(choices=status_level, max_length=64)
    neutron_metadata_status = models.CharField(choices=status_level, max_length=64)
    neutron_Loadbalancer_status = models.CharField(choices=status_level, max_length=64)
    neutron_l3_status =models.CharField(choices=status_level, max_length=64)
    neutron_DHCP_status = models.CharField(choices=status_level, max_length=64)
    neutron_river_status = models.CharField(choices=status_level, max_length=64)
    cinder_scheduler_status = models.CharField(choices=status_level, max_length=64)
    def __unicode__(self):
        return self.status

class Neutron_manager_node_service_status(models.Model):
    group_name = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)
    neutron_api_status = models.CharField(choices=status_level, max_length=64)
    neutron_network_status = models.CharField(choices=status_level, max_length=64)
    neutron_metadata_status = models.CharField(choices=status_level, max_length=64)
    neutron_Loadbalancer_status = models.IntegerField(blank=True, null=True)
    neutron_l3_status =models.CharField(choices=status_level, max_length=64, blank=True, null=True)
    neutron_DHCP_status = models.CharField(choices=status_level, max_length=64,  blank=True, null=True)
    neutron_river_status = models.CharField(choices=status_level, max_length=64)
    cinder_scheduler_status = models.CharField(choices=status_level, max_length=64)
    def __unicode__(self):
        return self.status

class Neutron_compute_service_status(models.Model):
    host_name = models.ForeignKey('Host')
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64)
    # river 是底层模式 ： ovs linux-bridge 等
    # river 的存储模式
    system_river_type_choices = (
        ('Open_vSwitch',"Open_vSwitch"),
        ('Linux_bridge ', "Linux_bridge"),
    )
    neutron_river_type = models.CharField(choices=system_river_type_choices,max_length=64)
    # neutron_river_status = models.IntegerField()
    def __unicode__(self):
        return self.status














