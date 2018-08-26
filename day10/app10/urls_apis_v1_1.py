from django.conf.urls import url
from .apis_v1_1 import *

urlpatterns = [
    url(r"^admin$",AdminAPI.as_view())  # 在这里配置这个之后，会自动进入这个类找对应的函数去执行
]
