#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse, render,redirect

from rbac import models


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    current_user = models.UserInfo.objects.filter(name=user, password=pwd).first()
    if not current_user:
        return render(request, 'login.html', {'msg': '用户名或密码错误'})



    return redirect('/customer/list/')
