#!/usr/bin/env python
# coding:utf8


from cinderclient.v1 import client as cinder_client

cinder = cinder_client.Client('admin', 'admin', 'admin', 'http://192.168.1.106:35357/v2.0')
# cinder = cinder_client.Client(
#     username='admin',
#     api_key='79271fcb2f4946b9991125d54f00ba7d',
#     project_id='239667eee2124453b69309e9cefae142', # 着个是token的id
#     # auth_url='http://192.168.1.106:35357/v2.0'
#     auth_url='http://192.168.254.242:8776/v1/239667eee2124453b69309e9cefae142'
# )

#
# cinder = cinder_client.Client(
#     'admin',
#     '12a95db48bff4aef985caacd4d4bec94',
#     project_id='239667eee2124453b69309e9cefae142', # 着个是token的id
#     auth_url='http://192.168.254.242:8776/v1/239667eee2124453b69309e9cefae142',
#     insecure=False,
#     cacert=None,
#     http_log_debug=True
# )
# for volume in cinder.volumes.list():
#     print volume.id
cinder.volumes.list()
print cinder.services.list()






# c = cinder_client.Client('admin',
#                          'admin',
#                          project_id='74086863d3034f63897729d10b11560f',
#                          auth_url='http://192.168.1.106:35357/v2.0',
#                          insecure=False,
#                          cacert=None,
#                          http_log_debug=True)
# c.client.auth_token = 'admin'
# c.client.management_url = 'http://192.168.1.106:35357/v2.0'
# c.volumes.list()