# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ceph_monitor_node_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='Ceph_monitor_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='Ceph_osd_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('osd_name', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='cinder_minager_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_api_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_volume_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_scheduler_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='cinder_node_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_api_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_volume_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_scheduler_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=64)),
                ('ip_manager', models.GenericIPAddressField()),
                ('ip_storage', models.GenericIPAddressField()),
                ('ip_public', models.GenericIPAddressField(null=True, blank=True)),
                ('ip_pxe', models.GenericIPAddressField()),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('group', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Mysql_node_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('mysql_group', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Mysql_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('mysql_group', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Neutron_compute_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_river_type', models.CharField(max_length=64, choices=[(b'Open_vSwitch', b'Open_vSwitch'), (b'Linux_bridge ', b'Linux_bridge')])),
                ('host_name', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Neutron_manager_node_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_api_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_network_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_metadata_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_Loadbalancer_status', models.IntegerField(null=True, blank=True)),
                ('neutron_l3_status', models.CharField(blank=True, max_length=64, null=True, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_DHCP_status', models.CharField(blank=True, max_length=64, null=True, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_river_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_scheduler_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('group_name', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Neutron_manager_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_api_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_network_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_metadata_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_Loadbalancer_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_l3_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_DHCP_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_river_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_scheduler_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('group_name', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Nova_compute_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('libvirtd_staus', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('group_name', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Nova_manager_node_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_api_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_novncproxy_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_consoleauth_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_scheduler_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_conductor_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_license_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('group_name', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Nova_manager_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_api_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_novncproxy_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_consoleauth_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_scheduler_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_conductor_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_license_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('group_name', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Openstack_keystone_service_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Openstack_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('available_proportion', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pacemaker_node_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('rabbitmq_group', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Pacemaker_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('rabbitmq_group', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Rabbitmq_node_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('rabbitmq_group', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Rabbitmq_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('rabbitmq_group', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Redis_node_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('redis_group', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Redis_service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('redis_group', models.ForeignKey(to='openstack.Group')),
            ],
        ),
        migrations.AddField(
            model_name='cinder_node_service_status',
            name='group_name',
            field=models.ForeignKey(to='openstack.Host'),
        ),
        migrations.AddField(
            model_name='cinder_minager_service_status',
            name='group_name',
            field=models.ForeignKey(to='openstack.Group'),
        ),
        migrations.AddField(
            model_name='ceph_osd_service_status',
            name='osd_host',
            field=models.ForeignKey(to='openstack.Host'),
        ),
        migrations.AddField(
            model_name='ceph_monitor_service_status',
            name='monitor_host',
            field=models.ForeignKey(to='openstack.Group'),
        ),
        migrations.AddField(
            model_name='ceph_monitor_node_service_status',
            name='monitor_host',
            field=models.ForeignKey(to='openstack.Host'),
        ),
    ]
