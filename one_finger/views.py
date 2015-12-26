
from get_openstack_info import Token
from django.shortcuts import render,HttpResponse




from cinderclient.v1 import client as cinder_client



# from openstack_dashboard.api import cinder
# Create your views here.

def index(request):
    return render(request, 'one_finger/index.html')


def base(request):
    return  render(request, 'one_finger/base.html')

def back(request):
    return  render(request, 'one_finger/index_back.html')

def get_openstack_info(request):
    b = Token()
    # b.get_token()
    # b.get_endpoint()
    # b.get_service()
    b.get_host()
    return HttpResponse('None')


# def get_cinder_service(request):
#     b = cinder.cinder_client()
