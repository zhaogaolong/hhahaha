#!/usr/bin/env python
# coding:utf8
# 获取平台信息
# import time
import urllib2
import sys
import json
import commands
import pdb

from django.conf import settings
# in local models########
from openstack.api import opentack_ansible
from openstack.api import keystone, nova as nova_hosts, cinder ,neutron, ceph
from one_finger import models as one_finger_models
from openstack import models as openstack_models
from one_finger.cloud_logging import cloud_logging as logging
log = logging.logger



class GetOpenStackInfo():
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
        self.kc = keystone.KeyStone()
        # pdb.set_trace()
        self.token = self.kc.get_token()

    def get_endpoint(self):
        data = keystone.KeyStone().endpoint_list()

        # print data
        endpoint_data = {}
        for val in data:
            for i, v in val.items():
                # 迭代整个item 生成完整的字典
                endpoint_data[i] = v
            if one_finger_models.OpenStackKeyStoneEndpoint.objects.filter(endpoint_id=endpoint_data['id']):
                # 测试该记录是否已存存在
                continue
            # 创建数据库数据字典
            endpoint_db_data = {
                'endpoint_id': endpoint_data['id'],
                'service_id': endpoint_data['service_id'],
                'enabled': endpoint_data['enabled'],
                'region': endpoint_data['region'],
                'adminurl': endpoint_data['adminurl'],
                'internalurl': endpoint_data['internalurl'],
                'publicurl': endpoint_data['publicurl']
            }
            log.info('start get info')
            endpoint_obj = one_finger_models.OpenStackKeyStoneEndpoint(**endpoint_db_data)
            # print '%s_save' % endpoint_data['id']
            endpoint_data = {}
            endpoint_obj.save()
            log_info = 'Storage Endpoint to DB:' + json.dumps(endpoint_db_data)
            log.info(log_info)

    def get_service(self):
        data = self.kc.service_list()
        service_data = {}
        service_obj = one_finger_models.OpenStackKeystoneService.objects
        for val in data:
            for k, v in val.items():
                # 迭代整个item 生成完整的字典
                service_data[k] = v

            if one_finger_models.OpenStackKeystoneService.objects.filter(service_id=service_data['id']):
                # 测试该记录是否已存存在
                continue

            service_db_data = {
                'service_id': service_data['id'],
                'name': service_data['name'],
                'type': service_data['type'],
                'description': service_data['description'],
                'enabled': service_data['enabled'],
            }
            service_obj.create(**service_db_data)
            # print service_db_data

            log_info = 'Storage Endpoint to DB:' + json.dumps(service_db_data)
            log.info(log_info)

        # service_obj.save()
        # print 'save_server'

    def add_hosts(self, ip):
        host_list = nova_hosts.host_list()
        for host in host_list:
            if not openstack_models.Host.objects.filter(hostname=host):
                # 监测该主机是否存在数据库中
                openstack_models.Host.objects.create(hostname=host)
        log_info = 'Create Host: %s to DB' % ' '.join(host_list)
        log.info(log_info)
        self.add_hosts_ip(ip)

        # print host_list

    def add_hosts_ip(self, ip):
        host_db_all = nova_hosts.host_db_list()

        for host in host_db_all:
            if host.ip_manager and host.ip_pxe and host.ip_storage:
                # 如果IP地址存在就表明该主机的IP地址存在了
                continue

            # 通过hosts文件获取其他主机的管理IP地址
            discover_host_name_comm = "ssh %s cat /etc/hosts |grep %s |awk '{print $1}'" % (ip, host.hostname)

            ac = opentack_ansible.CmmAndRun(host=ip, cmd=discover_host_name_comm)
            data = ac.start()
            # pdb.set_trace()
            # status, manage_ip_out = commands.getstatusoutput(discover_host_name_comm)
            if not data:
                # 如果执行错误就return 结束
                return 'comm error: %s' % discover_host_name_comm
            # import pdb
            # pdb.set_trace()

            host_ip_info = self.get_host_ip(data)
            # import pdb
            # pdb.set_trace()

            host.ip_manager = host_ip_info['br-mgmt']
            host.ip_pxe = host_ip_info['br-fw-admin']
            host.ip_storage = host_ip_info['br-storage']
            host.ip_public = host_ip_info['br-ex']
            host.save()

            log_info = ('Save Host:%s  to DB' % host.hostname)
            log.info(log_info)

    def get_host_ip(self, manager_ip):
        host_ip_dic = {}
        interface_list = ['br-mgmt', 'br-storage', 'br-fw-admin', 'br-ex']

        for interface_name in interface_list:

            comm = "ssh %s ifconfig %s |grep inet |awk -F ':' '{print$2}' |awk '{print $1}'" % (manager_ip,
                                                                                                interface_name)
            # status, ip = commands.getstatusoutput(comm)
            # if not status:
            #     host_ip_dic[interface_name] = ip

            ac = opentack_ansible.CmmAndRun(host=manager_ip, cmd=comm)
            data = ac.start()
            # pdb.set_trace()

            if data:
                host_ip_dic[interface_name] = data
            else:
                host_ip_dic[interface_name] = None

        print host_ip_dic
        # pdb.set_trace()
        log_info = 'Get Host %s IP' % manager_ip
        log.info(log_info)
        return host_ip_dic

    def add_nova_host(self):
        # data = nova_hosts.host_list()

        data = nova_hosts.host_data()
        # 创建主机列表
        host_list = []

        # 创建主机db对象列表
        host_db_list = {}
        for item in data['services']:
            if item['host'] in host_list:
                continue
            else:
                host_list.append(item['host'])
                host_db_list[item['host']] = openstack_models.Host.objects.get(hostname=item['host'])

        # pdb.set_trace()
        # 定义角色的服务，稍后根据不同规划不同的角色
        manager_binary = ['nova-consoleauth', 'nova-scheduler', 'nova-conductor', 'nova-cert']
        compute_binary = ['nova-compute']

        nova_manager_obj = openstack_models.NovaManagerServiceStatus()

        # 开始分类啦
        # print data['services']
        manager_db_dic = {}
        compute_db_dic = {}
        for item in data['services']:
            if item['binary'] in manager_binary:
                if openstack_models.NovaManagerServiceStatus.objects.filter(
                        host_id=host_db_list[item['host']].id):
                    # 判断该记录是否存在，如果存在就继续下次循环
                    continue
                if not item['host'] in manager_db_dic:
                    # 监测该主机名是否在字典中，如果没有添加该主机，添加一个ForeignKey的host_id
                    manager_db_dic[item['host']] = {}
                    manager_db_dic[item['host']]['host_id'] = host_db_list[item['host']].id
                binary_name_status = '%s_status' % '_'.join(item['binary'].split('-'))
                binary_enabled = 'enabled_%s' % '_'.join(item['binary'].split('-'))
                # print binary_name_status
                # print binary_enabled

                if item['status'] == 'enabled':
                    # 数据库中存储的是布尔值
                    binary_enabled_status = 1
                else:
                    # 数据库中存储的是布尔值
                    binary_enabled_status = 0
                manager_db_dic[item['host']][binary_name_status] = item['state']
                manager_db_dic[item['host']][binary_enabled] = binary_enabled_status

                # print binary_name_status, type(binary_name_status)
                # print binary_enabled, type(binary_enabled)
                # print 'start if hostname: %s' % item['host']

            elif item['binary'] in compute_binary:
                if openstack_models.NovaComputeServiceStatus.objects.filter(
                        host_id=host_db_list[item['host']].id):
                    continue
                if not item['host'] in compute_db_dic:
                    compute_db_dic[item['host']] = {}
                    compute_db_dic[item['host']]['host_id'] = host_db_list[item['host']].id

                binary_name_status = '%s_status' % '_'.join(item['binary'].split('-'))
                binary_enabled = 'enabled_%s' % '_'.join(item['binary'].split('-'))
                # print binary_name_status, type(binary_name_status)
                # print binary_enabled, type(binary_enabled)
                if item['status'] == 'enabled':
                    binary_enabled_status = 1
                else:
                    binary_enabled_status = 0
                # pdb.set_trace()
                compute_db_dic[item['host']][binary_name_status] = item['state']
                compute_db_dic[item['host']][binary_enabled] = binary_enabled_status

        # print manager_db_dic
        # print 'compute_db_dic', compute_db_dic


        if not openstack_models.Group.objects.filter(name='Manager'):
            openstack_models.Group.objects.create(name='Manager')

        if not openstack_models.Group.objects.filter(name='Compute'):
            openstack_models.Group.objects.create(name='Compute')


        # 把数据存储到数据库中
        for k, v in manager_db_dic.items():
            # print 'k--->', k
            # print 'v--->', v
            if not openstack_models.NovaManagerServiceStatus.objects.filter(
                    host_id=openstack_models.Host.objects.get(hostname=k).id):

                # 把数据存储到数据库中
                openstack_models.NovaManagerServiceStatus.objects.create(**v)

                # 把主机添加相应的组中
                group_obj = openstack_models.Group.objects.get(name='Manager')
                manager_obj = openstack_models.Host.objects.get(hostname=k)
                manager_obj.host_group_id = group_obj.id
                manager_obj.save()

        log_info = 'Add Nova Compute Service to DB %s IP'
        log.info(log_info)

        # print(compute_db_dic)
        for k, v in compute_db_dic.items():
            # print k
            # print v
            if not openstack_models.NovaComputeServiceStatus.objects.filter(
                    host_id=openstack_models.Host.objects.get(hostname=k).id):
                openstack_models.NovaComputeServiceStatus.objects.create(**v)



                group_obj = openstack_models.Group.objects.get(name='Compute')
                compute_obj = openstack_models.Host.objects.get(hostname=k)
                compute_obj.host_group_id = group_obj.id
                compute_obj.save()

                # openstack_models.Host.objects.update_or_create(
                #     host_group_id=openstack_models.Group.objects.get(name='Compute').id)


        log_info = 'Add Nova Compute Service to DB %s IP'
        log.info(log_info)

    def add_cinder_host(self):
        host_data = cinder.CinderClient().service_list()
        log.debug(json.dumps(host_data))

        db_dic = {}

        for item in host_data['services']:
            # 获取信息
            manager_group_db_obj = openstack_models.Group.objects.get(
                name='Manager')
            manager_list = openstack_models.Host.objects.filter(
                host_group_id=manager_group_db_obj.id)
            # 获取所有主机信息
            for host in manager_list:
                if not openstack_models.CinderManagerStatus.objects.filter(
                        host_id=host.id):
                    # 判断该是否有该主机
                    if not host.hostname in db_dic:
                        # 如果没有创建字典就先创建一个
                        db_dic[host.hostname] = {}
                        db_dic[host.hostname]['host_id'] = host.id
                    binary_name = '%s' % '_'.join(item['binary'].split('-'))
                    print binary_name
                    db_dic[host.hostname][binary_name] =  item['state']
        if db_dic == None:
            return None
        for host, item in db_dic.items():
            openstack_models.CinderManagerStatus.objects.create(**item)

    def add_neutron_host(self):
        data = neutron.agent_list()

        db_dic = {}


        for item in data['agents']:
            # 获取该主机的id
            host_id = openstack_models.Host.objects.get(
                hostname=item['host']).id

            if not item['host'] in db_dic:
                # 判断字典里面是否有该主机
                db_dic[item['host']] = {}
                db_dic[item['host']]['host_id'] = host_id
                db_dic[item['host']]['neutron_river_type'] = \
                    settings.NEUTRON_RIVER

            binary_name = '%s' % '_'.join(item['binary'].split('-'))
            if item['alive']:
                status = 'up'
            else:
                status = 'down'
            db_dic[item['host']][binary_name] = status
        # print db_dic

        manager_group_id = openstack_models.Group.objects.get(name='Manager').id
        compute_group_id = openstack_models.Group.objects.get(name='Compute').id

        for host, item in db_dic.items():
            compute_obj = openstack_models.Host.objects.get(hostname=host)
            # print item
            if compute_obj.host_group_id == manager_group_id:
                # 该主机就是manager主机
                nm_obj = openstack_models.NeutronManagerServiceStatus
                if not nm_obj.objects.filter(
                        host_id=openstack_models.Host.objects.get(
                            hostname=host).id
                ):
                    nm_obj.objects.create(**item)
                # else:
                #   openstack_models.NeutronManagerServiceStatus.objects.filter(
                #         host_id=openstack_models.Host.objects.get(
                #             hostname=item['host']).id
                #     ).update(**item)
            elif compute_obj.host_group_id == compute_group_id:
                # 该主机就是compute主机
                nc_obj = openstack_models.NeutronComputeServiceStatus
                if not nc_obj.objects.filter(
                        host_id=openstack_models.Host.objects.get(
                            hostname=host).id):
                    nc_obj.objects.create(**item)

    def add_ceph_osd_host(self):
        if settings.CEPH_ENABLED == True:
            cc = ceph.Ceph()
            data = cc.osd_list()

            for k, v in data.items():
                if not openstack_models.CephOsdStatus.objects.filter(
                        osd_name=k):
                    openstack_models.CephOsdStatus.objects.create(**v)

    def add_ceph_mon_host(self):
        if settings.CEPH_ENABLED == True:
            # 判断是否启用ceph

            mon_db_dic = {}
            cc = ceph.Ceph()
            data = cc.mon_list()

            if data:
                for host_ip, v in data.items():
                    mon_db_dic[host_ip] = {}
                    host_id = openstack_models.Host.objects.get(
                        ip_storage=host_ip).id
                    mon_db_dic[host_ip]['host_id'] = host_id
                    mon_db_dic[host_ip]['mon_id'] = v['id']

                for host, val in mon_db_dic.items():
                    print val
                    openstack_models.CephMonitorStatus.objects.create(**val)

    def add_mysql_host(self):
        pass












class service():
    pass

class save_service_db():
    pass


if __name__ == '__main__':
    a = Token()