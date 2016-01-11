#!/usr/bin/env python
# coding:utf8
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    friends = models.ManyToManyField('self', blank=True,related_name='my_friends')
    def __unicode__(self):
        return self.name






class OpenStackKeystoneAuth(models.Model):
    os_no_cache = models.BooleanField(default=True)
    os_tenant_name = models.CharField(max_length=64, default='admin')
    os_username = models.CharField(max_length=64, default='admin')
    os_password = models.CharField(max_length=64, default='admin')
    auth_url = models.URLField()
    os_auth_strategy = models.CharField(max_length=64, default='keystone')
    cinder_endpoint_type = models.CharField(max_length=64,
                                            default=settings.ACCEPT_URL)
    glance_endpoint_type = models.CharField(max_length=64,
                                            default=settings.ACCEPT_URL)
    keystone_endpoint_type = models.CharField(max_length=64,
                                              default=settings.ACCEPT_URL)
    nova_endpoint_type = models.CharField(max_length=64,
                                          default=settings.ACCEPT_URL)
    neutron_endpoint_type = models.CharField(max_length=64,
                                             default=settings.ACCEPT_URL)
    token = models.CharField(max_length=64, blank=True, null=True)
    tenant_id = models.CharField(max_length=64, blank=True, null=True)

    def __unicode__(self):
        return self.os_tenant_name


class OpenStackKeyStoneEndpoint(models.Model):
    endpoint_id = models.CharField(max_length=64)
    service_id = models.CharField(max_length=64)
    region = models.CharField(max_length=64)
    publicurl =  models.CharField(max_length=64)
    internalurl =  models.CharField(max_length=64)
    adminurl =  models.CharField(max_length=64)
    enabled = models.BooleanField()

    def __unicode__(self):
        return self.publicurl


class OpenStackKeystoneService(models.Model):
    service_id = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    enabled = models.BooleanField()

    def __unicode__(self):
        return self.name


class ServiceStatusUrlSuffix(models.Model):
    service_name = models.CharField(max_length=64)
    api = models.CharField(max_length=64)
    service = models.CharField(max_length=64)
    token = models.CharField(max_length=64, blank=True, null=True)
    endpoint = models.CharField(max_length=64, blank=True, null=True)

    def __unicode__(self):
        return self.service_name

