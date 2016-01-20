#!/usr/bin/env python
# coding:utf8

from openstack.api import cinder


class Check():
    def __init__(self, models):
        self.models = models
        self._check_service_status()

    def _check_service_status(self):
        cc = cinder.CinderClient()
        service_data = cc.service_list()['services']
        if service_data:
            if not self.models.CinderManagerStatus.objects.all():
                status_dic = {
                    'cinder_api_status': 'up',
                }
                for service in service_data:
                    binary_name = '%s' % '_'.join(service['binary'].split('-'))
                    status_dic[binary_name] = service['state']

                self.status_db_obj = self.models.CinderStatus(**status_dic)
                self.status_db_obj.save()
            else:
                self.status_db_obj = self.models.CinderStatus.objects.first()
                self.status_db_obj.cinder_api_status = 'up'

                # check all service
                self._check_status_to_db(self.status_db_obj, service_data)
                self.status_db_obj.save()

                cinder_state_list = [
                    self.status_db_obj.cinder_api_status,
                    self.status_db_obj.cinder_volume,
                    self.status_db_obj.cinder_scheduler,
                ]

                if 'down' in cinder_state_list:
                    self.status_db_obj.status = 'down'
                else:
                    self.status_db_obj.status = 'up'
                self.status_db_obj.save()

    def _check_status_to_db(self, db_obj, data):
        for service in data:

            binary_name = '%s' % '_'.join(service['binary'].split('-'))
            # import pdb
            # pdb.set_trace()
            if getattr(db_obj, binary_name) != service['state']:
                setattr(db_obj, binary_name, service['state'])




