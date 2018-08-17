from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="队名"
    )
    def __str__(self):
        return self.name

class PlayerManger(models.Manager):
    def create_player(self,u_name):
        p = Player()
        p.name = u_name
        p.age = 18
        p.team_id = 1
        p.is_live = True
        p.save()
        return p

class Player(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    age = models.IntegerField(
        verbose_name="年纪"
    )
    is_live = models.BooleanField(
        verbose_name="是否退役"
    )
    team = models.ForeignKey(
        Team,
        null=True,
        verbose_name="归属球队"
    )
    obj = models.Manager()
    my_obj = PlayerManger()
    objects = models.Manager()
    def __str__(self):
        return self.name

class IdCard(models.Model):
    num = models.CharField(
        max_length=19,
        verbose_name="身份证号"
    )
    org = models.CharField(
        max_length=30,
        verbose_name="签发单位"
    )

class Person(models.Model):
    name = models.CharField(
        max_length=30
    )
    idcard = models.OneToOneField(
        IdCard,
        on_delete=models.PROTECT
    )

class Author(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        verbose_name="书名",
        max_length=30
    )
    author = models.ManyToManyField(
        Author,
        verbose_name="作者"
    )
    def __str__(self):
        return self.title
class Human(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    age = models.IntegerField(
        verbose_name="年纪"
    )
    height = models.FloatField(
        verbose_name="身高"
    )
    class Meta:
        # 声明此类是抽象类
        abstract = True
class Boy(Human):
    salary = models.CharField(
        max_length=20
    )
class Girl(Human):
    face_score = models.IntegerField(
        verbose_name="颜值"
    )

class Language(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="语种"
    )
    history = models.IntegerField(
        max_length=5,
        verbose_name="出现历史"
    )
    u_number = models.IntegerField(
        max_length=10,
        verbose_name="使用人数"
    )
    def __str__(self):
        return self.name