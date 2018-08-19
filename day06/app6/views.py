import os
import uuid
import hashlib
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def my_login(req):
    if req.method == "GET":
        return render(req,"login.html")
    else:
        # 处理登录逻辑
        param = req.POST
        uname = param.get("uname")
        print(uname)
        pwd = param.get("pwd")
        print(pwd)
        # 验证用户
        user = authenticate(username=uname,password=pwd)
        if user:
            login(req,user)
            return HttpResponse("ok")
        else:
            return HttpResponse("账号或密码错误")

@login_required(login_url="/app6/login")
def get_login_user(req):
    user = req.user
    return HttpResponse("欢迎{u_name}".format(u_name=user.username))

@login_required(login_url="/app6/login")
def upload_img_v1(req):
    if req.method == "GET":
        u_name = req.user.username
        # 获得用户的头像路径
        tmp = req.user.icon
        icon = tmp.url if tmp else ""
        # 拿到访问的域名
        host = req.get_host()
        # 拼接头像的url网址
        icon_str = "http://"+host+"/static/imgs/"+icon
        print (icon_str)
        return render(req,
                      "uploadimg.html",
                      {"uname":u_name,"u_icon":icon_str}
                      )
    else:
        #拿文件数据
        my_img = req.FILES.get("img")
        # 知道是谁上传
        user = req.user
        # 头像数据保存到对应的icon字段上
        user.icon = my_img
        # 保存数据
        user.save()
        return HttpResponse("ok")

def get_unique_name():
    # 获得一个uuid字符串
    uuid_val = uuid.uuid4()
    # 将uuid转成字符串
    uuid_str = str(uuid_val).encode("utf-8")
    # 获得一个md5
    md5 = hashlib.md5()
    # 将uuid字符串  做摘要
    md5.update(uuid_str)
    # 返回32位16进制结果
    return md5.hexdigest()


def upload_img_v2(req):
    if req.method == "POST":
        # 获得图片
        img = req.FILES.get("img")
        # 生成唯一的图片名字
        file_name = get_unique_name() + ".png"
        # 拼接文件路径
        file_path = os.path.join(settings.MEDIA_ROOT,file_name)
        # 打开文件
        with open(file_path,"wb") as fp:
            # 遍历写入我们的本地文件
            for i in img.chunks():
                fp.write(i)
        print(file_path)
        return HttpResponse("ok")

endpoint = 'http://oss-cn-shanghai.aliyuncs.com'
access_key_id = 'LTAIXPTosazV9jSq'
access_key_secret = '7uXYe15rjLzEjStAwVraExvAWFkxIw'
bucket_name = 'share-msg'
bucket_name_host = "share-msg.oss-cn-shanghai.aliyuncs.com"
import io
import oss2
def up_img_v3(req):
    if req.method == "POST":
        # 获得文件的数据
        my_file = req.FILES.get("img")
        # 实例化一个比特流的缓存区
        my_buf = io.BytesIO()

        # 将文件数据写入到缓存区
        for i in my_file.chunks():
            my_buf.write(i)
        # 将文件指针指会缓冲区的头
        my_buf.seek(0)
        # 调用oss的API

        # oss认证
        auth = oss2.Auth(access_key_id, access_key_secret)

        # 获得存储桶
        bucket = oss2.Bucket(auth, endpoint, bucket_name)

        # 获取文图片件后缀
        remote_file_name = get_unique_name() + "." +my_file.name.split(".")[-1]

        # 拼接图片远端的url
        img_url = "https://{host}/{file_name}".format(
            host=bucket_name_host,
            file_name=remote_file_name
        )
        # print(img_url)

        # 将缓存的数据传到oss上
        bucket.put_object(remote_file_name, my_buf.getvalue())

        # 拿用户 保存oss上文件的url
        user = req.user
        user.icon_url = img_url
        user.save()
        return HttpResponse("ok")
