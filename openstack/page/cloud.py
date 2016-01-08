#!/usr/bin/env python
# coding:utf8

import json

####

from openstack import models as openstack_models

class Cloud():
    def __init__(self):
        self.cloud_obj = openstack_models.CloudStatus.objects.first()

    def status(self):
        status_dic = {
            'status': self.cloud_obj.status,
            'proportion': self.cloud_obj.available_proportion
        }

        return status_dic