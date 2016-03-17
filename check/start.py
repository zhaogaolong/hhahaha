#!/usr/bin/env python
# coding:utf8
import time
import os
import sys
import time
import multiprocessing
import threading

# config allow this is py invoke django models
Base_dir = "/".join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1])
sys.path.append(Base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "one_finger.settings")
from openstack import models as openstack_models
from storage import models as storage_models
# from asset import models as asset_models
import django
django.setup()
# config allow this is py invoke django models

# check models
from cloud import nova
from cloud import neutron
from cloud import cinder
from ceph import ceph


def check_cloud():
    print '\033[32mcheck_cloud\033[0m'
    cloud_status = [
        openstack_models.NovaStatus.objects.first().status,
        storage_models.CephStatus.objects.first().status,
        openstack_models.NeutronStatus.objects.first().status,
        openstack_models.CinderStatus.objects.first().status,
    ]
    if not openstack_models.CloudStatus.objects.filter():
        cloud_db_obj = openstack_models.CloudStatus(status='null')
        cloud_db_obj.save()

    cloud_db_obj = openstack_models.CloudStatus.objects.first()
    # import pdb
    # pdb.set_trace()

    if len(cloud_status) == cloud_status.count('down'):
        check_db_update(cloud_db_obj, 'down')
    elif 'down' in cloud_status:
        check_db_update(cloud_db_obj, 'critical')
    elif 'warning' in cloud_status:
        check_db_update(cloud_db_obj, 'warning')
    elif len(cloud_status) == cloud_status.count('up'):
        check_db_update(cloud_db_obj, 'up')


def check_db_update(dbobj, status):
    if dbobj.status != status:
        dbobj.status = status
        dbobj.save()


def check_nova():
    print '\033[32mcheck_nova\033[0m'
    nc = nova.Check()
    nc.start()

    time.sleep(10)


def check_neutron():
    print '\033[32mcheck_neutron\033[0m'
    nc = neutron.Check()
    nc.start()
    time.sleep(10)


def check_cinder():
    print '\033[32mcheck_cinder\033[0m'

    nc = cinder.Check(openstack_models)
    time.sleep(10)

def check_ceph():
    print '\033[32mcheck_ceph\033[0m'
    ce = ceph.Check()
    ce.start()
    time.sleep(10)


if __name__ == "__main__":
    service_list = [
        check_nova,
        check_neutron,
        check_cinder,
        check_ceph,
    ]
    # service_list = [check_neutron]
    # # for service in service_list:
    # #     service()
    th_list = []

    while True:
        # th_list = []
        for service in service_list:
            t = threading.Thread(target=service)
            t.start()
            th_list.append(t)
        for th in th_list:
            th.join()
        th_list = []
        cloud = threading.Thread(target=check_cloud)
        cloud.start()
        cloud.join()
        print 'th_list:', th_list

    #
    # for service in service_list:
    #     t = threading.Thread(target=service)
    #     t.start()
    #     th_list.append(t)
    # #
    # for th in th_list:
    #     th.join()
    #     th_list.remove(th)
    # print 'th_list:', th_list