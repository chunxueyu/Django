from django.conf.urls import url
from .views import *

urlpatterns = [
    url("^login$",login_view),
    url("^welcome$",welcome)
]