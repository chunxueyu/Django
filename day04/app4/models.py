from django.db import models

# Create your models here.

class AirCompany(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="公司名字"
    )
    def __str__(self):
        return self.name
class MyAs(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="空姐名字"
    )
    face_score = models.IntegerField(
        verbose_name="颜值"
    )
    ac = models.ForeignKey(
        AirCompany,
        verbose_name="所属单位"
    )
    def get_msg(self):
        return self.name+"的颜值是："+str(self.face_score)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "空姐"