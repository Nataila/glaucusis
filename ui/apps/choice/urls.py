#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-06


from django.conf.urls import url, patterns

urlpatterns = patterns('apps.choice.views',
    url('^$', 'choice', {'template': 'choice/choice.html'}, 'choice')
)
