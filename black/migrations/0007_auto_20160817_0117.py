# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 16:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('black', '0006_auto_20160817_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=0, default=5, help_text='10점 만점, 높을수록 극혐!', max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
