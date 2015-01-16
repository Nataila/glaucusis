#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-07

from django import forms
from django.contrib.auth.models import User

class UserAddForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件：')

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'].strip().lower(),
            self.cleaned_data['email'].strip(),
            self.cleaned_data['password'].strip()
        )
        #user_profile = UserProfile.objects.create(
        #    user=user,
        #    realname=self.cleaned_data['realname'].strip(),
        #    email=self.cleaned_data['email'].strip(),
        #    tel=self.cleaned_data['tel'].strip(),
        #    fax=self.cleaned_data['fax'].strip(),
        #    mobile=self.cleaned_data['mobile'].strip(),
        #    address=self.cleaned_data['address'].strip(),
        #)

        #if commit:
        user.save()
        #    user_profile.save()

        return user


