# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-15 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=19, verbose_name='身份证号')),
                ('org', models.CharField(max_length=30, verbose_name='签发单位')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('idcard', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app3.IdCard')),
            ],
        ),
        migrations.AlterModelManagers(
            name='player',
            managers=[
                ('obj', django.db.models.manager.Manager()),
            ],
        ),
    ]