#!/usr/bin/env python
# coding:utf8

from django.db import models


class OpenStackKeystoneAuth(models.Model):
    os_no_cache = models.BooleanField(default=True)
    os_tenant_name = models.CharField(max_length=64, default='admin')
    os_username = models.CharField(max_length=64, default='admin')
    os_password = models.CharField(max_length=64, default='admin')
    auth_url = models.URLField()
    os_auth_strategy = models.CharField(max_length=64, default='keystone')
    cinder_endpoint_type = models.CharField(max_length=64, default='publicURL')
    glance_endpoint_type = models.CharField(max_length=64, default='publicURL')
    keystone_endpoint_type = models.CharField(max_length=64, default='publicURL')
    nova_endpoint_type = models.CharField(max_length=64, default='publicURL')
    neutron_endpoint_type = models.CharField(max_length=64, default='publicURL')
    token = models.CharField(max_length=64, blank=True, null=True)
    tenant_id = models.CharField(max_length=64, blank=True, null=True)

    def __unicode__(self):
        return self.os_tenant_name


class OpenStackKeyStoneEndpoint(models.Model):
    endpoint_id = models.CharField(max_length=64)
    service_id = models.CharField(max_length=64)
    region = models.CharField(max_length=64)
    public_url =  models.CharField(max_length=64)
    internal_url =  models.CharField(max_length=64)
    admin_url =  models.CharField(max_length=64)
    enabled = models.BooleanField()

    def __unicode__(self):
        return self.public_url


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

