from django.conf.urls import url
from .views import my_cars

urlpatterns = [
    url(r'^train$',my_cars)
]