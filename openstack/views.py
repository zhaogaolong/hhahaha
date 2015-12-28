from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
import get_openstack_info


def info(request):
    b = get_openstack_info.Token()
    b.get_token()
    b.get_endpoint()
    b.get_service()
    b.get_hosts()
    return HttpResponse('Openstack Info')