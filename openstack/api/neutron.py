#!/usr/bin/env python
# coding:utf8
from neutronclient.V2_0 import client as neutron_client
####
from openstack.api import base
from openstack.api import keystone
from one_finger.cloud_logging import cloud_logging as logging
log = logging.logger








