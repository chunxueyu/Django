# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-27 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180827_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='current_num',
            field=models.IntegerField(default=0, verbose_name='当前数量'),
        ),
    ]
