#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

from apps.libs.views import get_default_list

@login_required(login_url='/login/')
def simulate(request, template):
  default_result = get_default_list(request)
  content = {
      'request': request,
      'default_result': default_result
  }
  return TemplateResponse(request, template, content)
