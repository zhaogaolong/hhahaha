# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0004_auto_20151226_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='group',
        ),
    ]
