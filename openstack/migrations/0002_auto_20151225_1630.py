# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CephMonitorServiceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='CephOsdServiceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('osd_name', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='CephStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('monitor_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('osd_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='CinderApiStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='CinderSchedulerStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='CinderStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_api_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_volume_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('cinder_scheduler', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='CinderVolumeStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='MysqlServiceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='MysqlStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='NeutronComputeServiceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('neutron_river_type', models.CharField(max_length=64, choices=[(b'Open_vSwitch', b'Open_vSwitch'), (b'Linux_bridge ', b'Linux_bridge')])),
                ('host_name', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='NeutronManagerServiceStatus',
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
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='NeutronStatus',
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
            ],
        ),
        migrations.CreateModel(
            name='NovaComputeServiceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('libvirtd_staus', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('group_name', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='NovaManagerServiceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_api_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_no_vnc_proxy_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_console_auth_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_scheduler_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_conductor_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('nova_license_status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='NovaStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='PacemakerServiceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='PacemakerStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='RabbitmqServiceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='RabbitMqStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=54)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='RedisServiceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.CreateModel(
            name='RedisStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=64, choices=[(b'Ok', b'ok'), (b'Warning ', b'Warning'), (b'Error ', b'Error')])),
                ('host', models.ForeignKey(to='openstack.Host')),
            ],
        ),
        migrations.RenameModel(
            old_name='Openstack_status',
            new_name='OpenStackStatus',
        ),
        migrations.RemoveField(
            model_name='ceph_monitor_node_service_status',
            name='monitor_host',
        ),
        migrations.RemoveField(
            model_name='ceph_monitor_service_status',
            name='monitor_host',
        ),
        migrations.RemoveField(
            model_name='ceph_osd_service_status',
            name='osd_host',
        ),
        migrations.RemoveField(
            model_name='cinder_minager_service_status',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='cinder_node_service_status',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='mysql_node_service_status',
            name='mysql_group',
        ),
        migrations.RemoveField(
            model_name='mysql_service_status',
            name='mysql_group',
        ),
        migrations.RemoveField(
            model_name='neutron_compute_service_status',
            name='host_name',
        ),
        migrations.RemoveField(
            model_name='neutron_manager_node_service_status',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='neutron_manager_service_status',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='nova_compute_service_status',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='nova_manager_node_service_status',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='nova_manager_service_status',
            name='group_name',
        ),
        migrations.DeleteModel(
            name='Openstack_keystone_service_list',
        ),
        migrations.RemoveField(
            model_name='pacemaker_node_service_status',
            name='rabbitmq_group',
        ),
        migrations.RemoveField(
            model_name='pacemaker_service_status',
            name='rabbitmq_group',
        ),
        migrations.RemoveField(
            model_name='rabbitmq_node_service_status',
            name='rabbitmq_group',
        ),
        migrations.RemoveField(
            model_name='rabbitmq_service_status',
            name='rabbitmq_group',
        ),
        migrations.RemoveField(
            model_name='redis_node_service_status',
            name='redis_group',
        ),
        migrations.RemoveField(
            model_name='redis_service_status',
            name='redis_group',
        ),
        migrations.DeleteModel(
            name='Ceph_monitor_node_service_status',
        ),
        migrations.DeleteModel(
            name='Ceph_monitor_service_status',
        ),
        migrations.DeleteModel(
            name='Ceph_osd_service_status',
        ),
        migrations.DeleteModel(
            name='cinder_minager_service_status',
        ),
        migrations.DeleteModel(
            name='cinder_node_service_status',
        ),
        migrations.DeleteModel(
            name='Mysql_node_service_status',
        ),
        migrations.DeleteModel(
            name='Mysql_service_status',
        ),
        migrations.DeleteModel(
            name='Neutron_compute_service_status',
        ),
        migrations.DeleteModel(
            name='Neutron_manager_node_service_status',
        ),
        migrations.DeleteModel(
            name='Neutron_manager_service_status',
        ),
        migrations.DeleteModel(
            name='Nova_compute_service_status',
        ),
        migrations.DeleteModel(
            name='Nova_manager_node_service_status',
        ),
        migrations.DeleteModel(
            name='Nova_manager_service_status',
        ),
        migrations.DeleteModel(
            name='Pacemaker_node_service_status',
        ),
        migrations.DeleteModel(
            name='Pacemaker_service_status',
        ),
        migrations.DeleteModel(
            name='Rabbitmq_node_service_status',
        ),
        migrations.DeleteModel(
            name='Rabbitmq_service_status',
        ),
        migrations.DeleteModel(
            name='Redis_node_service_status',
        ),
        migrations.DeleteModel(
            name='Redis_service_status',
        ),
    ]
