# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 16:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('werewolf', '0012_auto_20170916_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.IntegerField(default=1)),
                ('character_img_url', models.CharField(default='rain/01.png', max_length=100)),
                ('position', models.CharField(default='村人', max_length=100, verbose_name='役職')),
                ('types', models.IntegerField(default=1)),
                ('death_flag', models.IntegerField(default=0)),
                ('resident', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='werewolf.Village')),
            ],
        ),
        migrations.AddField(
            model_name='remark',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
