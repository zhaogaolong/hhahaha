#!/usr/bin/env python
# coding:utf8
from openstack import models


class Nova():
    def __init__(self):
        self.nova_obj = models.NovaStatus.objects.first()
        self.nova_mg_obj = models.NovaManagerServiceStatus.objects.all()
        self.nova_cp_obj = models.NovaComputeServiceStatus.objects.all()

    def status(self):
        # 着是给首页的服务使用的
        status_dic = {
            'status': {
                'status': self.nova_obj.status,
                'api': self.nova_obj.nova_api_status,
                'consoleauth': self.nova_obj.nova_consoleauth_status,
                'scheduler': self.nova_obj.nova_scheduler_status,
                'conductor': self.nova_obj.nova_conductor_status,
                'cert': self.nova_obj.nova_cert_status,
                'compute': self.nova_obj.nova_compute_status,
            },
            'manager_node': {},
            'compute_node': {}
        }
        for mg in self.nova_mg_obj:
            manager_hostname = mg.host.hostname.split('.')[0]
            status_dic['manager_node'][manager_hostname] = mg.status

        for compute in self.nova_cp_obj:
            status = compute.nova_compute_status
            compute_name = compute.host.hostname.split('.')[0]
            status_dic['compute_node'][compute_name] = status
        return status_dic