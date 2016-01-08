#!/usr/bin/env python
# coding:utf8
from openstack import models


class Nova():
    def __init__(self):
        self.nova_obj = models.NovaStatus.objects.first()

    def status(self):
        status_dic = {
            'status': self.nova_obj.status,
            'api': self.nova_obj.nova_api_status,
            'consoleauth': self.nova_obj.nova_consoleauth_status,
            'scheduler': self.nova_obj.nova_scheduler_status,
            'conductor': self.nova_obj.nova_conductor_status,
            'cert': self.nova_obj.nova_cert_status,
            'compute': self.nova_obj.nova_compute_status,
        }

        return status_dic