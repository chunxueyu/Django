from django.db import models

# Create your models here.
class Trains(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    speed = models.IntegerField(
        verbose_name="时速",
        default=300,
        db_column="my_speed"
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="出场日期"
    )
    repair = models.DateField(
        auto_now=True
    )
    is_used = models.BooleanField(
        default=True,
        verbose_name="是否在用"
    )
    def __str__(self):
        return self.name+str(self.speed)
    class Meta:
        verbose_name="火车类"
        db_table="火车"


class Stu(models.Model):
    name = models.CharField(
        verbose_name="名字",
        max_length=30
    )
    sex = models.BooleanField(
        default=1,
        verbose_name="性别"
    )
    age = models.IntegerField(
        verbose_name="年龄"
    )
    birthday = models.DateField(
        auto_now=True
    )
    def __str__(self):
        return self.name+str(self.age)
    class Meta:
        verbose_name = "修改名字"
        db_table="信息表"

