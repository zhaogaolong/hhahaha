#!/usr/bin/env python
# coding:utf8
###
from openstack import models as openstack_models
from opentack_ansible import CmmAndRun


class Ceph():
    def __init__(self,):
        self.hostname = openstack_models.Host.objects.first().hostname

    def host_osd_list(self):
        cm = "ceph osd dump|grep osd.|awk '{print $1" " $2" " $14}'|grep -v max"
        ac = CmmAndRun(
            cmd=cm,
            host=self.hostname
        )
        data = ac.start()
        return data