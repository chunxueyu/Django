from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View
from .utils import *

def home(req):
    # 读取轮播数据
    wheels = MyWheel.objects.all()
    navs = MyNav.objects.all()
    # 必购得数据
    musts = MustBuy.objects.all()
    shops = Shop.objects.all()
    mains = MainShow.objects.all()
    data = {
        "title": "首页",
        "wheels": wheels,
        "navs": navs,
        "musts":musts,
        "shop0":shops[0],
        "shop1_3":shops[1:3],
        "shop3_7":shops[3:7],
        "shop_last":shops[7:],
        "mains":mains
    }
    return render(req,"home/home.html",data)

def market(req):
    return render(req,"market/market.html",{"title":"闪购"})

def cart(req):
    return render(req,"cart/cart.html",{"title":"购物车"})

def mine(req):
    user = req.user
    is_login = False
    username = ""
    u_icon = ""
    if isinstance(user,MyUser):
        is_login = True
        username = user.username
        if user.icon:
            u_icon = "http://"+req.get_host()+"/static/uploads/"+user.icon.url
        data = {
            "title":"我的",
            "is_login":is_login,
            "u_name":username,
            "icon":u_icon
        }
        return render(req,"mine/mine.html",data)
    else:
        data = {
            "title": "我的",
            "is_login": is_login,
            "u_name": username,
            "icon": u_icon
        }
        return render(req, "mine/mine.html", data)

# 注册
class RegisterAPI(View):
    def get(self,req):
        return render(req,'user/register.html')
    def post(self,req):
        param = req.POST
        u_name = param.get("uname")
        pwd = param.get("pwd")
        c_pwd = param.get("c_pwd")
        email = param.get("email")
        icon = req.FILES.get("icon")
        if u_name and len(u_name) > 3:
            if MyUser.objects.filter(username=u_name).exists():
                return HttpResponse("该用户名已经被注册了")
            else:
                if pwd and len(pwd)>0 and pwd == c_pwd:
                    user = MyUser.objects.create_user(
                        username=u_name,
                        password=pwd,
                        email=email,
                        icon=icon,
                        is_active=False
                    )
                    # if send_confirm_email(user,req.get_host()):
                    #     return HttpResponse("恭喜您注册成功")
                    # else:
                    #     return HttpResponse("验证邮件发送失败")
                     # 发送邮箱验证
                    code = create_random_str()
                    url = "http://{host}/axf/confirm/{random_str}".format(
                        host = req.get_host(),
                        random_str = code
                    )
                    tmp = loader.get_template("user/yanzheng.html")
                    html = tmp.render({"mail":"恭喜你 加入爱鲜蜂","url":url})
                    title ="会员激活"
                    msg = ""
                    # 发送者
                    email_from = settings.DEFAULT_FROM_EMAIL
                    # 接收者
                    receives = [email]
                    send_mail(
                        title,
                        msg,
                        email_from,
                        receives,
                        html_message=html,
                        fail_silently=False
                    )
                    cache.set(code,email,60*5)
                    return render(req,"user/sendemail.html",{"uname":u_name})
                else:
                    return HttpResponse("密码和确认密码必须保持一致")
        else:
            return HttpResponse("用户名必须大于3位")

# 登录
class LoginAPI(View):
    def get(self,req):
        return render(req,'user/login.html')
    def post(self,req):
        params = req.POST
        uname = params.get("uname")
        pwd = params.get("pwd")
        # 校验数据
        if uname and pwd and len(uname)>=3 and len(pwd)>0:
            # 校验用户
            user = authenticate(username=uname,password=pwd)
            if user:
                login(req,user)
                return redirect(reverse("axf:mine"))
            else:
                return redirect(reverse("axf:login"))
        else:
            return HttpResponse("别瞎搞")

# 用户认证
def confirm_api(req, random_str):
    # 去缓存  拿random_str对应的值
    res = cache.get(random_str)
    if res:
        # 根据res  去找对应的用户 然后给用户的状态变成激活态
        user = MyUser.objects.get(email=res)
        print(user)
        user.is_active = True
        user.save()
        # MyUser.objects.filter(pk=int(res)).update(
        #     is_active=True
        # )
        return render(req, "user/login.html", {"uname": user})
        # return redirect(reverse("axf:login"))
    else:
        return HttpResponse("验证链接无效")

# 退出
def logout_api(req):
    logout(req)
    return redirect(reverse("axf:mine"))
