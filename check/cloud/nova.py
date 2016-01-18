#!/usr/bin/env python
# coding:utf8
import os, sys
####
Base_dir = "/".join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1])
sys.path.append(Base_dir)
from openstack.api import nova


class check():
    def __init__(self, models):
        self.models = models
        self.host_data = nova.host_data()
        self._check_host()
        self._check_mgmt_api()
        self._check_status()

    def _check_host(self):
        host_data = nova.host_data()
        for item in host_data['services']:
            # 处理状态对比数据库信息
            self._check_db(item)

    def _check_db(self, item):
        manager_binary = ['nova-consoleauth',
                          'nova-scheduler',
                          'nova-conductor',
                          'nova-cert'
                          ]
        compute_binary = ['nova-compute']
        # print 'item', item

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

        if not self.models.NovaStatus.objects.first():
            db_dic = {
                'nova_api_status': 'down',
            }
            self.models.NovaStatus.objects.create(**db_dic)
            self._analysis()

    def _analysis(self):
        nova_db_obj = self.models.NovaStatus.objects.first()
        service_list = [
            'nova_consoleauth_status',
            'nova_api_status'
            'nova_scheduler_status',
            'nova_conductor_status',
            'nova_cert_status',
            'nova_compute_status'
            ]

        for service in service_list:
            status = self._check_cloud_service_status(service)

        # 今天告一段落，check all service

    def _check_mgmt_api(self):
        mg_db_list = self.models.NovaManagerServiceStatus.objects.all()
        print mg_db_list
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

    def _check_cloud_service_status(self):
        pass






















