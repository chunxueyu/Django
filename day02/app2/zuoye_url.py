from django.conf.urls import url
from .views import my_zuoye,search_by_name

urlpatterns = [
    url(r'^zuoye$',my_zuoye),
    url(r"^hehe", search_by_name)
]