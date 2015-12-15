# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenStackKeystoneAuth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os_no_cache', models.BooleanField(default=True)),
                ('os_tenant_name', models.CharField(default=b'admin', max_length=64)),
                ('os_username', models.CharField(default=b'admin', max_length=64)),
                ('os_password', models.CharField(default=b'admin', max_length=64)),
                ('auth_url', models.URLField()),
                ('os_auth_strategy', models.CharField(default=b'keystone', max_length=64)),
                ('cinder_endpoint_type', models.CharField(default=b'publicURL', max_length=64)),
                ('glance_endpoint_type', models.CharField(default=b'publicURL', max_length=64)),
                ('keystone_endpoint_type', models.CharField(default=b'publicURL', max_length=64)),
                ('nova_endpoint_type', models.CharField(default=b'publicURL', max_length=64)),
                ('neutron_endpoint_type', models.CharField(default=b'publicURL', max_length=64)),
                ('token', models.CharField(max_length=64, null=True, blank=True)),
                ('tenant_id', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpenStackKeyStoneEndpoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('endpoint_id', models.CharField(max_length=64)),
                ('service_id', models.CharField(max_length=64)),
                ('region', models.CharField(max_length=64)),
                ('public_url', models.CharField(max_length=64)),
                ('internal_url', models.CharField(max_length=64)),
                ('admin_url', models.CharField(max_length=64)),
                ('enabled', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='OpenStackKeystoneService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=64)),
                ('enabled', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceStatusUrlSuffix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=64)),
                ('api', models.CharField(max_length=64)),
                ('service', models.CharField(max_length=64)),
                ('token', models.CharField(max_length=64, null=True, blank=True)),
                ('endpoint', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
    ]
