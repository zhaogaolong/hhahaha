#!/usr/bin/env python
# coding:utf8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from alarm import models as alarm_models
from event import models as event_models
from one_finger import settings


class Mail():
    def __init__(self, event_id, status):
        self.mail_user = settings.MAIL_USER
        self.mail_password = settings.MAIL_PASSWORD
        self.mail_server = settings.MAIL_SERVER
        self.event_id = event_id
        ev = event_models.Event.objects.get(id=self.event_id)
        self.notifier = settings.NOTIFIER
        self.status = status

        self.content = u'时间: %s ' % ev.event_time + '<br>' \
                       + u'节点: %s' % ev.event_node.hostname + '<br>' \
                       + u'模块: %s' % ev.event_type.name + '<br>' \
                       + u'级别: %s' % ev.level + '<br>' \
                       + u'状态: %s' % self.status + '<br>' \
                       + ev.event_content + ' \n\n'
        self.msg = MIMEMultipart()
        self.msg.attach(MIMEText(
            self.content,
            _subtype='html',
            _charset='utf-8',
        ))
        self.msg['Subject'] = settings.MAIL_HEARD % {'level': ev.level}
        self.msg['From'] = self.mail_user
        self.msg['To'] = self.notifier

    def send_mail(self):
        try:
            smtp_server = smtplib.SMTP()
            smtp_server.connect(settings.MAIL_SERVER)
            smtp_server.login(self.mail_user, self.mail_password)
            smtp_server.sendmail(self.mail_user,
                                 self.notifier,
                                 self.msg.as_string())
            smtp_server.close()
            self.status = 'yes'
        except:
            self.status = 'no'

        self.save_db()

    def save_db(self):
        dic = self.db_dic()
        alarm_event = alarm_models.Event(**dic)
        alarm_event.save()

    def db_dic(self):
        dic = {
            'severity': event_models.Event.objects.get(id=self.event_id).level,
            'description_id': self.event_id,
            'mail_msg': self.content,
            'status': self.status
        }
        return dic

