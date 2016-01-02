#!/usr/bin/env python
# coding:utf8

from cinderclient.v1 import client as cinder_client
from cinderclient import client




# from openstack_dashboard.api import cinder
# b = {}
# c = cinder.cinderclient(b)






# b = [u'admin',
#      '796a5ceaf5fd4543b010d69d5732bbd6',
#      u'239667eee2124453b69309e9cefae142',
#      u'http://192.168.0.2:8776/v1/239667eee2124453b69309e9cefae142',
#      False,
#      None,
#      True
#      ]
#
c = cinder_client.Client('admin',
                         'c9de9164528f4f86b64172fa1bead1de',
                         project_id='239667eee2124453b69309e9cefae142',
                         auth_url='http://192.168.254.242:8776/v1/239667eee2124453b69309e9cefae142',
                         insecure=False,
                         cacert = None,
                         http_log_debug = True)
c.client.auth_token = 'c9de9164528f4f86b64172fa1bead1de'
c.client.management_url = 'http://192.168.254.242:8776/v1/239667eee2124453b69309e9cefae142'
#
# print c.volumes.list()

for service in c.services.list():
    print 'service.host:', service.host





