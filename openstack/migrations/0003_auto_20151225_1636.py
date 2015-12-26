# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0002_auto_20151225_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinderManagerStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_api_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_volume_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_scheduler', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.RemoveField(
            model_name='cinderapistatus',
            name='host',
        ),
        migrations.RemoveField(
            model_name='cinderschedulerstatus',
            name='host',
        ),
        migrations.RemoveField(
            model_name='cindervolumestatus',
            name='host',
        ),
        migrations.DeleteModel(
            name='CinderApiStatus',
        ),
        migrations.DeleteModel(
            name='CinderSchedulerStatus',
        ),
        migrations.DeleteModel(
            name='CinderVolumeStatus',
        ),
    ]
