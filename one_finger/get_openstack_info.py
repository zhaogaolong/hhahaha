#!/usr/bin/env python
# coding:utf8
# 获取平台信息
# import time
import urllib2
import sys
# #import simplejson as json
import json
# import ConfigParser
# import logging

# from one_finger import models as one_finger_models


from one_finger import models as one_finger_models

class token():
    def __init__(self):
        # 实例化存储对象
        self.admin_obj = one_finger_models.OpenStackKeystoneAuth.objects.filter(os_tenant_name='admin')

        self.service_suffix_obj = one_finger_models.ServiceStatusUrlSuffix.objects.all()
        self.keystone_obj = self.service_suffix_obj.filter(service_name='keystone')


        # print self.admin_obj.values()

        # 这是数据结构:[{'os_username': u'admin'}]
        self.username = self.admin_obj.values('os_username')[0]['os_username']
        self.password = self.admin_obj.values('os_password')[0]['os_password']
        self.tenant_name = self.admin_obj.values('os_tenant_name')[0]['os_tenant_name']
        self.auth_url = self.admin_obj.values('auth_url')[0]['auth_url']
        self.token = self.admin_obj.values('token')[0]['token']
        self.tenant_id = self.admin_obj.values('tenant_id')[0]['tenant_id']
        self.get_token()

        # print self.username
        # print self.password
        # print self.tenant_name
        # print 'url:', self.auth_url
        # print self.token
        # print self.tenant_id


    def get_token(self):
        # print dir(self.keystone_obj)
        # token_url = self.keystone_obj.values('token')[0]['token']
        token_url = self.keystone_obj.values('token')
        print 'tokenurl', token_url
        # print 'token_url:',token_url
        data = json.dumps({
            "auth":{
               'tenantName': self.tenant_name,
                'passwordCredentials':{
                    'username': self.username,
                    'password': self.password,
                }
            }
        })
        # print 'data', data
        url = '%s%s' % (self.auth_url, token_url)
        # print 'auth_url:', url
        if self.auth_url:
            # request = urllib2.Request(
            #      'http://192.168.1.106:35357/v2.0',
            #      data=data,
            #      headers={'Content-type': 'application/json'}
            # )
            request = urllib2.Request(
                url,
                data=data,
                headers={
                    'Content-type': 'application/json'
                    })
            # print urllib2.urlopen(request, timeout=5).read()

            data = json.loads(urllib2.urlopen(request, timeout=5).read())
            # print 'data_1dddd', data
            self.token = data['access']['token']['id']
            # print self.token
            if not self.tenant_id:
                self.tenant_id = data['access']['token']['tenant']['id']

                self.admin_obj.update(tenant_id=self.tenant_id)
                print 'save tenant_id'

    def get_endpoint(self):
        # endpoint_data = {
        #     'service_name':'',
        #     'api':'',
        #     'token':'',
        #     'endpoint':'',
        # }


        # 获取数据库中的url
        endpoint_url = self.keystone_obj.values('endpoint')[0]['endpoint']
        url = '%s%s' % (self.auth_url, endpoint_url)
        # print url
        request = urllib2.Request(url,
                headers={
                    'User-Agent': 'python-keystoneclient',
                    'X-Auth-Token': self.token,

                    })
        data = json.loads(urllib2.urlopen(request, timeout=5).read())
        # print 'check_api', request, data





        data = data['endpoints']
        endpoint_data = {}
        for val in data:
            for i,v in val.items():
                endpoint_data[i] = v
            print endpoint_data

            # 创建数据库数据字典
            endpoint_db_data = {
                'endpoint_id': endpoint_data['id'],
                'service_id': endpoint_data['service_id'],
                'enabled': endpoint_data['enabled'],
                'region': endpoint_data['region'],
                'admin_url': endpoint_data['adminurl'],
                'internal_url': endpoint_data['internalurl'],
                'public_url': endpoint_data['publicurl']
            }

            endpoint_obj = one_finger_models.Openstack_keystone_endpoint(**endpoint_db_data)
            print '%s_save' % endpoint_data['id']
            endpoint_data = {}
            endpoint_obj.save()


    def get_service(self):

        service_url = self.keystone_obj.values('service')[0]['service']
        url = '%s%s' % (self.auth_url, service_url)
        # print url
        request = urllib2.Request(url,
                headers={
                    'User-Agent': 'python-keystoneclient',
                    'X-Auth-Token': self.token,

                    })
        data = json.loads(urllib2.urlopen(request, timeout=5).read())
        # print(data)
        data = data['OS-KSADM:services']
        service_data = {}
        service_obj = one_finger_models.Openstack_keystone_service.objects
        for val in data:
            for k, v in val.items():
                service_data[k] = v
            # print service_data
            service_db_data = {
                'service_id': service_data['id'],
                'name': service_data['name'],
                'type': service_data['type'],
                'description': service_data['description'],
                'enabled': service_data['enabled'],
            }
            service_obj.create(**service_db_data)
            # print service_db_data

        # service_obj.save()
        # print 'save_server'




    def check_api(self, url, service):
        try:
            request = urllib2.Request(url,
                    headers={
                        'X-Auth-Token': self.token,
                        })
            urllib2.urlopen(request, timeout=self.get_timeout(service))
            print 'check_api', request
        except Exception as e:
            print self.logger.debug("Got exception from '%s' '%s'" % (service, e))
            print self.logger.critical(0)
            print 'Exception', e
            sys.exit(1)
        self.logger.critical(1)



class service():
    pass

class save_service_db():
    pass


if __name__ == '__main__':
    a = token()