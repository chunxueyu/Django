# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Engineer

def index(request):
    return HttpResponse("Django 呵呵哒！！")

def my_html(req):
    return render(req,"hehe.html")

def get_data(req):
    # 获取数据
    data = Engineer.objects.all()
    print("ok")
    print(data)
    return render(req,"hehe.html",context={"my_data":data})