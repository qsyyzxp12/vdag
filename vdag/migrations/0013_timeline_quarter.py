# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 06:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdag', '0012_timeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='quarter',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]