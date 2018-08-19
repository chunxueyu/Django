from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r"^login$",my_login,name="login"),
    url(r"^test$",get_login_user),
    url(r"^up_img_v1$",upload_img_v1,name="up_v1"),
    url(r"^up_img_v2$",upload_img_v2,name="up_v2"),
    # url(r"^up_img_v3$",up_img_v3,name="up_v3")
]
