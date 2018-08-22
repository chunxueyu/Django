from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^index$",index),
    url(r"^home$",home),
    url(r"^ys$",ys_cache),
    url(r"^send$",send_my_email),
    url(r"^email$",sendmail),
    url(r"^send_v2$",send_email_v2),
    url(r"^huohuo$",send_many_email),
    url(r"send_v3$",create_confirm_email),
    url(r"^confirm/(.*)",confirm_api)
]