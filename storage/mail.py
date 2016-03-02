#!/usr/bin/env python
# coding:utf8
# 使用方式
# python mail.py to_mail_addr header msg




import smtplib
import sys


to = '965771261@qq.com'

gmail_user = 'monitor-no-reply@wing-cloud.com'
gmail_pwd = 'Deewiuytr!@#123'
smtpserver = smtplib.SMTP()
smtpserver.connect("smtp.mxhichina.com:25")
#smtpserver.helo()
# smtpserver.starttls()
#smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
# header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + sys.argv[2] + '\n'
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + 'test mail' + '\n'
#print (header)
msg = header + '\n ' + 'this is a test mail' + ' \n\n'
smtpserver.sendmail(gmail_user, to, msg)
#print ('done!')
smtpserver.close()
