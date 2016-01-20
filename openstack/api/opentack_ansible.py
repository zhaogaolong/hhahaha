#!/usr/bin/env python
# coding:utf8


# import pdb
import ansible.runner
from one_finger.cloud_logging import cloud_logging as logging
log = logging.logger


class CmmAndRun():
    def __init__(self, module_name='shell', host=None, cmd=None, timeout=20):
        self.username = 'root'
        self.module_name = module_name
        self.host = host
        self.cmd = cmd
        self.timeout = timeout

    def start(self):
        runner = ansible.runner.Runner(
            module_name=self.module_name,
            module_args=self.cmd,
            pattern=self.host,
            timeout=self.timeout,
        )
        log.debug('ansible %s RunCommand: %s' % (self.host, self.cmd))

        # import pdb
        # pdb.set_trace()

        datastructure = runner.run()
        # print datastructure

        log.debug('ansible sttout %s' % datastructure)

        # print datastructure
        if not datastructure['contacted'][self.host]['rc']:
            data = datastructure['contacted'][self.host]['stdout']
            return data
        else:
            return None


if __name__ == '__main__':
    ac = CmmAndRun(host='172.16.254.1', cmd='date')
    print ac.start()