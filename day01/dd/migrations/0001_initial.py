# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-13 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u4f60\u7684\u540d\u5b57')),
                ('age', models.IntegerField(default=18)),
            ],
        ),
    ]
