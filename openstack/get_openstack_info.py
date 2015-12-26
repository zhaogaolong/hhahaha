#!/usr/bin/env python
# coding:utf8

# 获取平台信息
# import time
import urllib2
import sys
import json
import pdb
from one_finger import models as one_finger_models
from openstack import models as openstack_models


class Token():
    def __init__(self):
        # 实例化存储对象
        # 获取管理员的用户名
        self.admin_obj = one_finger_models.OpenStackKeystoneAuth.objects.filter(os_tenant_name='admin')

        # 这是数据结构:[{'os_username': u'admin'}]
        self.username = self.admin_obj.values('os_username')[0]['os_username']
        self.password = self.admin_obj.values('os_password')[0]['os_password']
        self.tenant_name = self.admin_obj.values('os_tenant_name')[0]['os_tenant_name']
        self.auth_url = self.admin_obj.values('auth_url')[0]['auth_url']
        self.token = self.admin_obj.values('token')[0]['token']
        self.tenant_id = self.admin_obj.values('tenant_id')[0]['tenant_id']

        # 生成后直接获取token
        self._get_token()

    def _get_token(self):
        # 获取token的方法

        # 获取token的url
        token_url = '%s/tokens' % self.auth_url

        # 包装好json urllib2 会使用它
        data = json.dumps({
            "auth":{
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

    def get_token(self):
        return self.token

    def get_endpoint(self):
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

        data = data['endpoints']
        endpoint_data = {}
        for val in data:
            for i,v in val.items():
                endpoint_data[i] = v
            # print endpoint_data

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
            
            endpoint_obj = one_finger_models.OpenStackKeyStoneEndpoint(**endpoint_db_data)
            # print '%s_save' % endpoint_data['id']
            endpoint_data = {}
            endpoint_obj.save()

    def get_service(self):
        url = '%s/OS-KSADM/services' % self.auth_url
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
        service_obj = one_finger_models.OpenStackKeystoneService.objects
        for val in data:
            for k, v in val.items():
                service_data[k] = v

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

    def get_hosts(self):
        self.add_hosts()
        # self.add_nova_host()

    def add_hosts(self):
        # 获取keystone的服务的数据库对象
        service_obj = one_finger_models.OpenStackKeystoneService.objects.filter(name='nova')

        # pdb.set_trace()
        # 获取 service id
        service_id = service_obj.values()[0]['service_id']

        # 获取endpoint的对象
        endpoint_obj = one_finger_models.OpenStackKeyStoneEndpoint.objects.filter(service_id=service_id)

        # 获取URL
        url = endpoint_obj.values()[0]['public_url']
        # print url, self.tenant_id

        # 拼接url ：http://192.168.254.242:8774/v2/239667eee2124453b69309e9cefae142/os-services
        url = url % {'tenant_id': self.tenant_id} + '/os-services'

        print url
        request = urllib2.Request(url,
                headers={
                    'X-Auth-Project-Id': self.username,
                    'Accept': 'application/json',
                    'User-Agent': 'python-novaclient',
                    'X-Auth-Token': self.token,

                    })
        data = json.loads(urllib2.urlopen(request, timeout=5).read())

        # 创建主机
        host_list = []
        for item in data['services']:
            # print item
            if item['host'] in host_list:
                continue
            else:
                host_list.append(item['host'])

        # host_db_obj = openstack_models.Host.objects()
        for host in host_list:
            openstack_models.Host.objects.create(hostname=host)
        # host_db_obj.save()

        print host_list









    def add_nova_host(self):
        # 获取keystone的服务的数据库对象
        service_obj = one_finger_models.OpenStackKeystoneService.objects.filter(name='nova')

        # pdb.set_trace()
        # 获取 service id
        service_id = service_obj.values()[0]['service_id']

        # 获取endpoint的对象
        endpoint_obj = one_finger_models.OpenStackKeyStoneEndpoint.objects.filter(service_id=service_id)

        # 获取URL
        url = endpoint_obj.values()[0]['public_url']
        # print url, self.tenant_id

        # 拼接url ：http://192.168.254.242:8774/v2/239667eee2124453b69309e9cefae142/os-services
        url = url % {'tenant_id': self.tenant_id} + '/os-services'

        print url
        request = urllib2.Request(url,
                headers={
                    'X-Auth-Project-Id': self.username,
                    'Accept': 'application/json',
                    'User-Agent': 'python-novaclient',
                    'X-Auth-Token': self.token,

                    })
        data = json.loads(urllib2.urlopen(request, timeout=5).read())

        # 创建主机
        host_list = []
        for item in data['services']:
            print item
            if item['host'] in host_list:
                continue
            else:
                host_list.append(item['host'])
        print host_list

        # 定义角色的服务，稍后根据不同规划不同的角色
        manager = ['nova-consoleauth', 'nova-scheduler', 'nova-conductor', 'nova-cert']
        compute = ['nova-compute']

        # 开始分类啦
        for item in data['services']:
            if item['binary'] in compute:
                pass




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
    a = Token()