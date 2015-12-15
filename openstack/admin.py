from django.contrib import admin
from openstack import models

# Register your models here.
#
# admin.site.register(models.Openstack_keystone_auth)
# admin.site.register(models.Openstack_keystone_endpoint)


admin.site.register(models.Openstack_status)

admin.site.register(models.Host)

admin.site.register(models.Group)

admin.site.register(models.Ceph_monitor_service_status)
admin.site.register(models.Ceph_monitor_node_service_status)
admin.site.register(models.Ceph_osd_service_status)

admin.site.register(models.Rabbitmq_service_status)
admin.site.register(models.Rabbitmq_node_service_status)

admin.site.register(models.Pacemaker_node_service_status)

admin.site.register(models.Redis_service_status)
admin.site.register(models.Redis_node_service_status)

admin.site.register(models.Mysql_service_status)
admin.site.register(models.Mysql_node_service_status)

admin.site.register(models.Nova_manager_service_status)
admin.site.register(models.Nova_manager_node_service_status)
admin.site.register(models.Nova_compute_service_status)

admin.site.register(models.Neutron_manager_service_status)
admin.site.register(models.Neutron_manager_node_service_status)
admin.site.register(models.Neutron_compute_service_status)