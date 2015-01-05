#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-04

from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template.response import TemplateResponse
from django.contrib.auth.forms import AuthenticationForm

def auth_login(request, template):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                redirect_to = request.GET.get('next', settings.LOGIN_REDIRECT_URL)
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponse('account error')
        else:
            return HttpResponse('pass')

    return TemplateResponse(request, template, {'form': form})
