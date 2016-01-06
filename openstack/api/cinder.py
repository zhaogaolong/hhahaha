#!/usr/bin/env python
# coding:utf8

import urllib2
import json

#####
from openstack.api.base import CinderBase
from openstack import models as openstack_models
from one_finger import models as one_finger_models
from openstack.api import keystone
from one_finger.cloud_logging import cloud_logging as logging
log = logging.logger


class CinderClient(CinderBase):
    def __init__(self):
        self.service_id = one_finger_models.OpenStackKeystoneService.objects.get(name='cinder').service_id
        self.endpoint_obj = one_finger_models.OpenStackKeyStoneEndpoint.objects.get(service_id=self.service_id)
        self.admin_obj = one_finger_models.OpenStackKeystoneAuth.objects.get(os_tenant_name='admin')
        self.service_list_url = (self.endpoint_obj.internalurl % {'tenant_id': self.admin_obj.tenant_id}
                                                                 + '/os-services')

        self.host_list = openstack_models.NovaManagerServiceStatus.objects.all()

    def service_list(self):

        url = self.service_list_url
        kc = keystone.KeyStone()
        token = kc.get_token()
        request = urllib2.Request(url, headers={
                'X-Auth-Project-Id': self.admin_obj.os_username,
                'Accept': 'application/json',
                'User-Agent': 'python-cinderclient',
                'X-Auth-Token': token,

                })

        debug_info = 'curl -i %s ' \
                     '-X POST -H "Content-Type: application/json" ' \
                     '-H "Accept: application/json" ' \
                     '-H "User-Agent: python-novaclient" ' \
                     '-d {"auth": {"tenantName": "admin", ' \
                     '"passwordCredentials": ' \
                     '{"username": admin, "password": "PASSWORD" }' % url
        log.debug(debug_info)
        data = json.loads(urllib2.urlopen(request, timeout=5).read())

        self.save_service_to_db(data)
        return data

    def save_service_to_db(self, data):

        if openstack_models.CinderStatus.objects.filter(name='cinder_status'):
            pass
        else:
            cinder_db_obj = openstack_models.CinderStatus(name='cinder_status')

            if data:
                cinder_db_obj.cinder_api_status = 'up'

            for service in data['services']:
                print '----------->', service

                if service['binary'] == 'cinder-volume':
                    cinder_db_obj.cinder_volume_status = service['state']
                elif service['binary'] == 'cinder-scheduler':
                    cinder_db_obj.cinder_scheduler = service['state']
            cinder_db_obj.save()





    def host_list(self):
        host_manager_ip = {}
        for host in self.host_list:
            host_manager_ip[host.host.hostname]= host.host.ip_manager



    def save_host_status(self):
        pass








