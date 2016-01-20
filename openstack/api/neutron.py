#!/usr/bin/env python
# coding:utf8
from neutronclient.v2_0 import client as neutron_client
####
from openstack.api import base
from openstack.api import keystone
from openstack.api import base
from openstack import models


from one_finger.cloud_logging import cloud_logging as logging
log = logging.logger


def neutronclient(endpoint_url=base.url_for('neutron')):
    kc = keystone.KeyStone()
    token = kc.token
    insecure = False
    cacert = None
    c = neutron_client.Client(token=token,
                              endpoint_url=endpoint_url,
                              insecure=insecure, ca_cert=cacert)

    # print endpoint_url
    return c


def agent_list():
    return neutronclient().list_agents()


