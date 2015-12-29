#!/usr/bin/env python
# coding:utf8

import ansible.runner

runner = ansible.runner.Runner(
    module_name='setup',
    module_args='',
    host_list='hosts',
    # pattern='web*',
    forks=10
)

datastructure = runner.run()
print datastructure