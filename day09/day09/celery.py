from __future__ import absolute_import
from  django.conf import settings
import os
from celery import Celery,platforms


os.environ.setdefault("DJANGO_SETTING_MODULE",'day09.settings')

app = Celery("hehe")
platforms.C_FORCE_ROOT = True   # 使用root去开启celery时，需要加这个
app.conf.CELERY_TIMEZONE = "Asia/Shanghai"   # 或者settings.TIME_ZONE
app.config_from_object("django.conf:settings")

# 如果想celeery自动发现你的任务 需要在app目录下  新建一个叫tasks.py的文件
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)
