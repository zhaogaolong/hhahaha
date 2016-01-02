#!/usr/bin/env python
# coding:utf8
# 这是获取状态信息
import urllib2
import json




data = json.dumps({
    "auth":
    {
        'tenantName': 'admin',
        'passwordCredentials':
        {
            'username': 'admin',
            'password': 'admin'
            }
        }
    })

# data = json.dumps({
#     "auth":{
#        'tenantName': 'admin',
#         'passwordCredentials': {
#
#             'username': 'admin',
#             'password': 'admin',
#         }
#     }
# })
request = urllib2.Request(
     'http://192.168.1.106:35357/v2.0',
     data=data,
     headers={'Content-type': 'application/json'}
)




# request = urllib2.Request('http://192.168.1.106:5000/v2.0/tokens',
#                         data=data,
#                         headers={
#                             'Content-type': 'application/json'
#                             })
request = urllib2.Request('http://192.168.1.106:5000/v2.0/tokens',
        data=data,
        headers={
            'Content-type': 'application/json'
            })

# print 're', urllib2.urlopen(request, timeout=self.get_timeout('keystone')).read()
print 'data_1dddd', json.loads(urllib2.urlopen(request, timeout=5).read())
                    # json.loads(urllib2.urlopen(request, timeout=5).read())