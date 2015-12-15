#!/usr/bin/env python
# coding:utf8
# 获取平台信息
# import time
import urllib2
# import sys
# #import simplejson as json
# import json
# import ConfigParser
# import logging

from one_finger import models as one_finger_models

class token():
    def __init__(self):
        self.username = one_finger_models.Openstack_keystone_auth.os_tenant_name
        self.password = one_finger_models.Openstack_keystone_auth.os_password
        self.tenant_name = one_finger_models.Openstack_keystone_auth.os_tenant_name
        self.endpoint_keystone = one_finger_models.Openstack_keystone_auth.auth_url
        self.token = one_finger_models.Openstack_keystone_auth.token
        self.tenant_id = one_finger_models.Openstack_keystone_auth.tenant_id

        print self.username
        print self.password
        print self.tenant_name
        print self.endpoint_keystone
        print self.token
        print self.tenant_id


    def get_token(self):
        data = {
            "auth":{
               'tenantName': self.tenant_name,
                'passwordCredentials':{
                    'username': self.username,
                    'password': self.password,
                }
            }
        }
        if self.endpoint_keystone:
            request = urllib2.Request(
                 self.endpoint_keystone,
                 data=data,
                 headers={
                     'Content-type': 'application/json'
                 }
            )

            print urllib2.urlopen(request, timeout=self.get_timeout('keystone')).read()




class service():
    pass

class save_service_db():
    pass


if __name__ == '__main__':
    a = token()