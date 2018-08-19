from django.contrib.auth.backends import ModelBackend
from .models import MyUser

class MyBackend(ModelBackend):
    def authenticate(self,request,username=None,password=None,**kwargs):
        # 通过username去找用户
        user = None
        try:
            user = MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            try:
                user = MyUser.objects.get(phone=username)
            except MyUser.DoesNotExist:
                return None
        # 找到用户 去做校验密码
        if user.check_password(password):
            return user
        else:
            return None