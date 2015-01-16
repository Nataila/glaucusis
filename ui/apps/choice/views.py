#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

from apps.db.models import Instrument, Exchange, Country

@login_required(login_url='/login/')
def choice(request, template):
    result = {}
    exchange_to_country = {}
    mid = {}
    final_result = []
    instr_data = Instrument.objects.all()
    exchange_data = Exchange.objects.all()
    country_data = Country.objects.all()
    for i in country_data:
        exchange_to_country[i.country_name] = []
    for i in exchange_data:
        result[i.exchange_name] = []
    for i in instr_data:
        mid[i.exchange_id.country_iso_code.country_name] = []
    for i in instr_data:
        exchange_to_country[i.exchange_id.country_iso_code.country_name].append(i.exchange_id.exchange_name)
        result[i.exchange_id.exchange_name].append(i.instrument_name)
    for i in exchange_to_country:
        exchange_to_country[i] = set(exchange_to_country[i])
    for i in exchange_to_country:
        for j in exchange_to_country[i]:
            if result.get(j, []):
                instr = result[j]
            else:
                instr = []
            mid[i].append({'exchange_name': j, 'instrument': instr})
    for i in mid:
        final_result.append({'country': i, 'data': mid[i]})
    content = {
        'request': request,
        'final_result': final_result
    }

    return TemplateResponse(request, template, content)
