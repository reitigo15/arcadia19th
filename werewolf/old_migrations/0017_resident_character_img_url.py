# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-17 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0016_resident'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='character_img_url',
            field=models.CharField(default='rain/01.png', max_length=100),
        ),
    ]
