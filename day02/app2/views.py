from django.shortcuts import render
from .models import Trains,Stu

# Create your views here.
def my_cars(req):
    data = Trains.objects.filter(speed__lte=1000).order_by("speed")
    result = {
        "title":"火车",
        "carts":data
    }
    return render(req,"trains.html",result)


def my_zuoye(req):
    data = Stu.objects.filter(age__lte=24).order_by("age")
    res = {
        "title":"信息",
        "shu":data
    }
    return render(req,"zuoye.html",res)

def search_by_name(req):
    na = req.GET
    kw = na.get("kw")
    # res = Stu.objects.filter(
    #     name__contains=kw
    # )
    # res = Stu.objects.filter(
    #     name__startswith=kw
    # )
    # res = Stu.objects.filter(age__in=[18,20])
    # res = Stu.objects.filter(birthday__year=1998)
    res = Stu.objects.filter(sex__in=[0])
    return render(req, "zuoye.html", {"shu": res})
