# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shotchart',
            name='zone11_hit_rate',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]