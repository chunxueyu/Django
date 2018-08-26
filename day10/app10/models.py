from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    p_choices = (
        (1,'普通用户'),
        (2,'vip用户'),
        (4,'管理员'),
        (8,'超级管理员')
    )
    permission = models.IntegerField(
        verbose_name="权限",
        choices=p_choices
    )


class MyAdmin(models.Model):
    desc = models.CharField(
        max_length=200,
        verbose_name="呵呵"
    )
    user = models.OneToOneField(
        MyUser
    )