# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-25 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180825_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=20)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=200, null=True)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.BooleanField(default=0)),
                ('pmdesc', models.BooleanField(default=0)),
                ('specifics', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('marketprice', models.FloatField()),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=10)),
                ('dealerid', models.CharField(max_length=20)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]
