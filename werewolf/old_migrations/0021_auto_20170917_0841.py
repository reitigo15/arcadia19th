# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-17 08:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0020_auto_20170917_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='types',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='remark',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='resident',
            name='resident',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
