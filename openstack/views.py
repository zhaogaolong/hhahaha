#!/usr/bin/env python
# coding:utf8
import json

#####
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from openstack import get_openstack_info
from openstack.page import cloud, ceph, nova, neutron, cinder
from one_finger.cloud_logging import cloud_logging as logging
log = logging.logger
# from check.cloud import start

from openstack import models as openstack_models




def info(request, ip):
    print 'ip:', ip

    log.info('get GetOpenStackInfo')
    b = get_openstack_info.GetOpenStackInfo()

    log.info('get get_endpoint')
    b.get_endpoint()

    log.info('get get_service')
    b.get_service()

    log.info('get add_hosts')
    b.add_hosts(ip)

    log.info('get add_nova_host')
    b.add_nova_host()

    log.info('get add_cinder_host')
    b.add_cinder_host()

    log.info('get add_neutron_host')
    b.add_neutron_host()

    log.info('get add_ceph_osd_host')
    b.add_ceph_osd_host()

    log.info('get add_ceph_mon_host')
    b.add_ceph_mon_host()
    # b.add_mysql_host()
    return HttpResponseRedirect('/')


def test(request):
    # b = start.job()
    # b.start()
    return render(request, 'openstack/dashboards/item.html')


def cloud_status(request):
    cs = cloud.Cloud()
    return HttpResponse(json.dumps(cs.status()))


def nova_status(request):
    nc = nova.Nova()
    return HttpResponse(json.dumps(nc.status()))


def neutron_status(request):
    nc = neutron.Neutron()
    return HttpResponse(json.dumps(nc.status()))


def cinder_status(request):
    cc = cinder.Cinder()
    return HttpResponse(json.dumps(cc.status()))


def ceph_status(request):
    cc = ceph.Ceph()
    return HttpResponse(json.dumps(cc.status()))


# dashboards items

def dashboards_node_status(request):
    node_list = openstack_models.Host.objects.all()
    return render(request, 'openstack/dashboards/node_status.html',
                  {'node_list': node_list})


def dashboards_neutron_status(request):
    manager_obj = openstack_models.Group.objects.get(name='Manager')
    compute_obj = openstack_models.Group.objects.get(name='Compute')
    manager_nodes = manager_obj.host_set.select_related()
    compute_nodes = compute_obj.host_set.select_related()

    return render(request, 'openstack/dashboards/neutron_status.html',
                  {
                      'manager_nodes': manager_nodes,
                      'compute_nodes': compute_nodes,
                  })


def dashboards_nova_status(request):
    return render(request, 'openstack/dashboards/nova_status.html')


def dashboards_cinder_status(request):
    return render(request, 'openstack/dashboards/cinder_status.html')


def dashboards_ceph_status(request):
    return render(request, 'openstack/dashboards/ceph_status.html')
