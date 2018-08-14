from django.shortcuts import render
from .models import Trains

# Create your views here.
def my_cars(req):
    data = Trains.objects.filter(speed__lte=1000).order_by("speed")
    result = {
        "title":"火车",
        "carts":data
    }
    return render(req,"trains.html",result)
