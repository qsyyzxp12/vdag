# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdag', '0006_auto_20170412_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppp',
            name='result',
            field=models.CharField(blank=True, choices=[(b'M', b'Made'), (b'A', b'Attempt'), (b'F', b'Foul'), (b'Pts', b'Points')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='ppp',
            name='value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='ppp',
            unique_together=set([('game', 'offense_way', 'shot_way', 'result')]),
        ),
    ]
