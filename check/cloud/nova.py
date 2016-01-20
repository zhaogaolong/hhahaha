#!/usr/bin/env python
# coding:utf8
# import os
# import sys
####
# Base_dir = "/".join(os.path.dirname(os.path.abspath(__file__)).split('/')[
# :-1])
# sys.path.append(Base_dir)
from openstack.api import nova


class Check():
    def __init__(self, models):
        self.models = models
        self.nova_status_db_obj = self.models.NovaStatus.objects.first()
        self.manager_db_list = \
            self.models.NovaManagerServiceStatus.objects.all()
        self.compute_db_list = \
            self.models.NovaComputeServiceStatus.objects.all()
        self.host_data = nova.host_data()
        self._check_host()
        self._check_mgmt_api()
        self._check_manage()
        self._check_status()

    def _check_host(self):
        # print '_check_host'
        # 这是能从openstack 平台获取的信息
        host_data = nova.host_data()
        for item in host_data['services']:
            # 处理状态对比数据库信息
            self._check_db(item)

    def _check_db(self, item):
        # print '_check_db'

        manager_binary = ['nova-consoleauth',
                          'nova-scheduler',
                          'nova-conductor',
                          'nova-cert'
                          ]
        compute_binary = ['nova-compute']
        # print 'item', item

        # 如果该主机是管理节点
        if item['binary'] in manager_binary:
            host_id = self.models.Host.objects.get(hostname=item['host']).id
            service_obj = self.models.NovaManagerServiceStatus.objects.get(
                host_id=host_id
            )
            binary_name = '%s_status' % '_'.join(item['binary'].split('-'))
            binary_db_status = getattr(service_obj, binary_name)

            if binary_db_status != item['state']:
                setattr(service_obj, binary_name, item['state'])
            service_obj.save()

        # 如果该主机是计算节点
        elif item['binary'] in compute_binary:
            host_id = self.models.Host.objects.get(hostname=item['host']).id

            # 获取服务记录的对象
            service_obj = self.models.NovaComputeServiceStatus.objects.get(
                host_id=host_id
            )

            if item['status'] == 'enabled':
                if not service_obj.enabled_nova_compute:
                    service_obj.enabled_nova_compute = 1

            nova_compute_status = item['state']
            if service_obj.nova_compute_status != nova_compute_status:
                # 如果现在的状态和数据库的状态不一致，那就要存储现在的状态
                service_obj.nova_compute_status = nova_compute_status

            service_obj.save()

    def _check_status(self):
        # print '_check_status'
        if not self.models.NovaStatus.objects.first():
            db_dic = {
                'nova_api_status': 'down',
            }
            self.models.NovaStatus.objects.create(**db_dic)
        self._analysis()

    def _analysis(self):
        # print '_analysis'
        service_list = [
            'nova_consoleauth_status',
            'nova_api_status',
            'nova_scheduler_status',
            'nova_conductor_status',
            'nova_cert_status',
            'nova_compute_status'
            ]

        for service in service_list:
            self._check_cloud_service_status(service)

        nova_status_db = self.models.NovaStatus.objects.first()
        nova_status_list = [
            nova_status_db.nova_consoleauth_status,
            nova_status_db.nova_scheduler_status,
            nova_status_db.nova_conductor_status,
            nova_status_db.nova_cert_status,
            nova_status_db.nova_compute_status,
        ]
        # import pdb
        # pdb.set_trace()
        # print nova_status_dic
        # print nova_status_list
        # 监测
        if 'down' in nova_status_list:
            nova_status_db.status = 'down'
        elif 'warning' in nova_status_list:
            nova_status_db.status = 'warning'
        if len(nova_status_list) == nova_status_list.count('up'):
            nova_status_db.status = 'up'

        nova_status_db.save()

    def _check_cloud_service_status(self, service):
        # print '_check_cloud_service_status'
        if service == 'nova_compute_status':
            self._check_nova_status_compute()
        else:
            self._check_nova_status_manager(service)

    def _check_mgmt_api(self):
        # print '_check_mgmt_api'
        mg_db_list = self.models.NovaManagerServiceStatus.objects.all()
        # print mg_db_list
        for mgmt in mg_db_list:
            host_db_obj = self.models.Host.objects.get(id=mgmt.host_id)
            host_mg_ip = host_db_obj.ip_manager
            data = nova.mgmt_api_status(host_mg_ip)
            # print 'data', data
            if data:
                # print data
                mgmt.nova_api_status = 'up'
            else:
                mgmt.nova_api_status = 'down'
            mgmt.save()

    def _check_manage(self):
        # print '_check_manage'
        # 着是监测管理节点的状态
        for manager in self.manager_db_list:
            status_dic = [
                manager.nova_api_status,
                manager.nova_consoleauth_status,
                manager.nova_scheduler_status,
                manager.nova_conductor_status,
                manager.nova_cert_status,
            ]
            if status_dic.count('up') == 5:
                manager.status = 'up'
            elif 5 < status_dic.count('up') > 0:
                manager.status = 'warning'
            else:
                manager.status = 'down'
            manager.save()

    def _check_nova_status_compute(self):
        # print '_check_nova_status_compute'
        status = []
        nova_status_obj = self.models.NovaStatus.objects.first()
        for compute in self.compute_db_list:
            status.append(compute.nova_compute_status)
        # print status


        if len(status) == status.count('up'):
           nova_status_obj.nova_compute_status = 'up'
        elif len(status) > status.count('up') > 0:
            # print 'save warning status to db'
            nova_status_obj.nova_compute_status = 'warning'
            nova_status_obj.save()
            # print 'nova_status--compute', nova_status_obj.nova_compute_status


        else:
            nova_status_obj.nova_compute_status = 'down'
        nova_status_obj.save()

    def _check_nova_status_manager(self, service):
        # print '_check_nova_status_manager'
        # print service
        status = []
        for manage in self.manager_db_list:
            # 迭代所有的管理节点，查看该服务状态
            status.append(getattr(manage, service))
        # print status
        # import pdb
        # pdb.set_trace()
        nova_status_db_obj = self.models.NovaStatus.objects.first()
        if len(status) == status.count('up'):
            # print 'nova status is up'
            setattr(nova_status_db_obj, service, 'up')
        elif len(status) < status.count('up') and status.count('up') > 0:
            setattr(nova_status_db_obj, service, 'warning')
        else:
            setattr(nova_status_db_obj, service, 'down')
        nova_status_db_obj.save()


