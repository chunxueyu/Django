from django.conf.urls import url
from .views import *

urlpatterns = [
    url("^home$",home,name="home"),
    url("^market$",market,name="market"),
    url("^cart$",cart,name="cart"),
    url("^mine$",mine,name="mine"),
    url("^register$",RegisterAPI.as_view(),name="register"),
    url("^login$",LoginAPI.as_view(),name="login"),
    url(r"^confirm/(.*)",confirm_api),
    url(r"^logout$",logout_api,name="logout")
]