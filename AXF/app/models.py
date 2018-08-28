from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    p_choices = (
        (1, '普通用户'),
        (2, 'vip用户'),
        (4, '管理员'),
        (8, '超级管理员')
    )
    icon = models.ImageField(
        upload_to="icons",
        verbose_name="头像"
    )
    address = models.CharField(
        verbose_name="收获地址",
        max_length=200
    )
    phone = models.CharField(
        verbose_name="联系方式",
        max_length=13
    )
    permission = models.IntegerField(
        verbose_name="权限",
        choices=p_choices,
        default=1
    )

class BaseData(models.Model):
    img = models.CharField(
        max_length=255
    )
    name = models.CharField(
        max_length=40
    )
    trackid = models.CharField(
        max_length=10
    )
    class Meta:
        abstract=True

class MyWheel(BaseData):
    class Meta:
        db_table = "axf_wheel"

class MyNav(BaseData):
    class Meta:
        db_table = "axf_nav"

class MustBuy(BaseData):
    class Meta:
        db_table = "axf_mustbuy"

class Shop(BaseData):
    class Meta:
        db_table = "axf_shop"

class MainShow(BaseData):
    categoryid = models.CharField(
        max_length=100
    )
    brandname = models.CharField(
        max_length=100
    )

    img1 = models.CharField(
        max_length=255
    )
    childcid1 = models.CharField(
        max_length=100
    )
    productid1 = models.CharField(
        max_length=100
    )
    longname1 = models.CharField(
        max_length=100
    )
    price1 = models.CharField(
        max_length=100
    )
    marketprice1 = models.CharField(
        max_length=100
    )

    img2 = models.CharField(
        max_length=255
    )
    childcid2 = models.CharField(
        max_length=100
    )
    productid2 = models.CharField(
        max_length=100
    )
    longname2 = models.CharField(
        max_length=100
    )
    price2 = models.CharField(
        max_length=100
    )
    marketprice2 = models.CharField(
        max_length=100
    )
    img3 = models.CharField(
        max_length=255
    )
    childcid3 = models.CharField(
        max_length=100
    )
    productid3 = models.CharField(
        max_length=100
    )
    longname3 = models.CharField(
        max_length=100
    )
    price3 = models.CharField(
        max_length=100
    )
    marketprice3 = models.CharField(
        max_length=100
    )
    class Meta:
        db_table = "axf_mainshow"

class Goods(models.Model):
    productid = models.CharField(
        max_length=20
    )
    productimg = models.CharField(
        max_length=200
    )
    productname = models.CharField(
        max_length=200,
        null=True
    )
    productlongname = models.CharField(
        max_length=200
    )
    isxf = models.BooleanField(
        default=0
    )
    pmdesc = models.BooleanField(
        default=0
    )
    specifics = models.CharField(
        max_length=20
    )
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(
        max_length=10
    )
    dealerid = models.CharField(
        max_length=20
    )
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    current_num = models.IntegerField(
        default=0,
        verbose_name="当前数量"
    )

    def __str__(self):
        return str(self.price)

    class Meta:
        db_table = "axf_goods"

class GoodsTypes(models.Model):
    typeid = models.CharField(
        max_length=40
    )
    typename = models.CharField(
        max_length=10
    )
    childtypenames = models.CharField(
        max_length=200,
    )
    typesort = models.IntegerField()

    class Meta:
        db_table = "axf_foodtypes"

class Cart(models.Model):
    user = models.ForeignKey(
        MyUser,
        verbose_name="用户"
    )
    goods = models.ForeignKey(
        Goods,
        verbose_name="商品"
    )
    num = models.IntegerField(
        verbose_name="数量",
        default=1
    )
    is_select = models.BooleanField(
        verbose_name="选中状态",
        default=True
    )
    class Meta:
        verbose_name = "购物车"
        index_together = ("user","is_select")

class Order(models.Model):
    ORDER_STATUS = (
        (1,"未付款"),
        (2,"未发货"),
        (3,"未收货"),
        (4,"未评价"),
        (5,"完成")
    )
    user = models.ForeignKey(
        MyUser
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    status = models.IntegerField(
        choices=ORDER_STATUS,
        default=1
    )
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        db_index=True
    )
    goods = models.ForeignKey(
        Goods
    )
    num = models.IntegerField(
        verbose_name="数量"
    )