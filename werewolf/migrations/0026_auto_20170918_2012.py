# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-18 20:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0025_remove_resident_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resident',
            old_name='death_flag',
            new_name='deathflag',
        ),
    ]
