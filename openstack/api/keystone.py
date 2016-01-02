#!/usr/bin/env python
# coding:utf8


from keystoneclient import client
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
        admin_obj = OpenStackKeystoneAuth.objects.get(os_tenant_name='admin')
        self.username = admin_obj.os_username
        self.password = admin_obj.os_password
        self.tenant_name = admin_obj.os_tenant_name
        self.auth_url = admin_obj.auth_url
        # print self.auth_url
        self.tenant_id = admin_obj.tenant_id
        self.get_token()

    def get_token(self):

        # 获取token的url
        # print
        token_url = '%s/tokens' % self.auth_url

        # 包装好json urllib2 会使用它
        data = json.dumps({
            'auth':{
               'tenantName': self.tenant_name,
                'passwordCredentials':{
                    'username': self.username,
                    'password': self.password,
                }
            }
        })

        if token_url:

            # 包装好request对象
            request = urllib2.Request(
                 token_url,
                 data=data,
                 headers={'Content-type': 'application/json'}
            )

            # 获取返回的数据以字典的形式展示
            data = json.loads(urllib2.urlopen(request, timeout=5).read())

            # 获取 token
            self.token = data['access']['token']['id']

            # 获取admin的tenant_id
            if not self.tenant_id:
                self.tenant_id = data['access']['token']['tenant']['id']

                self.admin_obj.update(tenant_id=self.tenant_id)
                # print 'save tenant_id'

        debug_info = 'curl -i %s -X POST -H "Content-Type: application/json" ' \
                     '-H "Accept: application/json" ' \
                     '-H "User-Agent: python-novaclient" ' \
                     '-d ' \
                     '{"auth": ' \
                     '{"tenantName": "admin", ' \
                     '"passwordCredentials": ' \
                     '{"username": %s, "password": "password" }}}' % (token_url, self.username)

        log.debug(debug_info)
        return self.token

    def endpoint_list(self):
        self.get_token()

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























