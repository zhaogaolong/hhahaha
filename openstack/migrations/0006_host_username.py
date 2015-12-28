# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0005_remove_host_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='username',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
