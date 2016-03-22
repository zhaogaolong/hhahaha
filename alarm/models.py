# coding:utf8
from django.db import models
from event import models as event_models

from asset import models as asset_models
# Create your models here.


class UserProfile(models.Model):
    name = models.CharField(u'名字', max_length=32)
    email = models.EmailField(u'邮箱')
    mobile = models.CharField(u'手机', max_length=32)
    wechart = models.CharField(u'微信', max_length=32)

    memo = models.TextField(u'备注', blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = "用户信息"

    def __unicode__(self):
        return self.name


class Event(models.Model):
    severity = models.CharField(max_length=64)
    time = models.TimeField(auto_now_add=True)
    # 绑定了event.models 就可以获取事件发主机的ID,
    # 所以就把主机给注释掉了
    # host = models.ForeignKey(asset_models.Host)
    description = models.ForeignKey(event_models.Event)

    # 填写联系人
    # notifier = models.ForeignKey('UserProfile')
    # email 的内容
    mail_msg = models.TextField(u'邮件内容')
    status = models.CharField(max_length=1024, blank=True, null=True)


