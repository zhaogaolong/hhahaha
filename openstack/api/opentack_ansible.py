#!/usr/bin/env python
# coding:utf8


import pdb
import ansible.runner
from one_finger.cloud_logging import cloud_logging as logging
log = logging.logger


class CmmAndRun():
    def __init__(self, module_name='shell', host=None, cmd=None):
        self.username = 'root'
        self.module_name = module_name
        self.host = host
        self.cmd = cmd

    def start(self):
        runner = ansible.runner.Runner(
            module_name=self.module_name,
            module_args=self.cmd,
            pattern=self.host,
        )
        log.debug('ansible %s RunCommand: %s' % (self.host, self.cmd))

        datastructure = runner.run()

        if not datastructure['contacted'][self.host]['rc']:
            data = datastructure['contacted'][self.host]['stdout']
            # pdb.set_trace()
            return data

        else:
            return None


if __name__ == '__main__':
    ac = CmmAndRun(host='192.168.201.4', cmd='date')
    # print ac.start()