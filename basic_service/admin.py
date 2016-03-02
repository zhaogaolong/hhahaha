from django.contrib import admin
from basic_service import models
# Register your models here.
admin.site.register(models.MysqlStatus)
admin.site.register(models.MysqlServiceStatus)
admin.site.register(models.RabbitMqStatus)
admin.site.register(models.RabbitmqServiceStatus)
admin.site.register(models.RedisStatus)
admin.site.register(models.RedisServiceStatus)
admin.site.register(models.PacemakerStatus)
admin.site.register(models.PacemakerServiceStatus)
