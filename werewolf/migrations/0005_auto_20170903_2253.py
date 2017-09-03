# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-03 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0004_auto_20170903_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='remark',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='remark',
            name='serial_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='remark',
            name='text',
            field=models.TextField(verbose_name='本文'),
        ),
        migrations.AlterField(
            model_name='remark',
            name='user',
            field=models.CharField(max_length=200, verbose_name='ユーザ名'),
        ),
    ]