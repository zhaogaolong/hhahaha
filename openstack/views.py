from django.shortcuts import render

# Create your views here.

import json

#####
from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from openstack import get_openstack_info
from openstack.page import cloud,ceph,nova,neutron,cinder


def info(request):
    # b = get_openstack_info.GetOpenStackInfo()
    b = get_openstack_info.GetOpenStackInfo()
    b.get_endpoint()
    b.get_service()
    b.add_hosts('192.168.201.3')
    b.add_nova_host()
    b.add_cinder_host()
    b.add_neutron_host()
    b.add_ceph_osd_host()
    b.add_ceph_mon_host()
    # b.add_mysql_host()

    return HttpResponse('Openstack Info')


def test(request):
    return render(request, 'openstack/test.html')


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


