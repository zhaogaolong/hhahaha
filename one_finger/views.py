
from get_openstack_info import token
from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request, 'one_finger/index.html')


def base(request):
    return  render(request, 'one_finger/base.html')

def back(request):
    return  render(request, 'one_finger/index_back.html')

def get_openstack_info(request):
    b = token()
    b.get_endpoint()
    # b.get_service()
    return HttpResponse('None')