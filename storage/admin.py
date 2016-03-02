from django.contrib import admin
from storage import models
# Register your models here.
admin.site.register(models.CephStatus)
admin.site.register(models.CephMonitorStatus)
admin.site.register(models.CephOsdStatus)
