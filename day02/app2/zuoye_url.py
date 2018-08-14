from django.conf.urls import url
from .views import my_zuoye

urlpatterns = [
    url(r'^zuoye$',my_zuoye)
]