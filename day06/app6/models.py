from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    sex_choice = (
        (1,"男"),
        (2,"女"),
        (3,"男女")
    )
    age = models.IntegerField(
        verbose_name="年纪"
    )
    phone = models.CharField(
        max_length=13
    )
    sex = models.IntegerField(
        choices = sex_choice
    )
    icon = models.ImageField(
        upload_to="icons",
        null=True
    )
    icon_url = models.CharField(
        max_length=255,
        verbose_name="头像路径",
        null=True
    )




