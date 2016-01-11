#!/usr/bin/env python
# coding:utf8
from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

######

from models import OpenStackKeystoneAuth
from openstack.views import info


# ----------用户登录登出-----------
def account_login(request):
    # print request.method
    if request.method == 'GET':
        return render(request, 'one_finger/login.html')

    else:
        # print request.POST
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(username=username,password=passwd)
        if user is not None:
            login(request, user)
            user.userprofile.online = True
            user.userprofile.save()

            if not OpenStackKeystoneAuth.objects.all():
                return render(request, 'one_finger/input_info.html')

            return HttpResponseRedirect("/")
        else:
            return render(request, 'one_finger/login.html', {
                'login_err': "Wrong username or password!"
            })


def input_info(request):
    if request.method == 'GET':
        return render(request, 'one_finger/input_info.html')
    else:
        if OpenStackKeystoneAuth.objects.all():
            return HttpResponseRedirect('/')
        auth_dic = {
            'os_tenant_name': request.POST.get('os_username'),
            'os_username': request.POST.get('os_username'),
            'os_password': request.POST.get('os_password'),
            'auth_url': request.POST.get('auth_url'),
            'os_auth_strategy': 'keystone',
            'cinder_endpoint_type': request.POST.get('url_type'),
            'glance_endpoint_type': request.POST.get('url_type'),
            'keystone_endpoint_type': request.POST.get('url_type'),
            'nova_endpoint_type': request.POST.get('url_type'),
            'neutron_endpoint_type': request.POST.get('url_type'),
        }

        OpenStackKeystoneAuth.objects.create(**auth_dic)

        return render(request, 'openstack/openstack_info.html', {
            'manager_ip': request.POST.get('manager_ip')
        })

@login_required
def index(request):
    return render(request, 'one_finger/index.html')




@login_required
def back(request):
    return render(request, 'one_finger/test/index_back.html')


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'one_finger/login.html')