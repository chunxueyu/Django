# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render



# Create your models here.
from  .models import Engineer
from  .models import Language

def index(request):
    return HttpResponse("<h1>Django 呵呵哒！！</h1>")

def my_html(request):
    return render(request,"my_index.html")

def get_data(req):
    #获取数据
    data = Engineer.objects.all()
    print(data)
    return render(req,"my_index.html",context={"my_data":data})

def zuoye(req):
    data = Language.objects.all()
    print(data)
    return render(req,"zuoye.html",context={"my_data":data})
