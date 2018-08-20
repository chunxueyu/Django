from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^person/(\d+)",persons_api,name="person"),
    url(r"^img",get_confirm_img,name="img"),
    url(r"^my_login$",my_login),
    url(r"^confirm$",confirm_api)
]