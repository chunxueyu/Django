from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

ads = ["IT教育哪家强","你好他也好","美女荷官，真人体验"]
goods = ["该发工资了","我看见你跟妹子。。。。"]
class AdvertisMiddleware(MiddlewareMixin):
    def process_request(self,req):
        path =req.path
        if path == "/app6/test":
            leads = ['hehe','114.242.26.54']
            # print(req.META.get("REMOTE_ADDR"))
            ip = req.META.get("REMOTE_ADDR")
            if ip in leads:
                return render(req,"advs.html",{"ads":goods})
            else:
                return render(req,"advs.html",{"ads":ads})
        else:
            pass