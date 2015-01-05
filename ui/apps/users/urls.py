#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url('^$', 'apps.users.views.auth_login', {'template': 'users/login.html'}, 'auth_login')
)
