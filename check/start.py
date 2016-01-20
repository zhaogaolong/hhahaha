#!/usr/bin/env python
# coding:utf8
import time
import os
import sys
import time
# config allow this is py invoke django models
Base_dir = "/".join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1])
sys.path.append(Base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "one_finger.settings")
from openstack import models
import django
django.setup()
# config allow this is py invoke django models

# check models
from cloud import nova
from cloud import neutron
from cloud import cinder


if __name__ == "__main__":
    cc = cinder.Check(models)
    # while True:
    #     nc = nova.Check(models)
    #     nc = neutron.Check(models)
    #     cc = cinder.Check(models)
    #     time.sleep(3)

