#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

import json
import sys

from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q

from apps.db.models import Instrument, News, Instrument, Price, Listinter, Interlistwatch
from apps.libs.views import get_default_list

reload(sys)
sys.setdefaultencoding('utf-8')

#@login_required(login_url='/login/')
#def stock(request, template):
#    result = []
#    user_id = request.user.id
#    attention_data = InstrWatch.objects.filter(user = user_id)
#    news = News.objects.all()
#    exchange = get_exchange(request)
#    for i in exchange:
#        result.append({'name': i, 'data': exchange[i]['instrument'], 'id': exchange[i]['id']})
#    content = {
#        'exchange_data': result,
#        'attention_data': attention_data,
#        'news': news,
#        'request': request
#    }
#    return TemplateResponse(request, template, content)
#
def get_exchange(request):
    exchange_list = []
    result = {}
    data = Instrument.objects.all()
    for i in data:
        exchange_list.append(i.exchange_id.exchange_name)
    for i in set(exchange_list):
        result[i] = {'id': '', 'instrument': []}
    for i in data:
        result[i.exchange_id.exchange_name]['instrument'].append({'id': i.id, 'name': i.instrument_name})
        result[i.exchange_id.exchange_name]['id'] = i.exchange_id.id
    return result

@login_required(login_url='/login/')
def stock(request, template):
    need_watch_instr = ''
    is_watched = True
    default_result = get_default_list(request)
    search_intr = request.GET.get('in_id', '')
    user_id = request.user.id
    if search_intr:
        need_watch_instr = Instrument.objects.get(id=search_intr)
        watched_list = Interlistwatch.objects.filter(Q(user=user_id), Q(inter_list=need_watch_instr))
        if watched_list:
            is_watched = False
    content = {
        'is_watched': is_watched,
        'need_watch_instr': need_watch_instr,
        'default_result': default_result,
        'request': request,
    }
    return TemplateResponse(request, template, content)

#@login_required(login_url='/login/')
#def get_instr_watch_list(request):
#    '''获取关注的列表以及列表下的股票
#    '''
#    watch_list = {}
#    list_result = []
#    mid_dict = {}
#    user = request.user.id
#    list_data = Interlistwatch.objects.filter(user=user)
#    user_watched = Listinter.objects.all()
#    for i in user_watched:
#        watch_list[i.name] = []
#    #for i in list_data:
#    #    watch_list[i.list_name.name] = []
#    for i in list_data:
#        watch_list[i.list_name.name].append({'name': i.inter_list.instrument_name, 'id': i.inter_list.id})
#        mid_dict[i.list_name.name] = i.id
#    for i in watch_list:
#        list_result.append({'list_name': i, 'data': watch_list[i]})
#    for i in list_result:
#        try:
#            i['id'] = mid_dict[i['list_name']]
#        except KeyError:
#            i['id'] = []
#    return list_result

@login_required(login_url='/login/')
def get_chart_data(request):
    ''' 获取曲线图数据
    '''
    search_id = 1
    instrId = request.GET.get('instrId', '')
    instr_name = request.GET.get('instr_name', '')
    if instrId:
        search_id = instrId
        data = Price.objects.filter(instrument_id=search_id).order_by('date_time')
    if instr_name:
        data = Price.objects.filter(instrument_id__instrument_name=instr_name).order_by('date_time')

    result = {'instrument': '', 'time': [], 'price_value': [], 'instrument_fasi': []}
    for i in data:
        result['price_value'].append(int(i.price_value))
        result['instrument_fasi'].append(int(i.instrument_fasi))
        result['time'].append(i.date_time.strftime("%Y-%m-%d"))
        result['instrument'] = i.instrument_id.instrument_name
    result_json = json.dumps(result)
    return HttpResponse(result_json)

@login_required(login_url='/login/')
def set_instr_watch(request):
    ''' 设置关注股票
    '''
    result = {'status': 200}
    user = request.user
    watch_id = request.GET.get('instrId')
    instrument_data = Instrument.objects.filter(id=watch_id)
    obj = InstrWatch(user=user, instrument=instrument_data[0])
    obj.save()
    result_json = json.dumps(result)
    return HttpResponse(result_json)

@login_required(login_url='/login/')
def add_to_list(request):
    list_id = request.GET.get('to_list', '')
    instr_id = request.GET.get('instr_id', '')
    instr_name = request.GET.get('instr_name', '')
    list_obj = Listinter.objects.get(id=list_id)
    if instr_name:
        instr_obj = Instrument.objects.get(instrument_name=instr_name)
    elif instr_id:
        instr_obj = Instrument.objects.get(id=instr_id)

    instr_list = Interlistwatch(
            user = request.user,
            list_name = list_obj,
            inter_list = instr_obj
        )
    instr_list.save()
    if instr_name:
        return HttpResponse(json.dumps({'code': 200, 'instr_id': instr_obj.id}))
    elif instr_id:
        reverse_url = '/stock?in_id=%s'%instr_id
        return HttpResponseRedirect(reverse_url)

@login_required(login_url='/login/')
def get_news(request):
    result = {
        'id': '',
        'title': '',
        'content': '',
        'link': '',
        'fasi': '',
        'time': '',
        'source': '',
        'instrument': {'id': '', 'name': ''},
        'industry': {'id': '', 'name': ''}
    }
    result_list = []
    instr_id = request.GET.get('instrId')
    news_data = News.objects.filter(instrument_id=instr_id)
    #for i in news_data:
    #    result['id']= i.id
    #    result['title'] = i.news_title
    #    result['fasi'] = i.news_fasi
    #    result['content'] = i.news_content
    #    result['link'] = i.news_link
    #    result['time'] = i.news_time.strftime("%Y-%m-%d %H:%M:%S")
    #    result['source'] = i.source
    #    result['instrument']['id'] = i.instrument_id.id
    #    result['instrument']['name'] = i.instrument_id.instrument_name
    #    result['industry']['id'] = i.industry_classification.id
    #    result['industry']['name'] = i.industry_classification.industry_classification_name
    for i in news_data:
        result_list.append({
            'id': i.id,
            'title': i.news_title,
            'content': i.news_content,
            'link': i.news_link,
            'fasi': i.news_fasi,
            'time': i.news_time.strftime("%Y-%m-%d %H:%M:%S"),
            'source': i.source,
            'instrument': {
                'id': i.instrument_id.id,
                'name': i.instrument_id.instrument_name
            },
            'industry': {
                'id': i.industry_classification.id,
                'name': i.industry_classification.industry_classification_name
            }
            })
    result = json.dumps(result_list)
    return HttpResponse(result)

@login_required(login_url='/login/')
def add_watch_list(request):
    user = request.user
    new_watch_name = request.GET.get('watched_name', '')
    watched_list = Listinter(
        user = user,
        name = new_watch_name
    )
    watched_list.save()
    return HttpResponse(200)
