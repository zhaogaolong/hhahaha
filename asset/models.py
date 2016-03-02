from django.db import models

# Create your models here.


class Host(models.Model):
    hostname = models.CharField(max_length=64)
    host_group = models.ManyToManyField('Group')
    ip_manager = models.GenericIPAddressField(max_length=64, blank=True, null=True)
    ip_storage = models.GenericIPAddressField(max_length=64, blank=True, null=True)
    ip_public = models.GenericIPAddressField(max_length=64, blank=True, null=True)
    ip_pxe = models.GenericIPAddressField(max_length=64, blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    # password = models.CharField(max_length=64, blank=True, null=True)
    remark = models.CharField(max_length=1024,
                              null=True,blank=True)
    status_level = (
        ('Ok', "ok"),
        ('Warning ', "Warning"),
        ('Error ', "Error"),
    )
    status = models.CharField(choices=status_level, max_length=64, blank=True, null=True)

    def __unicode__(self):
        return self.hostname


class Group(models.Model):
    name = models.CharField(max_length=64)
    remark = models.CharField(max_length=1024,
                              null=True,blank=True)
    def __unicode__(self):
        return self.name


class SystemInfo(models.Model):
    host = models.ForeignKey('Host')
    cpu_status = models.FloatField(max_length=10, default=00.00)
    mem_status = models.FloatField(max_length=10, default=00.00)
    uptime = models.CharField(max_length=64)

    def __unicode__(self):
        return self.host_id