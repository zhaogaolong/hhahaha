"""one_finger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from one_finger import views as one_finger_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', one_finger_views.index, name='index'),
    url(r'^base/', one_finger_views.base, name='base'),
    url(r'^back/', one_finger_views.back, name='back'),
    url(r'^get_openstack_info/', one_finger_views.get_openstack_info, name='get_openstack_info'),

]