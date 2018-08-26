from django.http import HttpResponse,HttpResponseForbidden


def api_permission_check(permission):
    def outer(func):
        def inner(req,*args,**kwargs):
            user = req.user
            if user.permission&permission == permission:
                return func(req,*args,**kwargs)
            else:
                return HttpResponseForbidden()
        return inner
    return outer

def myadmin_required(func):
    def inner(req,*args,**kwargs):
        user = req.user
        if hasattr(user,"myadmin"):
            return func(req,*args,**kwargs)
        else:
            return HttpResponseForbidden()
    return inner