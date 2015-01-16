#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-04

from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.template.response import TemplateResponse
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.forms import AuthenticationForm

from apps.users.forms import UserAddForm

def auth_login(request, template):
    """ 用户登录
    """

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

def auth_logout(request):
    """ 用户退出
    """

    return logout_then_login(request, login_url=settings.LOGIN_REDIRECT_URL)

def register(request, template):
    """用户注册
    """
    form = UserAddForm()
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth_login'))

    return TemplateResponse(request, template, {'form': form})


