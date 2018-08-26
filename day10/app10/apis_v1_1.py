from django.forms import model_to_dict
from django.http import JsonResponse, QueryDict
from django.views.generic import View
from .mysignal import *

from .models import *


NOT_FOUND = 2
SUCCESS = 1
class AdminAPI(View):
    def get(self,req):
        a_id = int(req.GET.get("aid"))
        mysignal.send(sender="有钱人",pa1="川菜",pa2="在如家吃")
        try:
            res = MyAdmin.objects.get(pk=a_id)
        except:
            data = {
                'code':NOT_FOUND,
                'msg':"没有此id对应的数据",
                'data':None
            }
            return JsonResponse(data)
        data = {
            'code':SUCCESS,
            'data':model_to_dict(res),
            'msg':"ok"
        }
        return JsonResponse(data)

    def post(self,req):
        aid = int(req.POST.get("aid",2))
        desc = req.POST.get("desc")
        # res = MyAdmin.objects.create(
        #     user_id=aid,
        #     desc=desc
        # )
        admin = MyAdmin()
        admin.user_id = 2
        admin.desc = "这是描述"
        admin.save()
        data = {
            'code':SUCCESS,
            'msg':"created",
            'data':model_to_dict(res)
        }
        return JsonResponse(data)

    def delete(self,req):
        params = QueryDict(req.body)
        print(params)
        aid = params.get("aid")
        MyAdmin.objects.get(pk=int(aid)).delete()

        data = {
            "code":SUCCESS,
            'msg':"deleted",
            "data":{
                "admin_id":aid,
            }
        }
        return JsonResponse(data)