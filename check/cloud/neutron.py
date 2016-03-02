#!/usr/bin/env python
# coding:utf8

from openstack.api import neutron as neutron_api
from openstack import models as openstack_models
from asset import models as asset_models
from one_finger import settings

class Check():
    def __init__(self):
        self.neutron_compute_db_list =  \
            openstack_models.NeutronComputeServiceStatus.objects.all()
        self.neutron_manager_db_list = \
            openstack_models.NeutronManagerServiceStatus.objects.all()
        self.neutron_agent_list = neutron_api.agent_list()
        self._check_host()
        self._check_manager_api()
        self._cloud_status()
        self._check_only_one_service()
        self._check_all_compute()
        self._check_neutron_status()
        # import pdb
        # pdb.set_trace()

    def _check_host(self):
        # 通过neutron获取的信息进行格式化监测每个主机的状态
        #　host_data = self.neutron_agent_list()
        #　import pdb
        #　pdb.set_trace()

        self.manager_node_list = []
        self.compute_node_list = []
        manager_group_obj = asset_models.Group.objects.get(name='Manager')
        compute_group_obj = asset_models.Group.objects.get(name='Compute')
        for host_obj in manager_group_obj.host_set.select_related():
            self.manager_node_list.append(host_obj.hostname)
        for host_obj in compute_group_obj.host_set.select_related():
            self.compute_node_list.append(host_obj.hostname)

        for item in self.neutron_agent_list['agents']:
            if item['host'] in self.manager_node_list:
                # 如果该主机ID能在group里面查询到，就证明该主机是管理节点
                service_db_db = \
                    openstack_models.NeutronManagerServiceStatus.objects.get(
                        host_id=asset_models.Host.objects.get(
                            hostname=item['host']
                        ).id)
                service_name = '%s' % '_'.join(item['binary'].split('-'))
                if item['alive']:
                    alive = 'up'
                else:
                    alive = 'down'
                self._check_host_service(service_db_db, service_name, alive)

            elif item['host'] in self.compute_node_list:
                # 如果该主机ID能在group里面查询到，就证明该主机是管理节点
                service_db_db = \
                    openstack_models.NeutronComputeServiceStatus.objects.get(
                        host_id=asset_models.Host.objects.get(
                            hostname=item['host']
                        ).id)
                service_name = '%s' % '_'.join(item['binary'].split('-'))
                if item['alive']:
                    alive = 'up'
                else:
                    alive = 'down'
                self._check_host_service(service_db_db, service_name, alive)

            # elif host_db_obj.host_group_id == compute_group_id:
            #     service_db_db = \
            #         self.models.NeutronComputeServiceStatus.objects.get(
            #             host_id=host_db_obj.id)

            #     service_name = '%s' % '_'.join(item['binary'].split('-'))
            #     if item['alive']:
            #         alive = 'up'
            #     else:
            #         alive = 'down'
                self._check_host_service(service_db_db, service_name, alive)

    def _check_host_service(self, service_db_db, service, alive):
        # 测试每一个主机的每一个服务和数据库中对比
        if not getattr(service_db_db, service) == alive:
            setattr(service_db_db, service, alive)
            service_db_db.save()

    def _check_manager_api(self):
        for manager in self.neutron_manager_db_list:
            ip = manager.host.ip_manager
            url = 'http://%s:9696/' % ip
            # print 'imput url', url
            nc = neutron_api.neutronclient(endpoint_url=url)
            try:
                data = nc.list_agents()
            except Exception:
                data = None

            # import pdb
            # pdb.set_trace()
            if data:
                manager.neutron_api_status = 'up'
            else:
                manager.neutron_api_status = 'down'
            manager.save()
            self._check_manager_node(manager)

    def _check_manager_node(self, manager):
        status_list = [
            manager.neutron_api_status,
            manager.neutron_openvswitch_agent,
            manager.neutron_metadata_agent,
            manager.neutron_lbaas_agent,
            # manager.neutron_l3_agent,
            # manager.neutron_dhcp_agent,
        ]
        # import pdb
        # pdb.set_trace()
        if len(status_list) == status_list.count('up'):
            self._service_status_contrast(manager, 'up')

        elif len(status_list) > status_list.count('up') > 0:
            self._service_status_contrast(manager, 'warning')
        else:
            self._service_status_contrast(manager, 'down')

    def _service_status_contrast(self, manager, status):
        if not manager.status == status:
            manager.status = status
            manager.save()

    def _cloud_status(self):
        # print '_cloud_status'
        if not openstack_models.NeutronStatus.objects.first():
            dic = {
                'neutron_river_type': 'Open_vSwitch',
                'neutron_lbaas_agent': 'null',
                'neutron_metadata_agent': 'null',
            }
            openstack_models.NeutronStatus.objects.create(**dic)

        service_list = [
            'neutron_api_status',
            'neutron_metadata_agent',
            'neutron_lbaas_agent',
            settings.NEUTRON_RIVER_TYPE,
        ]

        for service in service_list:
            self._check_service(service)

    def _check_service(self, service):
        # 监测所有管理节点的指定的service监测并更新到neutronStatus状态
        status = []
        for manager in self.neutron_manager_db_list:
            status.append(getattr(manager, service))
        # print service
        # print status
        neutron_db_obj  = openstack_models.NeutronStatus.objects.first()
        if len(status) == status.count('up'):
            setattr(neutron_db_obj, service, 'up')

        elif len(status) > status.count('up') > 0:
            setattr(neutron_db_obj,
                    service, 'warning')

        elif len(status) == status.count('down'):
            setattr(neutron_db_obj,
                    service, 'down')
        neutron_db_obj.save()

    def _check_only_one_service(self):
        # print '_check_only_one_service'
        for srevice in self.neutron_agent_list['agents']:
            if srevice['alive']:
                status = 'up'
            else:
                status = 'down'
            if srevice['binary'] == 'neutron-l3-agent':
                mg_obj = openstack_models.NeutronStatus.objects.first()
                if mg_obj.neutron_l3_agent != status:
                    mg_obj.neutron_l3_agent = status
                    mg_obj.save()

            elif srevice['binary'] == 'neutron-dhcp-agent':
                mg_obj = openstack_models.NeutronStatus.objects.first()
                if mg_obj.neutron_dhcp_agent != status:
                    mg_obj.neutron_dhcp_agent = status
                    mg_obj.save()

    def _check_all_compute(self):
        status = []
        for compute in self.neutron_compute_db_list:
            st = getattr(compute, settings.NEUTRON_RIVER_TYPE)
            status.append(st)
        neutron_db_obj = openstack_models.NeutronStatus.objects.first()
        self._check_service_status(neutron_db_obj, 'neutron_compute', status)

    def _check_service_status(self, db_obj, service, list):
        # import pdb
        # pdb.set_trace()
        if len(list) == list.count('up'):
            setattr(db_obj, service, 'up')
        elif len(list) > list.count('up') > 0:
            setattr(db_obj, service, 'warning')
        else:
            setattr(db_obj, service, 'down')
        db_obj.save()

    def _check_neutron_status(self):
        neutron_db_obj = openstack_models.NeutronStatus.objects.first()
        neutron_status_list = [
            neutron_db_obj.neutron_api_status,
            neutron_db_obj.neutron_l3_agent,
            neutron_db_obj.neutron_dhcp_agent,
            neutron_db_obj.neutron_compute,
        ]
        if 'down' in neutron_status_list:
            neutron_db_obj.status = 'down'
        elif 'warning' in neutron_status_list:
            neutron_db_obj.status = 'warning'
        else:
            neutron_db_obj.status = 'up'
        neutron_db_obj.save()

















