#!/usr/bin/env python
# coding:utf8

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from event import  models
# Create your views here.


@login_required
def check_event_log(request):
    events = models.Event.objects.order_by("-event_time")
    return render(request, 'event/check_log_v2.html', {
        'events': events,
    })