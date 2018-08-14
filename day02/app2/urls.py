from django.conf.urls import url
from .views import my_cars,search_by_name

urlpatterns = [
    url(r'^train$',my_cars),
]