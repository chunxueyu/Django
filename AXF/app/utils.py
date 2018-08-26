import hashlib
import uuid

from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.template import loader


def create_random_str():
    uid = uuid.uuid4()
    uid_str = str(uid).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uid_str)
    return md5.hexdigest()


def send_confirm_email(user,host):
    # 拼接验证链接
    random_str = create_random_str()
    url = "http://{host}/axf/confirm/{random_str}".format(
        host=host,
        random_str=random_str
    )
    # 发送邮件
    temp = loader.get_template("user/yanzheng.html")
    # 渲染模板
    html = temp.render({"url":url})
    # 拼接邮件的发送内容
    title = "血色浪漫"
    msg = ""
    email_from = settings.DEFAULT_FROM_EMAIL
    receivers = [user.email]
    send_mail(
        title,
        msg,
        email_from,
        receivers,
        fail_silently=False,
        html_message=html
    )
    # 设置缓存
    cache.set(random_str,user.id,settings.CACHE_AGE)
    return True