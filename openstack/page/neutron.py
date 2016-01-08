#!/usr/bin/env python
# coding:utf8
from openstack import models


class Neutron():
    def __init__(self):
        self.neutron_obj = models.NeutronStatus.objects.first()

    def status(self):
        status_dic = {
            'status': self.neutron_obj.status,
            'api': self.neutron_obj.neutron_api_status,
            'metadata': self.neutron_obj.neutron_metadata_status,
            'lbaas': self.neutron_obj.neutron_lbaas_status,
            'l3': self.neutron_obj.neutron_l3_status,
            'dhcp': self.neutron_obj.neutron_dhcp_status,
            'agent': self.neutron_obj.neutron_openvswitch_agent,
            'compute': self.neutron_obj.neutron_compute
        }

        return status_dic

