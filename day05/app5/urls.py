from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r"^game$",game),
    url(r"^test",ttreq),
    url(r"^index",index,name="index"),
    url(r"^login$",login_api,name="login"),
    url(r"^logout$",logout_api,name="logout")
]