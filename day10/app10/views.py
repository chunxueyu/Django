from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from  .decorators import api_permission_check,myadmin_required


# Create your views here.
def login_view(req):
    if req.method == "GET":
        return render(req,"login.html")
    else:
        param = req.POST
        uname = param.get("uname")
        pwd = param.get("pwd")
        user = authenticate(username=uname,password=pwd)
        if user:
            login(req,user)
            return redirect("/app10/welcome")  # 重定向
        else:
            return HttpResponse("error")


# @api_permission_check(4)
@myadmin_required
@login_required(login_url="/app10/login")
def welcome(req):
    user = req.user
    return HttpResponse("欢迎"+user.username)
