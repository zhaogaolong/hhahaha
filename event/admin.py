from django.contrib import admin

# Register your models here.
from event import models


class Event(admin.ModelAdmin):
    list_display = ('event_time', 'event_type_id', 'event_node_id', 'level', 'event_content')

admin.site.register(models.Event, Event)
admin.site.register(models.TopType)
admin.site.register(models.SecondType)
