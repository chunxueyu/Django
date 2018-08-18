from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def register_api(req):
    if req.method == "GET":
        return render(req,"user/register.html")
    else:
        # 获取post请求参数
        param = req.POST
        u_name = param.get("u_name")
        pwd = param.get("pwd")
        c_pwd = param.get("confirm_pwd")
        # 校验用户名
        if len(u_name) >= 3:
            # 用户名是否被人注册了
            if User.objects.filter(username=u_name).exists():
                return HttpResponse("坚持住 这名不能用")
            else:
                # 校验密码
                if pwd and len(pwd) > 3 and pwd == c_pwd:
                    # 校验通过去创建用户
                    User.objects.create_user(
                        username=u_name,
                        password=pwd
                    )
                    # 跳转登录页
                    # return redirect(reverse("register:login"))
                    return HttpResponse("注册成功")
                else:
                    return HttpResponse("两次密码不一致")
        else:
            return HttpResponse("用户名长度过短")

def login_api(req):
    if req.method == "GET":
        return render(req,"user/login.html")
    else:
        # 登录逻辑
        param = req.POST
        u_name = param.get("uname")
        pwd = param.get("pwd")
        # 校检数据长度
        if pwd and len(pwd) >= 3 and u_name and len(u_name) >=3:
            # 校检用户
            user = authenticate(username=u_name,password=pwd)
            if user:
                # 校验通过  获得用户 那我们让用户登陆
                login(req,user)
                return render(req,"index.html",{"u_name":user.username})
            else:
                return render(req,"user/login.html")
        else:
            return HttpResponse("用户名或密码过短")

def logout_api(req):
    logout(req)
    return render(req,"index.html",{"u_name":"游客"})