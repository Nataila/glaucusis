#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

from django.db.models import Q
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

from apps.db.models import Instrument

@login_required(login_url='/login/')
def index(request, template):
    user_id = request.user.id
    search = request.GET.get('search', '')
    instr_data = []
    if search:
        instr_data = Instrument.objects.filter(Q(instrument_id__exact=search) | Q(instrument_name__exact=search))
    content = {
        'instr_data': instr_data,
        'request': request
    }
    return TemplateResponse(request, template, content)
