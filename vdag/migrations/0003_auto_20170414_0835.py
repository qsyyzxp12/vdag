# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 08:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vdag', '0002_shotchart_zone11_hit_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shotchart',
            name='zone10_hit_rate',
        ),
        migrations.RemoveField(
            model_name='shotchart',
            name='zone11_hit_rate',
        ),
        migrations.RemoveField(
            model_name='shotchart',
            name='zone1_hit_rate',
        ),
        migrations.RemoveField(
            model_name='shotchart',
            name='zone2_hit_rate',
        ),
        migrations.RemoveField(
            model_name='shotchart',
            name='zone3_hit_rate',
        ),
        migrations.RemoveField(
            model_name='shotchart',
            name='zone4_hit_rate',
        ),
        migrations.RemoveField(
            model_name='shotchart',
            name='zone5_hit_rate',
        ),
        migrations.RemoveField(
            model_name='shotchart',
            name='zone6_hit_rate',
        ),
        migrations.RemoveField(
            model_name='shotchart',
            name='zone7_hit_rate',
        ),
        migrations.RemoveField(
            model_name='shotchart',
            name='zone8_hit_rate',
        ),
        migrations.RemoveField(
            model_name='shotchart',
            name='zone9_hit_rate',
        ),
    ]
