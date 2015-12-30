from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
import get_openstack_info


def info(request):
    b = get_openstack_info.Token()
    b.get_token()
    b.get_endpoint()
    b.get_service()
    b.add_hosts('192.168.201.3')
    b.add_nova_host()
    return HttpResponse('Openstack Info')