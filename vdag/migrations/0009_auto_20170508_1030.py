# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vdag', '0008_auto_20170508_0952'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='defense',
            unique_together=set([('game', 'isTeamDefense', 'player', 'quarter')]),
        ),
    ]
