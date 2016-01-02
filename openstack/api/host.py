#!/usr/bin/env python
# coding:utf8

import urllib2
import json
#####
from one_finger import models as one_finger_models
from openstack import models as openstack_models
from openstack.api import keystone


def host_list():
    kc = keystone.KeyStone()
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
    url = url % {'tenant_id': kc.tenant_id} + '/os-services'

    # print url
    request = urllib2.Request(url,                headers={
            'X-Auth-Project-Id': kc.username,
            'Accept': 'application/json',
            'User-Agent': 'python-novaclient',
            'X-Auth-Token': kc.token,

            })
    data = json.loads(urllib2.urlopen(request, timeout=5).read())

    # 创建主机
    hosts = []
    for item in data['services']:
        if item['host'] in hosts:
            continue
        else:
            hosts.append(item['host'])
    return hosts


def host_db_list():
    return openstack_models.Host.objects.all()