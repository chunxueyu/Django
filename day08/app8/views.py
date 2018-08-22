import time

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from .models import Book
from django.db import connection
from django.core.mail import send_mail, send_mass_mail

# Create your views here.
from django.template import loader
from django.views.decorators.cache import cache_page

from .util import create_random_str


def index(req):
    return render(req,"RTF.html")

# 装饰器实现
@cache_page(60)
def home(req):
    # 模拟查询速度慢的情况
    time.sleep(3)
    return HttpResponse("开心！！！")

def fetch_to_dict(cursor):
    colums = [ i[0] for i in cursor.description]
    return [dict(zip(colums,row)) for row in cursor.fetchall()]

def ys_cache(req):
    data = cache.get("data")
    if data:
        # 走线路一
        return HttpResponse(data)
    else:
        # 走线路二
        # 模拟耗时的数据查询
        time.sleep(3)
        # 获取数据库连接
        cursor = connection.cursor()
        # 执行sql语句
        cursor.execute('select name from app8_book')
        # res = cursor.fetchall()
        # 将结果转成数组嵌套字典的形式
        res = fetch_to_dict(cursor)
        print(res)
        # 缓存数据
        cache.set("data",res[0].get("name"),20)
        return HttpResponse("ok")

def send_my_email(req):
    email_addr = req.GET.get("addr")
    title = "python1808offer"
    msg = "恭喜您在千峰占座成功"
    # 发送者
    email_from = settings.DEFAULT_FROM_EMAIL
    # 接收者
    receives = [email_addr]
    send_mail(
        title,
        msg,
        email_from,
        receives,
        fail_silently=False
    )
    data = {
        "code":1,
        "msg":"邮件发送成功请注意查收",
        "data":[]
    }
    return JsonResponse(data)

def sendmail(req):
    return render(req,"sendemail.html")

def send_email_v2(req):
    addr = req.GET.get('addr')
    #加载我们Email模板页面
    temp = loader.get_template('emtemplate.html')
    #渲染
    html= temp.render({'mail':addr})
    title = 'python1808offer'
    msg = '恭喜你，在千锋占座成功'
    # 发送的地址
    email_from = settings.DEFAULT_FROM_EMAIL
    # 接收的地址
    receives = [addr]
    send_mail(
        title,
        msg,
        email_from,
        receives,
        html_message=html,
        fail_silently=False
    )
    data = {
        'code': 1,
        'msg': '邮件发送成功，请注意查收',
        'data': []
    }
    return JsonResponse(data)

def send_many_email(req):
    msg1 = (
        "标题1",
        "消息体1",
        settings.DEFAULT_FROM_EMAIL,
        ['justforjs@qq.com', '18355092908@163.com']
    )
    msg2 = (
        "标题2",
        "消息体2",
        settings.DEFAULT_FROM_EMAIL,
        ['justforjs@qq.com', '18355092908@163.com','liuda@1000phone.com']
    )
    send_mass_mail((msg1,msg2),fail_silently=False)
    return HttpResponse("本是同根生")

def create_confirm_email(req):
    addr = req.GET.get("addr")
    code = create_random_str()
    url = "http://{host}/app8/confirm/{random_str}".format(
        host = req.get_host(),
        random_str = code
    )
    # 发送邮件
    tmp = loader.get_template("emtemplate.html")
    html = tmp.render({"mail":"恭喜你 加入澳门赌场 真人发牌体验","url":url})
    title = "会员激活"
    msg = ""
    # 发送者
    email_from = settings.DEFAULT_FROM_EMAIL
    # 接收者
    receives = [addr]
    send_mail(
        title,
        msg,
        email_from,
        receives,
        html_message=html,
        fail_silently=False
    )
    # 设置缓存
    cache.set(code,addr,30)
    data = {
        "code": 1,
        "msg": "邮件发送成功请注意查收",
        "data": []
    }
    return JsonResponse(data)

def confirm_api(req,p1):
    # 去缓存  拿p1对应的值
    res = cache.get(p1)
    if res:
        # 根据res  去找对应的用户 然后给用户的状态变成激活态
        return HttpResponse("激活成功，送3000元")
    else:
        return HttpResponse("验证连接无效")