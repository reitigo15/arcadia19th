# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-18 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0024_auto_20170918_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resident',
            name='position',
        ),
    ]
