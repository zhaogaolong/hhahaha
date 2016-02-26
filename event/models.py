from django.db import models
from openstack import models as openstack_models
# Create your models here.


class Event(models.Model):
    event_time = models.DateTimeField(auto_now_add=True)
    event_models = models.CharField(max_length=1024)
    event_content = models.CharField(max_length=2048)
    event_node = models.ForeignKey(openstack_models.Host,
                                   null=True,
                                   blank=True
                                   )
