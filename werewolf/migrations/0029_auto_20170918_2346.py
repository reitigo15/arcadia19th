# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-18 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0028_auto_20170918_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='village',
            name='daytime_length',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='village',
            name='nighttime_length',
            field=models.IntegerField(),
        ),
    ]
