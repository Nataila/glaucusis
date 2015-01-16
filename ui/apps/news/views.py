#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def news(request, template):
    return TemplateResponse(request, template, {'request': request})