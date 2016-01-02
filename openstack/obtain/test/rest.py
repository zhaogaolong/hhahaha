#!/usr/bin/env python
#coding:utf8


#!/usr/bin/python
import time
import urllib2
import sys
#import simplejson as json
import json
import ConfigParser
import logging





LOGGING_LEVELS = {
    'CRITICAL': logging.CRITICAL,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG
}

def get_logger(level):
    logger = logging.getLogger()
    ch = logging.StreamHandler(sys.stdout)
    logger.setLevel(LOGGING_LEVELS[level])
    logger.addHandler(ch)
    return logger

class OSAPI(object):
    """Openstack API"""

    def __init__(self):
        self.username = "admin"
        self.password = "admin"
        self.tenant_name = "admin"
        self.endpoint_keystone = ["http://192.168.1.106:35357/v2.0"]
        self.token = None
        self.tenant_id = None
        self.get_token()


    def get_token(self):
        data = json.dumps({
            "auth":
            {
                'tenantName': self.tenant_name,
                'passwordCredentials':
                {
                    'username': self.username,
                    'password': self.password
                    }
                }
            })

        print 'type', type(data)
        fail_services = 0
        for keystone in self.endpoint_keystone:
            try:
                request = urllib2.Request('http://192.168.1.106:5000/v2.0/tokens',
                        data=data,
                        headers={
                            'Content-type': 'application/json'
                            })
                print 'request_data', request.data
                print 'dataaa', urllib2.urlopen(request, timeout=5)
                data = json.loads(urllib2.urlopen(request, timeout=5).read())
                print 'data_2', data
                self.token = data['access']['token']['id']
                self.tenant_id = data['access']['token']['tenant']['id']

                return
            except Exception as e:
                print 'hhhhhhhhhhhhhhhhhhhhhh',e
                self.logger.debug("Got exception '%s'" % e)
                fail_services += 1


        if fail_services == len(self.endpoint_keystone):
            sys.exit(1)

    def check_api(self, url):
        try:
            request = urllib2.Request(url,
                    headers={
                        'X-Auth-Token': self.token,
                        })
            print 'dddddddddddddddd', urllib2.urlopen(request, timeout=5).read()
            print 'check_api',request
        except Exception as e:

            print 'Exception',e
            sys.exit(1)

def main():
    print 'start get token'
    API = OSAPI()
    print 'API', API
    map = 'v2/%(tenant_id)s/flavors'

    url = 'http://%s:%s/%s' % ('192.168.1.106', 8774, map)

    url = url % API.__dict__
    API.check_api(url)

if __name__ == "__main__":
    main()