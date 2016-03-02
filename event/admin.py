from django.contrib import admin

# Register your models here.
from event import models
admin.site.register(models.Event)
admin.site.register(models.TopType)
admin.site.register(models.SecondType)
