from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

from .models import *

# Create your views here.
def my_as(req):
    my_data = MyAs.objects.filter()
    tmp = loader.get_template("myas.html")
    print(tmp)
    my_code = "<h2>呵呵哒</h2>"
    my_str = tmp.render({"ass":my_data,"code":my_code})
    print(my_str)
    return HttpResponse(my_str)
    # return render(req,"myas.html",{"ass":[]})

def my_search(req,hh1,hh2):
    print(hh1,hh2)
    #那参数
    kw = req.GET.get("kw","")
    # 拿数据
    data = MyAs.objects.filter(
        Q(name__contains=kw) | Q(ac__name__contains=kw)
    )
    return render(req,"homework.html",{"ass":data})


#重定向
def index(req):
    # return HttpResponseRedirect("/app4/as")
    # return HttpResponseRedirect(reverse("python1808:ashehe")) #urls也要改name="ashehe"
    #设置默认
    # return redirect(reverse("python1808:getas",args=(3,)))
    #给网址设置自定义参数
    return redirect(reverse("py:hzn", kwargs={"hh2": 23, "hh1": 30}))

def get_as_by_id(req,a_id,extra):#extra是额外加的解析路径
    # 获取空姐信息
    aid = int(a_id)
    # 根据id拿到空姐信息
    my_as = MyAs.objects.get(id=aid)
    # 返回给前端
    return HttpResponse(my_as.name+extra)

def home(req):
    return render(req,"child.html")

def h(req):
    return render(req,"work.html")
