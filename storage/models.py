from django.db import models
from asset.models import Host
# Create your models here.
# ####ceph##########
status_level = (
    ("up", "up"),
    ("warning", "warning"),
    ("down", "down"),
)

mode_status_level = (
        ("up", "up"),
        ("warning", "warning"),
        ("critical", "critical"),
        ("down", "down"),
    )


class CephStatus(models.Model):
    # this is a ceph service tables
    status = models.CharField(choices=mode_status_level, max_length=64)
    monitor_status = models.CharField(choices=status_level, max_length=64)
    osd_status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.status


class CephMonitorStatus(models.Model):
    # this is a ceph monitor service tables
    host = models.ForeignKey(Host)
    mon_id = models.IntegerField()
    status = models.CharField(choices=status_level,
                              max_length=64,
                              blank=True,
                              null=True)

    def __unicode__(self):
        return self.host.hostname


class CephOsdStatus(models.Model):
    # this is a ceph osd service tables
    osd_name = models.CharField(max_length=64)
    host = models.ForeignKey(Host)
    status = models.CharField(choices=status_level, max_length=64)

    def __unicode__(self):
        return self.osd_name


