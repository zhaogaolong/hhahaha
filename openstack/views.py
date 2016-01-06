from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from openstack import get_openstack_info


def info(request):
    # b = get_openstack_info.GetOpenStackInfo()
    b = get_openstack_info.GetOpenStackInfo()
    b.get_endpoint()
    b.get_service()
    b.add_hosts('192.168.201.3')
    b.add_nova_host()
    b.add_cinder_host()
    b.add_neutron_host()
    return HttpResponse('Openstack Info')