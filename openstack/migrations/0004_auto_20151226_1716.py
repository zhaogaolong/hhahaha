# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0003_auto_20151225_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='ip_manager',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='ip_pxe',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='ip_storage',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='status',
            field=models.CharField(blank=True, max_length=64, null=True, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')]),
        ),
    ]
