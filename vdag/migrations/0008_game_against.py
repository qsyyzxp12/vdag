# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdag', '0007_auto_20170412_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='against',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
