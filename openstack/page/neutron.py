#!/usr/bin/env python
# coding:utf8
from openstack import models
from one_finger import settings

class Neutron():
    def __init__(self):
        self.neutron_obj = models.NeutronStatus.objects.first()
        self.neutron_mg_obj = models.NeutronManagerServiceStatus.objects.all()
        self.neutron_cp_obj = models.NeutronComputeServiceStatus.objects.all()

    def status(self):
        status_dic = {
            'status': {
                'status': self.neutron_obj.status,
                'api': self.neutron_obj.neutron_api_status,
                'metadata': self.neutron_obj.neutron_metadata_agent,
                'lbaas': self.neutron_obj.neutron_lbaas_agent,
                'l3': self.neutron_obj.neutron_l3_agent,
                'dhcp': self.neutron_obj.neutron_dhcp_agent,
                'agent': self.neutron_obj.neutron_river_type,
                'compute': self.neutron_obj.neutron_compute
            },
            'manager_node': {},
            'compute_node': {}
        }
        for mg in self.neutron_mg_obj:
            manager_hostname = mg.host.hostname.split('.')[0]
            status_dic['manager_node'][manager_hostname] = mg.status

        for compute in self.neutron_cp_obj:
            status = getattr(compute, settings.NEUTRON_RIVER_TYPE)
            compute_name = compute.host.hostname.split('.')[0]
            status_dic['compute_node'][compute_name] = status
        return status_dic





