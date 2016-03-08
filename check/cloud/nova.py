#!/usr/bin/env python
# coding:utf8
# import os
# import sys
####
# Base_dir = "/".join(os.path.dirname(os.path.abspath(__file__)).split('/')[
# :-1])
# sys.path.append(Base_dir)
from openstack.api import nova
from event.openstack import nova as event_nova
from asset import models as asset_models
from openstack import models as openstack_models


class Check():
    def __init__(self):
        self.host_data = nova.host_data()

    def start(self):
        self._check_host()
        self._check_mgmt_api()
        self._check_manage()
        self._check_status()
        self._check_cloud_nova()

    def _check_host(self):
        # print '_check_host'
        # 这是能从openstack 平台获取的信息
        # 检查每一台主机的服务状态
        host_data = nova.host_data()
        for item in host_data['services']:
            # 处理状态对比数据库信息
            self._check_db(item)

    def _check_db(self, item):
        # 检查现在的状态和数据库中的状态是否发生变化

        manager_binary = ['nova-consoleauth',
                          'nova-scheduler',
                          'nova-conductor',
                          'nova-cert'
                          ]
        compute_binary = ['nova-compute']
        # print 'item', item

        # 如果该主机是管理节点
        if item['binary'] in manager_binary:
            service_obj = openstack_models.NovaManagerServiceStatus.objects.get(
                host_id=asset_models.Host.objects.get(hostname=item['host']).id
            )
            binary_name = '%s_status' % '_'.join(item['binary'].split('-'))

            # 获取服务现在的状态
            binary_db_status = getattr(service_obj, binary_name)
            if binary_db_status != item['state']:
                setattr(service_obj, binary_name, item['state'])
                service_obj.save()
                event = getattr(event_nova, item['state'])
                event(item['host'], item['binary'])

        # 如果该主机是计算节点
        elif item['binary'] in compute_binary:
            # 获取服务记录的对象
            service_obj = openstack_models.NovaComputeServiceStatus.objects.get(
                host_id=asset_models.Host.objects.get(hostname=item['host']).id
            )
            if item['status'] == 'enabled':
                if not service_obj.enabled_nova_compute:
                    service_obj.enabled_nova_compute = 1
                    service_obj.save()
            if service_obj.nova_compute_status != item['state']:
                # 如果现在的状态和数据库的状态不一致，那就要存储现在的状态
                service_obj.nova_compute_status = item['state']
                event = getattr(event_nova, item['state'])
                event(item['host'], item['binary'])
                service_obj.save()

    def _check_mgmt_api(self):
        # 监测每个管理节点的API相应
        # print '_check_mgmt_api'
        mg_db_list = openstack_models.NovaManagerServiceStatus.objects.all()
        # print mg_db_list
        for mgmt in mg_db_list:
            host_db_obj = asset_models.Host.objects.get(id=mgmt.host_id)
            host_mg_ip = host_db_obj.ip_manager
            data = nova.mgmt_api_status(host_mg_ip)
            # print 'data', data
            if data:
                # print data
                if mgmt.nova_api_status != 'up':
                    mgmt.nova_api_status = 'up'
                    event_nova.up(host_db_obj.hostname, 'nova-api')
                    mgmt.save()
            else:
                if mgmt.nova_api_status != 'down':
                    mgmt.nova_api_status = 'down'
                    event_nova.down(host_db_obj.hostname, 'nova-api')
                    mgmt.save()

    def _check_manage(self):
        # print '_check_manage'
        # 着是监测管理节点的状态
        for manager in openstack_models.NovaManagerServiceStatus.objects.all():
            status_dic = [
                manager.nova_api_status,
                manager.nova_consoleauth_status,
                manager.nova_scheduler_status,
                manager.nova_conductor_status,
                manager.nova_cert_status,
            ]
            if status_dic.count('up') == 5:
                if manager.status != 'up':
                    manager.status = 'up'
                    manager.save()
                    event_nova.up(manager.host.hostname, 'node_status')
            elif 5 < status_dic.count('up') > 0:
                if manager.status != 'warning':
                    manager.status = 'warning'
                    manager.save()
                    event_nova.warning(manager.host.hostname, 'node_status')
            else:
                if manager.status != 'down':
                    manager.status = 'down'
                    manager.save()
                    event_nova.down(manager.host.hostname, 'node_status')

    def _check_status(self):
        # print '_check_status'
        if not openstack_models.NovaStatus.objects.first():
            # 数据库中如果没有该条记录就创建一条
            db_dic = {
                'nova_api_status': 'down',
            }
            openstack_models.NovaStatus.objects.create(**db_dic)
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

        nova_status_db = openstack_models.NovaStatus.objects.first()
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
            if nova_status_db.status != 'down':
                nova_status_db.status = 'down'
                nova_status_db.save()
                ev = event_nova.CloudStatus('Cloud Status', 'down')
                ev.down()
        elif 'warning' in nova_status_list:
            if nova_status_db.status != 'warning':
                nova_status_db.status = 'warning'
                nova_status_db.save()
                ev = event_nova.CloudStatus('Cloud Status', 'warning')
                ev.warning()
        elif len(nova_status_list) == nova_status_list.count('up'):
            nova_status_db.status = 'up'
            if nova_status_db.status != 'up':
                nova_status_db.status = 'up'
                nova_status_db.save()
                ev = event_nova.CloudStatus('Cloud Status', 'up')
                ev.up()


    def _check_cloud_service_status(self, service):
        # print '_check_cloud_service_status'
        if service == 'nova_compute_status':
            self._check_nova_status_compute()
        else:
            self._check_nova_status_manager(service)

    def _check_nova_status_compute(self):
        # print '_check_nova_status_compute'
        status = []
        nova_status_obj = openstack_models.NovaStatus.objects.first()
        for compute in openstack_models.NovaComputeServiceStatus.objects.all():
            status.append(compute.nova_compute_status)
        # print status

        # import pdb
        #pdb.set_trace()

        if len(status) == status.count('up'):
            if nova_status_obj.nova_compute_status != 'up':
                nova_status_obj.nova_compute_status = 'up'
                nova_status_obj.save()
                ev = event_nova.CloudStatus('nova_compute', 'up')
                ev.up()
        elif len(status) > status.count('up') > 0:
            # print 'save warning status to db'
            if nova_status_obj.nova_compute_status != 'warning':
                nova_status_obj.nova_compute_status = 'warning'
                nova_status_obj.save()
                ev = event_nova.CloudStatus('nova_compute', 'warning')
                ev.warning()
            # print 'nova_status--compute', nova_status_obj.nova_compute_status
        else:
            if nova_status_obj.nova_compute_status != 'down':
                nova_status_obj.nova_compute_status = 'down'
                nova_status_obj.save()
                ev = event_nova.CloudStatus('nova_compute', 'down')
                ev.down()

    def _check_nova_status_manager(self, service):
        # 检查每一个管理节点上的一个服务的状态
        # print '_check_nova_status_manager'
        # print service
        status = []
        for manage in openstack_models.NovaManagerServiceStatus.objects.all():
            # 迭代所有的管理节点，查看该服务状态
            status.append(getattr(manage, service))
        # print status
        # import pdb
        # pdb.set_trace()
        nova_status_obj = openstack_models.NovaStatus.objects.first()
        state = getattr(nova_status_obj, service)

        if len(status) == status.count('up'):
            # print 'nova status is up'
            state = getattr(nova_status_obj, service)
            # import pdb
            # pdb.set_trace()
            if state != 'up':
                setattr(nova_status_obj, service, 'up')
                nova_status_obj.save()
                ev = event_nova.CloudStatus(service, 'up')
                ev.up()
        elif len(status) > status.count('up') > 0:
            if state != 'warning':
                setattr(nova_status_obj, service, 'warning')
                nova_status_obj.save()
                ev = event_nova.CloudStatus(service, 'warning')
                ev.warning()
        else:
            if state != 'down':
                setattr(nova_status_obj, service, 'down')
                nova_status_obj.save()
                ev = event_nova.CloudStatus(service, 'down')
                ev.warning()

    def _check_cloud_nova(self):
        status = [
            openstack_models.NovaStatus.objects.first().nova_api_status,
            openstack_models.NovaStatus.objects.first().nova_cert_status,
            openstack_models.NovaStatus.objects.first().nova_conductor_status,
            openstack_models.NovaStatus.objects.first().nova_consoleauth_status,
            openstack_models.NovaStatus.objects.first().nova_scheduler_status,
            openstack_models.NovaStatus.objects.first().nova_compute_status,
        ]
        #import pdb
        #pdb.set_trace()
        if len(status) == status.count('up'):
            # print 'nova status is up'
            nova_cloud_obj = openstack_models.NovaStatus.objects.first()
            if nova_cloud_obj.status != 'up':
                nova_cloud_obj.status = 'up'
                nova_cloud_obj.save()
                ev = event_nova.CloudStatus('NOVA STATUS', 'up')
                ev.up()
        elif len(status) > status.count('up') > 0:
            nova_cloud_obj = openstack_models.NovaStatus.objects.first()
            if nova_cloud_obj.status != 'warning':
                nova_cloud_obj.status = 'warning'
                nova_cloud_obj.save()
                ev = event_nova.CloudStatus('NOVA STATUS', 'warning')
                ev.warning()
        else:
            nova_cloud_obj = openstack_models.NovaStatus.objects.first()
            if nova_cloud_obj.status != 'down':
                nova_cloud_obj.status = 'down'
                nova_cloud_obj.save()
                ev = event_nova.CloudStatus('NOVA STATUS', 'down')
                ev.down()



