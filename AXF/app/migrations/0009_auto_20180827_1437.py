# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-27 06:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_goodstypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=1, verbose_name='数量')),
                ('is_select', models.BooleanField(default=True, verbose_name='选中状态')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '购物车',
            },
        ),
        migrations.AlterIndexTogether(
            name='cart',
            index_together=set([('user', 'is_select')]),
        ),
    ]
