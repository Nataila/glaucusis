#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05


from django.conf.urls import url, patterns

urlpatterns = patterns('apps.stock.views',
    url('^$', 'stock', {'template': 'stock/stock.html'}, 'stock')
)
