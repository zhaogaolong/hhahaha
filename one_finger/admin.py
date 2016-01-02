#!/usr/bin/env python
# coding:utf8

from django.contrib import admin
from one_finger import models


admin.site.register(models.OpenStackKeystoneAuth)
admin.site.register(models.OpenStackKeyStoneEndpoint)
admin.site.register(models.ServiceStatusUrlSuffix)
admin.site.register(models.OpenStackKeystoneService)

