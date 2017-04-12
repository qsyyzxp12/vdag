# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdag', '0004_auto_20170412_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppp',
            name='shot_way',
            field=models.CharField(choices=[(b'D', b'Drive'), (b'PU', b'Pull Up'), (b'SU', b'Spot Up'), (b'TO', b'Turnover'), (b'PO', b'Possession')], default=b'', max_length=2),
        ),
    ]