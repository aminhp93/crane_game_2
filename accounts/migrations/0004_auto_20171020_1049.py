# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 10:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20171020_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 10, 20, 10, 49, 52, 390424, tzinfo=utc), null=True),
        ),
    ]