# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20170901_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='productincard',
            name='session_key',
            field=models.CharField(default=None, max_length=128),
        ),
    ]
