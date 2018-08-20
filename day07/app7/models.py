from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="家庭名字"
    )


class Person(models.Model):
    name = models.CharField(
        verbose_name="名字",
        max_length=30
    )
    age = models.IntegerField(
        verbose_name="年纪"
    )
    home = models.ForeignKey(
        Home,
        null=True
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="人类"

