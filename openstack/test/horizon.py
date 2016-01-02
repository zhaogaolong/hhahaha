#!/usr/bin/env python
# coding:utf8


from cinderclient.v1 import client as cinder_client
from cinderclient import utils
import pdb


def cinderclient():
    insecure = False
    cacert = None
    cinder_url = "http://192.168.254.242:8776/v1/239667eee2124453b69309e9cefae142"

    token_id = '56ea226c9150497295f6ac7fa854306f'
    tenant_id = '239667eee2124453b69309e9cefae142'
    c = cinder_client.Client('admin',
                             token_id,
                             project_id=tenant_id,
                             auth_url=cinder_url,
                             insecure=insecure,
                             cacert=cacert,
                             http_log_debug=True)
    c.client.auth_token = token_id
    c.client.management_url = cinder_url
    return c



def volume_list(search_opts=None):
    """
    To see all volumes in the cloud as an admin you can pass in a special
    search option: {'all_tenants': 1}
    """
    c_client = cinderclient()
    if c_client is None:
        return []
    # print c_client.volumes.list(search_opts=search_opts)
    return c_client.volumes.list(search_opts=search_opts)


def do_service_list(cs, args):
    """Lists all services. Filter by host and service binary."""
    result = cs.services.list(host=args.host, binary=args.binary)
    columns = ["Binary", "Host", "Zone", "Status", "State", "Updated_at"]
    # NOTE(jay-lau-513): we check if the response has disabled_reason
    # so as not to add the column when the extended ext is not enabled.
    if result and hasattr(result[0], 'disabled_reason'):
        columns.append("Disabled Reason")
    if result:
        print 'OKKKKKKKKK'
    utils.print_list(result, columns)

class args():
    host = ['rbd:volumes', 'rbd:volumes@capacity']
    binary = ['cinder-scheduler', 'cinder-volume']




if __name__ == '__main__':
    for volume in volume_list():
        print volume.id

    cs = cinderclient()
    a = cs.services.list(host='rbd:volumes', binary='cinder-scheduler')
    # print type(a)
    # for i in a:
    #     print i.host
    # for service in cs.services.list():
        # print service.host
        # print service.binary

    ar = args()
    print ar.host ,ar.binary

    do_service_list(cs, args)