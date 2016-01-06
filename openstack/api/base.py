#!/usr/bin/env python
# coding:utf8

from one_finger import  models as one_finger_models
from django.conf import settings


class Base(object):
    pass


class KeyStoneBase(Base):
    version = 2


class NovaBase(Base):
    pass


def url_for(service_name, endpoint_type=None):
    # 获取 endpoint_url_type
    endpoint_url_type = settings.ACCEPT_URL
    region = settings.REGION
    url = get_url_for_service(service_name=service_name,
                              region=region,
                              endpoint_url_type=endpoint_url_type
                              )
    if url:
        return url
    else:
        raise 'unknown service %s' % service_name


def get_url_for_service(service_name, region, endpoint_url_type):

    # 获取service的id
    service_id = one_finger_models.OpenStackKeystoneService.objects.get(
        name=service_name,
    ).service_id

    # 通过service_id 获取endpoint的对象
    service_obj = one_finger_models.OpenStackKeyStoneEndpoint.objects.get(
        service_id=service_id,
        region=region,
    )

    url = getattr(service_obj, endpoint_url_type)

    if 'tenant_id' in url:
        # 如果url 里面需要tenant_id 就添加tenant_id 后再返回结果
        tenant_id = one_finger_models.OpenStackKeystoneAuth.objects.get(
            os_tenant_name='admin'
        ).tenant_id

        url = url % {'tenant_id':tenant_id}

        return url

    else:
        # 那就直接返回url
        return url


class CinderBase(Base):
    pass


class NeutronBase(Base):
    pass


class CeilOmeTerBase(Base):
    pass


class GlanceBase(Base):
    pass

