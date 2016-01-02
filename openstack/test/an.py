#!/usr/bin/env python
# coding:utf8

import ansible.runner

runner = ansible.runner.Runner(
    module_name='shell',
    module_args='dasste',
    # timeout=10,
    # forks=10,
    pattern='192.168.201.4',
    # transport='smart',
    # check=False,
    # become=False,
    # become_method='sudo',
)


datastructure = runner.run()
# print datastructure['contacted']

for k, v in datastructure['contacted'].items():
    print k
    print v