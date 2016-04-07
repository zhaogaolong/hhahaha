from django.shortcuts import render, HttpResponseRedirect,HttpResponse

from asset import models as asset_models
from base.api import remote_execution
import json
# Create your views here.


def ssh_host(request, host_id):
    print 'host ip is a aaaaaaaaaaaaaaa'

    port = 4200 + int(host_id)
    host_ip = asset_models.Host.objects.get(id=host_id).ip_manager
    check_cmd = 'netstat -antp |grep -e %s' % port
    datastructure = remote_execution.run(cmd=check_cmd, host_ip='127.0.0.1')

    # import pdb
    # pdb.set_trace()
    if datastructure['contacted']['127.0.0.1']['rc']:
        cmd = "shellinaboxd -p %s --css=/etc/shellinaboxd/shellinaboxd.css -t" \
              " -s /:SSH:%s -b " % (port, host_ip)
        b = remote_execution.run(cmd=cmd,
                                 host_ip='127.0.0.1')

        url = 'http://%s:%s/?u=root&p=r00tme' % ('192.168.254.230', port)
        print 'if resturn'
        ssh_url = {'url': url}
        return HttpResponse(json.dumps(ssh_url))
    else:
        url = 'http://%s:%s/?u=root&p=r00tme' % ('192.168.254.230', port)
        print 'return'
        ssh_url = {'url': url}
        return HttpResponse(json.dumps(ssh_url))







