#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-08

from django.conf.urls import url, patterns

urlpatterns = patterns('apps.news.views',
    url('^$', 'news', {'template': 'news/news.html'}, 'news')
)
