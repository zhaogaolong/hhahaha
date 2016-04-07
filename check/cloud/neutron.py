#!/usr/bin/env python
# coding:utf8

from openstack.api import neutron as neutron_api
from openstack import models as openstack_models
from asset import models as asset_models
from one_finger import settings
from event.openstack import neutron as event_neutron


class Check():
    def __init__(self):
        self.neutron_agent_list = neutron_api.agent_list()
        self.dhcp = 0
        self.l3 = 0
        # import pdb
        # pdb.set_trace()

    def start(self):
        self._check_host()
        self._check_manager_api()
        self._cloud_status()
        self._check_all_compute()
        self._check_neutron_status()

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

        # import pdb
        # db.set_trace()
        for item in self.neutron_agent_list['agents']:
            # print item['binary'], item['host']

            if item['binary'] == 'neutron-l3-agent' or \
                            item['binary'] == 'neutron-dhcp-agent':
                if openstack_models.NeutronStatus.objects.first():
                    self._check_only_one_service(item)
                else:
                    dic = {
                        'neutron_river_type': settings.NEUTRON_RIVER_TYPE,
                        'neutron_metadata_agent': 'up',
                        'neutron_lbaas_agent': 'up'
                    }
                    openstack_models.NeutronStatus(**dic)

                # 如果是dhcp和l3跳过检查，因为有一个专门检查L3和dhcp的方法

            elif item['host'] in self.manager_node_list:
                # 如果该主机ID能在group里面查询到，就证明该主机是管理节点
                service_db_db = \
                    openstack_models.NeutronManagerServiceStatus.objects.get(
                        host_id=asset_models.Host.objects.get(
                            hostname=item['host']
                        ).id)
                service_name = '%s' % '_'.join(item['binary'].split('-'))

                # 这里的if 主要是元数据的格式 'alive': True,所以要转义为up or down
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

    def _check_host_service(self, service_db_db, service, alive):
        # 测试每一个主机的每一个服务和数据库中对比
        if not getattr(service_db_db, service) == alive:
            setattr(service_db_db, service, alive)
            service_db_db.save()
            # 触发记录日志
            getattr(event_neutron, alive)(service_db_db.host.hostname, service)

    def _check_manager_api(self):
        for manager in \
                openstack_models.NeutronManagerServiceStatus.objects.all():
            ip = manager.host.ip_manager
            url = 'http://%s:9696/' % ip
            # print 'imput url', url
            nc = neutron_api.neutronclient(endpoint_url=url)
            try:
                data = nc.list_agents()
            except Exception:
                data = None

            if data:
                self._data_check_to_db(manager, 'neutron_api_status', 'up')
                #manager.neutron_api_status = 'up'

            else:
                self._data_check_to_db(manager, 'neutron_api_status', 'up')
                # manager.neutron_api_status = 'down'
            self._check_manager_node(manager)

    def _data_check_to_db(self, db_obj, service, value):
        '''
        这是一个检查数据库数据和现在的数据是否一致，是否需要更新。
        '''
        if getattr(db_obj, service) != value:
            setattr(db_obj, service, value)
            db_obj.save()
            # 触发日志记录
            ev = getattr(event_neutron, value)
            ev(db_obj.host.hostname, service)

    def _check_manager_node(self, manager):
        status_list = [
            manager.neutron_api_status,
            getattr(manager, settings.NEUTRON_RIVER_TYPE),
            manager.neutron_metadata_agent,
            manager.neutron_lbaas_agent,
        ]
        # import pdb
        # pdb.set_trace()
        if len(status_list) == status_list.count('up'):
            self._data_check_to_db(manager, 'status', 'up')

        elif len(status_list) > status_list.count('up') > 0:
            self._data_check_to_db(manager, 'status', 'warning')
        else:
            self._data_check_to_db(manager, 'status', 'down')

    def _cloud_status(self):
        # print '_cloud_status'
        if not openstack_models.NeutronStatus.objects.first():
            dic = {
                'neutron_river_type': settings.NEUTRON_RIVER_TYPE,
                'neutron_lbaas_agent': 'null',
                'neutron_metadata_agent': 'null',
            }
            openstack_models.NeutronStatus.objects.create(**dic)

        service_list = [
            'neutron_api_status',
            'neutron_metadata_agent',
            'neutron_lbaas_agent',
        ]

        for service in service_list:
            self._check_service(service)

    def _check_service(self, service):
        # 监测所有管理节点的指定的service监测并更新到neutronStatus状态
        status = []
        for manager in \
            openstack_models.NeutronManagerServiceStatus.objects.all():
            status.append(getattr(manager, service))

        neutron_db_obj = openstack_models.NeutronStatus.objects.first()
        if len(status) == status.count('up'):
            if getattr(neutron_db_obj, service) != 'up':
                setattr(neutron_db_obj, service, 'up')
                neutron_db_obj.save()
                # 触发记录日志
                ev = event_neutron.CloudStatus(service, 'up')
                ev.up()

        elif len(status) > status.count('up') > 0:
            if getattr(neutron_db_obj, service) != 'warning':
                setattr(neutron_db_obj, service, 'warning')
                neutron_db_obj.save()
                # 触发记录日志
                ev = event_neutron.CloudStatus(service, 'warning')
                ev.warning()

        elif len(status) == status.count('down'):
            if getattr(neutron_db_obj, service) != 'down':
                setattr(neutron_db_obj, service, 'down')
                neutron_db_obj.save()
                # 触发记录日志
                ev = event_neutron.CloudStatus(service, 'down')
                ev.down()

    def _check_only_one_service(self, item):
        if item['alive']:
            status = 'up'
        else:
            status = 'down'
        if item['binary'] == 'neutron-l3-agent':
            self.l3 += 1
            mg_obj = openstack_models.NeutronStatus.objects.first()
            if mg_obj.neutron_l3_agent != status:
                mg_obj.neutron_l3_agent = status
                mg_obj.save()
                ev = event_neutron.CloudStatus('neutron-L3-agent', status)
                getattr(ev, status)()
            if mg_obj.neutron_l3_start_node:
                if mg_obj.neutron_l3_start_node != item['host']:
                    # 如果名字不一样就触发迁移的日志
                    content = 'Neutron L3 service Migrate from  %s host to ' \
                              '%s host' % (mg_obj.neutron_l3_start_node,
                                           item['host'])
                    mg_obj.neutron_l3_start_node = item['host']
                    mg_obj.save()
                    event_neutron.neutron_migrate(content)

            else:
                mg_obj.neutron_l3_start_node = item['host']
                mg_obj.save()
                content = 'create L3 service and start in the %s' % item['host']
                event_neutron.neutron_info(item['host'], content)

        elif item['binary'] == 'neutron-dhcp-agent':
            self.dhcp += 1
            mg_obj = openstack_models.NeutronStatus.objects.first()
            if mg_obj.neutron_dhcp_agent != status:
                mg_obj.neutron_dhcp_agent = status
                mg_obj.save()
                ev = event_neutron.CloudStatus('neutron-DHCP-agent', status)
                getattr(ev, status)()

            if mg_obj.neutron_dhcp_start_node:
                if mg_obj.neutron_dhcp_start_node != item['host']:
                    # 如果名字不一样就触发迁移的日志
                    content = 'Neutron DHCP service Migrate from  %s host to ' \
                              '%s host' % (mg_obj.neutron_dhcp_start_node,
                                           item['host'])
                    mg_obj.neutron_dhcp_start_node = item['host']
                    mg_obj.save()
                    event_neutron.neutron_migrate(content)

            else:
                mg_obj.neutron_dhcp_start_node = item['host']
                mg_obj.save()
                content = 'create DHCP service and start in the %s' % \
                          item['host']
                event_neutron.neutron_info(item['host'], content)

    def _check_all_compute(self):
        status = []
        neutron_db_obj = openstack_models.NeutronStatus.objects.first()
        for compute in \
                openstack_models.NeutronComputeServiceStatus.objects.all():
            st = getattr(compute, settings.NEUTRON_RIVER_TYPE)
            status.append(st)
        if len(status) == status.count('up'):
            self._data_check_to_db(neutron_db_obj, 'neutron_compute', 'up')
        elif len(status) > status.count('up') > 0:
            self._data_check_to_db(neutron_db_obj, 'neutron_compute', 'warning')
        else:
            self._data_check_to_db(neutron_db_obj, 'neutron_compute', 'down')

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

        if not self.dhcp:
            neutron_db_obj = openstack_models.NeutronStatus.objects.first()
            neutron_db_obj.neutron_dhcp_start_node = None
            neutron_db_obj.neutron_dhcp_agent = 'down'
            neutron_db_obj.save()
            ev = event_neutron.CloudStatus('neutron-dhcp-agent', 'down')
            ev.down()
        if not self.l3:
            neutron_db_obj = openstack_models.NeutronStatus.objects.first()
            neutron_db_obj.neutron_l3_start_node = None
            neutron_db_obj.neutron_l3_agent = 'down'
            neutron_db_obj.save()
            ev = event_neutron.CloudStatus('neutron-l3-agent', 'down')
            ev.down()



