#!/usr/bin/env python
# coding:utf8


from keystoneclient.v2_0 import client
import pdb
import json
import urllib2
####

from openstack.api.base import KeyStoneBase
from one_finger.models import OpenStackKeystoneAuth
from one_finger.cloud_logging import cloud_logging as logging



###

log = logging.logger


class KeyStone(KeyStoneBase):
    def __init__(self):
        self.admin_obj = OpenStackKeystoneAuth.objects.get(
            os_tenant_name='admin')
        self.username = self.admin_obj.os_username
        self.password = self.admin_obj.os_password
        self.tenant_name = self.admin_obj.os_tenant_name
        self.auth_url = self.admin_obj.auth_url
        self.tenant_id = self.admin_obj.tenant_id
        self.get_token()

    def get_token(self):
        # pdb.set_trace()

        keystone = client.Client(
            username=self.username,
            password=self.password,
            tenant_name=self.tenant_name,
            auth_url=self.auth_url
        )

        # 获取keystone 详细信息
        data = keystone.auth_ref

        if not self.tenant_id:
            self.tenant_id = data['token']['tenant']['id']
            self.admin_obj.tenant_id = self.tenant_id
            self.admin_obj.save()
            # print 'save tenant_id'
        self.token = data['token']['id']
        log.debug(data)
        return self.token

    def endpoint_list(self):
        # endpoint的url
        url = '%s/endpoints' % self.auth_url

        # 包装好json urllib2 会使用它
        request = urllib2.Request(
                url,
                headers={
                    'User-Agent': 'python-keystoneclient',
                    'X-Auth-Token': self.token,
                    })
        data = json.loads(urllib2.urlopen(request, timeout=5).read())
        # print 'check_api', request, data
        debug_info = 'curl -i %s -X POST -H "Content-Type: application/json" ' \
                     '-H "Accept: application/json" ' \
                     '-H "User-Agent: python-novaclient" ' \
                     '-H "X-Auth-Token: TOKEN_REDACTED"' % url

        log.debug(debug_info)
        return data['endpoints']


    def service_list(self):

        url = '%s/OS-KSADM/services' % self.auth_url
        # print url
        request = urllib2.Request(url,
                headers={
                    'User-Agent': 'python-keystoneclient',
                    'X-Auth-Token': self.token,

                    })
        data = json.loads(urllib2.urlopen(request, timeout=5).read())
        # print(data)

        debug_info = 'curl -i %s -X POST -H "Content-Type: application/json" ' \
                     '-H "Accept: application/json" ' \
                     '-H "User-Agent: python-novaclient" ' \
                     '-H "X-Auth-Token: TOKEN_REDACTED"' % url

        log.debug(debug_info)
        return data['OS-KSADM:services']























