import time

from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test
import logging

logger = logging.getLogger("t09")

# Create your views here.
def index(req):
    logger.info("呵呵")
    # 这里可以随便写个错误
    return HttpResponse("ok")

def celery_test(req):
    n = req.GET.get("n")
    # print("睡前工资10000")
    # time.sleep(int(n))
    # print("睡后1000")
    test.delay(int(n))

    return HttpResponse("好惨")