from django.http import HttpResponse, QueryDict, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.urls import reverse


def game(req):
    return render(req,"2048.html")


def ttreq(request):
    # print(dir(request))
    # print(request.POST)  # POST请求
    # print(request.COOKIES)  #打印cookie
    # print(request.method)  # 打印请求方法
    # print(request.META.get("REMOTE_ADDR"))  #客户端ip
    # print(request.FILES)
    # print("&&&&&&&&&&")
    # param = QueryDict(request.body)
    # print(param)

    # print(request.path)  #拿请求域名
    # print(request.get_host())  #那域名加端口
    # print(request.get_port())  #拿端口
    # response = HttpResponse()  # 实例化对象
    # response.content="呵呵"
    # response.status_code=404   #设置状态码
    # response.write("!!哈哈哈")  #追加内容
    # response.flush()   #冲刷缓冲区
    # response.content = "捉迷藏"  # 覆盖，会覆盖之前的内容

    # return HttpResponse("ok")
    # return response

    my_dict = {"key":"呵呵"}
    return JsonResponse(my_dict)


#首页api
def index(req):
    user_name = req.COOKIES.get("uname","游客")
    data = req.session.get('msg')
    print(data)
    return render(req,"index.html",{"u_name":user_name})

def login_api(req):
    #如果是get请求 返回页面
    if req.method == "GET":
        return render(req,"login.html")
    else:
        # post请求就去处理登陆逻辑
        param = req.POST
        u_name = param.get("uname")
        pwd = param.get("pwd")
        # 设置session
        req.session['msg'] = "ok"
        #假装这里有校验 并且校验通过
        response = HttpResponseRedirect("/app5/index")
        # 设置cookie,并在10秒后过期
        response.set_cookie("uname",u_name,max_age=10)
        return response

def logout_api(req):
    response = HttpResponseRedirect(reverse("app5:index"))
    # 删除session
    del req.session['msg']
    # 删除uname对应的cookie
    response.delete_cookie("uname")
    return response