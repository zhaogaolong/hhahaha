from django.contrib import admin
from openstack import models

# Register your models here.
#
# admin.site.register(models.Openstack_keystone_auth)
# admin.site.register(models.Openstack_keystone_endpoint)


admin.site.register(models.CloudStatus)

admin.site.register(models.Host)

admin.site.register(models.Group)


admin.site.register(models.NovaStatus)
admin.site.register(models.NovaManagerServiceStatus)
admin.site.register(models.NovaComputeServiceStatus)

admin.site.register(models.NeutronStatus)
admin.site.register(models.NeutronManagerServiceStatus)
admin.site.register(models.NeutronComputeServiceStatus)

admin.site.register(models.CinderStatus)
admin.site.register(models.CinderManagerStatus)

admin.site.register(models.CephStatus)
admin.site.register(models.CephMonitorStatus)
admin.site.register(models.CephOsdStatus)

admin.site.register(models.RabbitMqStatus)
admin.site.register(models.RabbitmqServiceStatus)

admin.site.register(models.PacemakerStatus)
admin.site.register(models.PacemakerServiceStatus)

admin.site.register(models.RedisStatus)
admin.site.register(models.RedisServiceStatus)

admin.site.register(models.MysqlStatus)
admin.site.register(models.MysqlServiceStatus)

